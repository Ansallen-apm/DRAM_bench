import argparse
import sys
import os

# Add src to path if needed, or assume running from root
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from config import load_config, load_mapping
from mapper import AddressMapper
from dram_sim import DRAMController
import multiprocessing

class TraceReader:
    """
    Reads and parses trace files.
    讀取並解析 Trace 檔案。
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration

        parts = line.strip().split()
        if not parts:
            return self.__next__()

        # Format: [R/W]x [Address] [Bus_Width_Log2] [Burst_Length_Code]
        # 格式：[R/W]x [Address] [Bus_Width_Log2] [Burst_Length_Code]
        # Data Size = (2^Bus_Width_Log2) * (Burst_Length_Code + 1)

        type_str = parts[0]
        addr_str = parts[1]
        bus_width_log2 = int(parts[2])
        burst_len_code = int(parts[3], 16)

        is_write = 'W' in type_str
        address = int(addr_str, 16)

        # Calculate Request Size
        # 計算請求大小
        beats = burst_len_code + 1
        bytes_per_beat = 2**bus_width_log2
        size = bytes_per_beat * beats

        # We pass 'size' to controller. 'burst_count' is no longer direct input for DRAM duration.

        return {
            'is_write': is_write,
            'address': address,
            'size': size,
            'beats': beats # Optional, for debug
        }

import os

def run_channel_sim(channel_id, trace_filepath, config, mapping, policy, queue_depth, interval_us, verbose_interval, trace_name, log_dir):
    """
    Simulates a single Channel independently by streaming the trace file.
    This avoids loading the entire trace into memory, preventing OOM on huge files.
    """
    mapper = AddressMapper(mapping)
    controller = DRAMController(config, mapper, scheduler_type=policy, queue_depth=queue_depth)

    trace_reader = TraceReader(trace_filepath)
    trace_iter = iter(trace_reader)

    interval_log_file = None
    interval_cycles = None
    next_interval_cycle = None
    last_bus_busy_cycles = 0
    interval_count = 1

    if interval_us is not None:
        freq_mhz = config['ClockFrequencyMHz']
        cycle_time_ns = 1000.0 / freq_mhz
        interval_ns = interval_us * 1000.0
        interval_cycles = interval_ns / cycle_time_ns
        next_interval_cycle = interval_cycles

        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
            log_filename = os.path.join(log_dir, f'interval_{trace_name}_CH{channel_id}.log')
        else:
            log_filename = f'interval_{trace_name}_CH{channel_id}.log'

        interval_log_file = open(log_filename, 'w')
        if verbose_interval:
            print(f"[CH{channel_id}] Interval Logging Enabled: {interval_us} us (approx {int(interval_cycles)} cycles)")
        interval_log_file.write(f"Interval Logging Enabled: {interval_us} us\n")
        interval_log_file.write(f"Interval (us), Utilization (%)\n")

    next_req = None
    eof_reached = False

    while not eof_reached or len(controller.queue) > 0:
        # Fill Queue up to depth
        while not eof_reached and len(controller.queue) < queue_depth:
            if next_req is None:
                next_req = next(trace_iter, None)
                if next_req is None:
                    eof_reached = True
                    break

            # Process map address to see if it belongs to this worker's channel
            mapped = mapper.map_address(next_req['address'])
            req_ch = mapped.get('Channel', 0)

            if req_ch == channel_id:
                next_req['mapped'] = mapped
                controller.queue.append(next_req)
                next_req = None # Consume it
            else:
                next_req = None # Discard it, belongs to another channel

        # Tick even if queue might not be fully populated yet
        # (or if we hit EOF and just need to drain)
        controller.tick()

        # Interval utilization logging
        if interval_cycles is not None and controller.current_time >= next_interval_cycle:
            current_bus_busy_cycles = controller.stats['bus_busy_cycles']
            interval_busy = current_bus_busy_cycles - last_bus_busy_cycles

            # Since this controller is ONLY processing ONE channel:
            interval_total_available = interval_cycles * 1

            interval_utilization = (interval_busy / interval_total_available) * 100 if interval_total_available > 0 else 0
            interval_time_us = interval_us * interval_count
            # 強制轉換為整數並加入千分位逗號，避免科學記號
            formatted_time = f"{int(interval_time_us):,}"

            if verbose_interval:
                msg = f"[CH{channel_id}] Interval {formatted_time} us: Utilization = {interval_utilization:.2f} %"
                print(msg)
            interval_log_file.write(f"{formatted_time}, {interval_utilization:.2f}\n")

            last_bus_busy_cycles = current_bus_busy_cycles
            interval_count += 1
            next_interval_cycle += interval_cycles

    if interval_log_file is not None:
        interval_log_file.close()

    # Calculate final stats for this specific channel
    stats = controller.stats
    max_data_bus_free_time = 0
    if controller.data_bus_free_time:
        max_data_bus_free_time = max(controller.data_bus_free_time.values())

    total_cycles = max(controller.current_time, max_data_bus_free_time)
    total_cycles = max(1, total_cycles)

    return {
        'channel_id': channel_id,
        'total_cycles': total_cycles,
        'stats': stats
    }


def main():
    parser = argparse.ArgumentParser(description='Simple DRAM Simulator')
    parser.add_argument('--config', required=True, help='Path to timing config JSON (時序設定檔路徑)')
    parser.add_argument('--mapping', required=True, help='Path to address mapping JSON (位址映射檔路徑)')
    parser.add_argument('--trace', required=True, help='Path to trace file (Trace 檔案路徑)')
    parser.add_argument('--policy', default='PageHitFirst', choices=['FIFO', 'PageHitFirst'], help='Scheduling policy (排程策略)')
    parser.add_argument('--queue_depth', type=int, default=16, help='Command queue depth (指令隊列深度)')
    parser.add_argument('--interval_us', type=float, default=None, help='Interval in microseconds for calculating utilization (計算利用率的時間區間，單位為 us)')
    parser.add_argument('--verbose_interval', action='store_true', help='Print interval utilization to console with [CHx] tag (在終端機印出帶有 [CHx] 標籤的區間利用率)')
    parser.add_argument('--log_dir', type=str, default='.', help='Directory to save the interval log files (存放 interval log 檔案的資料夾)')

    args = parser.parse_args()

    # Load Configs
    # 載入設定
    try:
        config = load_config(args.config)
        mapping = load_mapping(args.mapping)
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return

    # Initialize Components
    # 初始化元件
    mapper = AddressMapper(mapping)
    controller = DRAMController(config, mapper, scheduler_type=args.policy, queue_depth=args.queue_depth)

    # Fast Pre-scan to discover active channels in the trace
    # 快速掃描找出 Trace 到底用到了哪些 Channel，避免啟動不需要的 Worker
    active_channels = set()
    mapper = AddressMapper(mapping)

    with open(args.trace, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            addr_str = parts[1]
            address = int(addr_str, 16)
            mapped = mapper.map_address(address)
            active_channels.add(mapped.get('Channel', 0))
            # Optional: early exit if we found maximum possible channels
            # (e.g. if we know it's a 4CH mapping, break when len == 4)

    print(f"Starting parallel simulation with {args.config} and {args.mapping}")
    print(f"Policy: {args.policy}, Queue Depth: {args.queue_depth}")
    print(f"Detected {len(active_channels)} active channel(s) in trace: {active_channels}")

    # Multiprocessing Pool Setup
    trace_base_name = os.path.splitext(os.path.basename(args.trace))[0]

    pool_args = []
    for ch_id in active_channels:
        pool_args.append((
            ch_id, args.trace, config, mapping, args.policy, args.queue_depth, args.interval_us, args.verbose_interval, trace_base_name, args.log_dir
        ))

    # Determine optimal number of processes
    num_processes = min(len(active_channels), multiprocessing.cpu_count())

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(run_channel_sim, pool_args)

    # ------------------------------------------------------------------------
    # Aggregate and Print Results
    # 彙整與印出結果
    # ------------------------------------------------------------------------

    freq_mhz = config['ClockFrequencyMHz']
    cycle_time_ns = 1000.0 / freq_mhz

    total_bus_busy_cycles = 0
    total_bytes = 0
    overall_max_cycles = 0

    total_page_hits = 0
    total_page_misses = 0
    total_page_conflicts = 0

    print("\n--- Per-Channel Statistics (個別通道統計) ---")
    for res in sorted(results, key=lambda x: x['channel_id']):
        ch_id = res['channel_id']
        ch_cycles = res['total_cycles']
        ch_stats = res['stats']

        # Individual Channel Math
        ch_time_ns = ch_cycles * cycle_time_ns
        ch_time_sec = ch_time_ns / 1e9
        ch_bw_gbs = (ch_stats['total_bytes'] / 1e9) / ch_time_sec if ch_time_sec > 0 else 0
        ch_utilization = (ch_stats['bus_busy_cycles'] / ch_cycles) * 100 if ch_cycles > 0 else 0
        ch_avg_qd = ch_stats['cumulative_queue_depth'] / ch_stats['queue_depth_samples'] if ch_stats['queue_depth_samples'] > 0 else 0

        print(f"\n[Channel {ch_id}]")
        print(f"  Total Cycles: {ch_cycles}")
        print(f"  Total Bytes: {ch_stats['total_bytes']}")
        print(f"  Bandwidth: {ch_bw_gbs:.2f} GB/s")
        print(f"  Utilization: {ch_utilization:.2f} %")
        print(f"  Avg Queue Depth: {ch_avg_qd:.2f}")

        # Aggregation for Overall
        overall_max_cycles = max(overall_max_cycles, ch_cycles)
        total_bus_busy_cycles += ch_stats['bus_busy_cycles']
        total_bytes += ch_stats['total_bytes']
        total_page_hits += ch_stats['page_hits']
        total_page_misses += ch_stats['page_misses']
        total_page_conflicts += ch_stats['page_conflicts']

    overall_max_cycles = max(1, overall_max_cycles)
    num_active_channels = len(results)

    # Overall Math
    total_time_ns = overall_max_cycles * cycle_time_ns
    total_time_sec = total_time_ns / 1e9

    overall_bw_gbs = (total_bytes / 1e9) / total_time_sec if total_time_sec > 0 else 0

    # Overall utilization denominator is MAX_CYCLES * NUM_CHANNELS
    total_available_cycles = overall_max_cycles * num_active_channels
    overall_utilization = (total_bus_busy_cycles / total_available_cycles) * 100 if total_available_cycles > 0 else 0

    print("\n=============================================")
    print("Overall Simulation Results (整體模擬結果):")
    print("=============================================")
    print(f"Total Cycles (總週期): {overall_max_cycles}")
    print(f"Total Bytes (總位元組): {total_bytes}")
    print(f"Bandwidth (頻寬): {overall_bw_gbs:.2f} GB/s")
    print(f"Utilization (利用率): {overall_utilization:.2f} %")
    print("-" * 30)
    print(f"Page Hits (Page 命中): {total_page_hits}")
    print(f"Page Misses (Page 未命中): {total_page_misses}")
    print(f"Page Conflicts (Page 衝突): {total_page_conflicts}")

if __name__ == "__main__":
    main()
