# DRAM Simulator

A Python-based DRAM Simulator modeling LPDDR4/5 timing, address mapping, and scheduling policies.
<!--
DRAM 模擬器
基於 Python 實作的 DRAM 模擬器，支援 LPDDR4/5 時序、位址映射以及排程策略。
-->

## Features (功能)
- **Timing Support**: Configurable LPDDR4/LPDDR5 timings (tRP, tRCD, tCL, tCWL, tRAS, tRRD, tFAW, etc.).
  <!-- 支援可配置的 LPDDR4/LPDDR5 時序參數。 -->
- **Address Mapping**: Flexible bit-masking for Channel, Rank, Bank, Row, Column mapping.
  <!-- 彈性的位址映射設定，支援 Channel, Rank, Bank, Row, Column 的位元遮罩。 -->
- **Scheduling Policies**: Supports FIFO and Page-Hit First (Open-Page Policy).
  <!-- 支援 FIFO 與 Page-Hit First (Open-Page Policy) 排程策略。 -->
- **State Tracking**: Models Bank states (Open/Closed/Conflict) and Bus Contention.
  <!-- 追蹤 Bank 狀態 (Open/Closed/Conflict) 與匯流排競爭 (Bus Contention)。 -->

## Usage (使用方式)

Run the simulator using `src/main.py`:
<!-- 使用 src/main.py 執行模擬器： -->

```bash
python3 src/main.py --config <config_file> --mapping <mapping_file> --trace <trace_file> --policy <FIFO|PageHitFirst> --queue_depth <1-1024>
```

### Arguments (參數)
- `--config`: Path to timing config JSON (e.g., `configs/LP4_cfg.json`).
- `--mapping`: Path to address mapping JSON (e.g., `configs/mapping.json`).
- `--trace`: Path to trace file (e.g., `traces/sample.trace`).
- `--policy`: Scheduling policy (`FIFO` or `PageHitFirst`).
- `--queue_depth`: Command Queue Depth (Integer, Range: 1-1024). Default is 16.
  <!-- 指令隊列深度 (整數，範圍：1-1024)。預設為 16。 -->

### Example (範例)

```bash
python3 src/main.py --config configs/LP4_cfg.json --mapping configs/mapping.json --trace traces/sample.trace --policy FIFO --queue_depth 32
```

## Trace Files (Trace 檔案)

The repository includes several generated trace files for testing different access patterns and data sizes (100 transactions each):
<!-- 專案包含多個生成的 Trace 檔案，用於測試不同的存取模式與資料大小 (每個檔案包含 100 筆交易)： -->

Located in `traces/`:
- **Sequential Access (循序存取)**:
    - `seq_read_128B.trace`, `seq_read_256B.trace`, `seq_read_512B.trace`
    - `seq_write_128B.trace`, `seq_write_256B.trace`, `seq_write_512B.trace`
- **Random Access (隨機存取)**:
    - `rand_read_128B.trace`, `rand_read_256B.trace`, `rand_read_512B.trace`
    - `rand_write_128B.trace`, `rand_write_256B.trace`, `rand_write_512B.trace`

### Trace Format (Trace 格式)
Each line represents a memory request:
<!-- 每一行代表一個記憶體請求： -->
`[R/W] [Address] [Size_Power_of_2] [Burst_Code]`

- `ARx 0000000126B52000 6 00`: Read 64B ($2^6$), 1 Burst.
- `AWx 0000000126B52000 6 01`: Write 64B, 2 Bursts.

## Configuration (設定)

### Timing Config (`configs/LP4_cfg.json`)
Defines timing parameters and clock frequency.
<!-- 定義時序參數與時脈頻率。 -->

```json
{
    "ClockFrequencyMHz": 1600,
    "BurstLength": 16,
    "tRP": 29,
    "tRCD": 29,
    ...
}
```

### Address Mapping (`configs/mapping.json`)
Defines which bits of the physical address correspond to DRAM hierarchy levels. Format: `[[MSB, LSB], ...]`
<!-- 定義實體位址的哪些位元對應到 DRAM 階層。格式：`[[MSB, LSB], ...]` -->

```json
{
    "Channel": [[33, 33]],
    "Rank": [[32, 31]],
    "Bank": [[16, 14], [5, 4]],
    "Row": [[30, 17]],
    "Column": [[13, 3]]
}
```

## Output (輸出)
The simulator outputs performance statistics:
<!-- 模擬器輸出效能統計數據： -->

- **Total Cycles**: Execution time in clock cycles.
  <!-- 總執行週期。 -->
- **Bandwidth**: Effective data transfer rate (GB/s).
  <!-- 有效資料傳輸率 (GB/s)。 -->
- **Utilization**: Percentage of time data bus was busy.
  <!-- 資料匯流排忙碌時間百分比。 -->
- **Average Queue Depth**: Average number of requests in the command queue.
  <!-- 平均隊列深度：指令隊列中的平均請求數量。 -->
- **Page Stats**: Hits, Misses, Conflicts count.
  <!-- Page 狀態統計：Hits, Misses, Conflicts 次數。 -->
