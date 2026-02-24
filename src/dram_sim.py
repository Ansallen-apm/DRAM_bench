
class BankState:
    """
    Tracks the state and timing constraints of a single DRAM Bank.
    追蹤單一 DRAM Bank 的狀態與時序限制。
    """
    def __init__(self, id, config):
        self.id = id
        self.config = config

        # State
        self.is_open = False
        self.open_row = None

        # Timing trackers (Cycle when the command was issued)
        # 時序追蹤器 (紀錄指令發出的週期)
        self.last_act = -10000
        self.last_pre = -10000
        self.last_read = -10000
        self.last_write = -10000

        # Parameters
        self.tRP = config['tRP']
        self.tRCD = config['tRCD']
        self.tRAS = config['tRAS']
        self.tRC = config['tRC']
        self.tCL = config['tCL']
        self.tCWL = config['tCWL']
        self.tWR = config['tWR']
        self.tCCD = config.get('tCCD', 4)
        self.tRTP = max(4, config.get('tRTP', 8))

    def get_next_act_time(self):
        """
        Calculates the earliest time an ACT command can be issued.
        計算 ACT 指令最早可發出的時間。
        Constraints: tRP from PRE, tRC from ACT.
        限制：來自 PRE 的 tRP，來自 ACT 的 tRC。
        """
        return max(self.last_pre + self.tRP, self.last_act + self.tRC)

    def get_next_pre_time(self):
        """
        Calculates the earliest time a PRE command can be issued.
        計算 PRE 指令最早可發出的時間。
        """
        bl_cycles = self.config['BurstLength'] // 2
        wr_rec = self.last_write + self.tCWL + bl_cycles + self.tWR
        rd_rec = self.last_read + self.tRTP
        return max(self.last_act + self.tRAS, wr_rec, rd_rec)

    def get_next_read_time(self):
        """
        Calculates the earliest time a READ command can be issued.
        計算 READ 指令最早可發出的時間。
        """
        return max(self.last_act + self.tRCD, self.last_read + self.tCCD, self.last_write + self.tCCD)

    def get_next_write_time(self):
        """
        Calculates the earliest time a WRITE command can be issued.
        計算 WRITE 指令最早可發出的時間。
        """
        return max(self.last_act + self.tRCD, self.last_write + self.tCCD, self.last_read + self.tCCD)


class DRAMController:
    """
    Simulates the DRAM Memory Controller.
    模擬 DRAM 記憶體控制器。
    """
    def __init__(self, config, mapper, scheduler_type='FIFO', queue_depth=16):
        self.config = config
        self.mapper = mapper
        self.scheduler_type = scheduler_type
        self.queue_depth = queue_depth

        self.current_time = 0
        self.queue = []
        self.banks = {}
        self.completed_requests = 0

        self.data_bus_free_time = 0
        self.cmd_bus_free_time = 0

        # Global ACT Constraints
        # 全域 ACT 限制
        self.act_history = {} # (Channel, Rank) -> List of ACT timestamps
        self.tRRD = config.get('tRRD', 0)
        self.tFAW = config.get('tFAW', 0)

        self.stats = {
            'total_cycles': 0,
            'page_hits': 0,
            'page_misses': 0,
            'page_conflicts': 0,
            'bus_busy_cycles': 0,
            'total_bytes': 0,
            'cumulative_queue_depth': 0,
            'queue_depth_samples': 0
        }

        self.burst_cycles = config['BurstLength'] // 2

    def get_bank(self, req):
        """
        Retrieves or creates the BankState object for a request.
        取得或建立請求對應的 BankState 物件。
        """
        if 'mapped' not in req:
            req['mapped'] = self.mapper.map_address(req['address'])
        key = (req['mapped'].get('Channel', 0), req['mapped'].get('Rank', 0), req['mapped']['Bank'])
        if key not in self.banks:
            self.banks[key] = BankState(key, self.config)
        return self.banks[key]

    def get_command_status(self, req):
        """
        Determines the next required command and its readiness.
        決定下一個需要的指令及其就緒狀態。
        Returns: (is_ready, command_type, next_ready_time)
        回傳：(是否就緒, 指令類型, 下次就緒時間)
        """
        bank = self.get_bank(req)
        row = req['mapped']['Row']

        if bank.is_open:
            if bank.open_row == row:
                # Target Row Open -> RD/WR
                # 目標 Row 已開啟 -> 執行 RD/WR
                cmd_type = 'WR' if req['is_write'] else 'RD'
                if cmd_type == 'WR':
                    ready_time = bank.get_next_write_time()
                    latency = self.config['tCWL']
                else:
                    ready_time = bank.get_next_read_time()
                    latency = self.config['tCL']

                duration = req['burst_count'] * self.burst_cycles
                min_issue_time = max(ready_time, self.data_bus_free_time - latency)

                return (min_issue_time <= self.current_time), cmd_type, min_issue_time

            else:
                # Conflict -> PRE
                # Row 衝突 -> 執行 PRE
                ready_time = bank.get_next_pre_time()
                return (ready_time <= self.current_time), 'PRE', ready_time
        else:
            # Closed -> ACT
            # Bank 關閉 -> 執行 ACT
            ready_time = bank.get_next_act_time()

            # Global ACT Constraints (tRRD, tFAW) per Rank
            # 每個 Rank 的全域 ACT 限制 (tRRD, tFAW)
            rank_key = (req['mapped'].get('Channel', 0), req['mapped'].get('Rank', 0))
            history = self.act_history.get(rank_key, [])

            trrd_constraint = 0
            tfaw_constraint = 0

            if history:
                trrd_constraint = history[-1] + self.tRRD

            if len(history) >= 4:
                tfaw_constraint = history[-4] + self.tFAW

            final_ready_time = max(ready_time, trrd_constraint, tfaw_constraint)

            return (final_ready_time <= self.current_time), 'ACT', final_ready_time

    def issue_command(self, req_idx, cmd_type):
        """
        Issues a command for the request at req_idx.
        對 req_idx 的請求發出指令。
        Returns True if request is completed (RD/WR done), False otherwise.
        若請求完成 (RD/WR 結束) 回傳 True，否則回傳 False。
        """
        req = self.queue[req_idx]
        bank = self.get_bank(req)
        row = req['mapped']['Row']

        # Classify request status if not already done
        # 若尚未分類請求狀態，進行分類 (Hit/Miss/Conflict)
        if 'status' not in req:
            # print(f"Classifying Req {req['address']:x} Bank {bank.id} Row {row}. Open: {bank.is_open}, OpenRow: {bank.open_row}")
            if bank.is_open:
                if bank.open_row == row:
                    req['status'] = 'HIT'
                    self.stats['page_hits'] += 1
                else:
                    req['status'] = 'CONFLICT'
                    self.stats['page_conflicts'] += 1
            else:
                req['status'] = 'MISS'
                self.stats['page_misses'] += 1

        self.cmd_bus_free_time = self.current_time + 1

        if cmd_type == 'PRE':
            bank.last_pre = self.current_time
            bank.is_open = False
            bank.open_row = None
            return False

        elif cmd_type == 'ACT':
            bank.last_act = self.current_time
            bank.is_open = True
            bank.open_row = row

            # Track ACT for global constraints per Rank
            # 追蹤 ACT 以檢查 Rank 層級的全域限制
            rank_key = (req['mapped'].get('Channel', 0), req['mapped'].get('Rank', 0))
            if rank_key not in self.act_history:
                self.act_history[rank_key] = []

            history = self.act_history[rank_key]
            history.append(self.current_time)
            if len(history) > 4:
                history.pop(0)

            return False

        elif cmd_type in ['RD', 'WR']:
            if cmd_type == 'WR':
                bank.last_write = self.current_time
                latency = self.config['tCWL']
            else:
                bank.last_read = self.current_time
                latency = self.config['tCL']

            duration = req['burst_count'] * self.burst_cycles
            data_start = self.current_time + latency
            self.data_bus_free_time = data_start + duration

            self.stats['bus_busy_cycles'] += duration
            self.stats['total_bytes'] += req['size']

            return True

    def tick(self):
        """
        Advances the simulation by one step (or more if skipping).
        推進模擬一步 (若使用時間跳躍則可能更多)。
        """
        # Track queue depth statistics
        # 追蹤隊列深度統計
        self.stats['cumulative_queue_depth'] += len(self.queue)
        self.stats['queue_depth_samples'] += 1

        if self.current_time < self.cmd_bus_free_time:
            self.current_time = self.cmd_bus_free_time
            # Don't return, check if we can do something now?
            # If cmd bus busy, we can't issue.
            # But we just updated current_time.
            # Loop again? No, tick is one step.
            return

        candidates = []
        min_next_time = float('inf')

        for i, req in enumerate(self.queue):
            ready, cmd, next_ts = self.get_command_status(req)
            if ready:
                candidates.append((i, cmd))
            else:
                if next_ts < min_next_time:
                    min_next_time = next_ts

        if not candidates:
            # Time Skipping Logic
            # 時間跳躍邏輯
            if min_next_time != float('inf') and min_next_time > self.current_time:
                self.current_time = min_next_time
            else:
                self.current_time += 1
            return

        selected_idx = -1
        selected_cmd = None

        if self.scheduler_type == 'FIFO':
            selected_idx, selected_cmd = candidates[0]

        elif self.scheduler_type == 'PageHitFirst':
            hit_candidate = None
            for idx, cmd in candidates:
                if cmd in ['RD', 'WR']:
                    hit_candidate = (idx, cmd)
                    break

            if hit_candidate:
                selected_idx, selected_cmd = hit_candidate
            else:
                selected_idx, selected_cmd = candidates[0]
        else:
            selected_idx, selected_cmd = candidates[0]

        done = self.issue_command(selected_idx, selected_cmd)

        if done:
            self.queue.pop(selected_idx)
            self.completed_requests += 1

        self.current_time += 1
