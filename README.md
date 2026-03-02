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

### Quick Run (快速執行)
Use the provided script to run a default simulation:
<!-- 使用提供的腳本執行預設模擬： -->

```bash
./run_sim.sh
```

### Benchmark (效能測試)
Run the benchmark script to simulate multiple traces with different configurations (LPDDR4/LPDDR5):
<!-- 執行效能測試腳本以使用不同配置 (LPDDR4/LPDDR5) 模擬多個 Trace 檔案： -->

```bash
python3 run_benchmark.py
```

The results will be printed to the console and saved in [BENCHMARK_RESULTS.md](BENCHMARK_RESULTS.md).
<!-- 結果將顯示在控制台並儲存於 BENCHMARK_RESULTS.md。 -->

### Arguments (參數)
- `--config`: Path to timing config JSON (e.g., `configs/LP4_32_cfg.json`).
- `--mapping`: Path to address mapping JSON (e.g., `configs/mapping_2ch.json`).
- `--trace`: Path to trace file (e.g., `traces/sample.trace`).
- `--policy`: Scheduling policy (`FIFO` or `PageHitFirst`).
- `--queue_depth`: Command Queue Depth (Integer, Range: 1-1024). Default is 16.
  <!-- 指令隊列深度 (整數，範圍：1-1024)。預設為 16。 -->

### Example (範例)

```bash
python3 src/main.py --config configs/LP4_32_cfg.json --mapping configs/mapping_2ch.json --trace traces/basic100/seq_read_128B.trace --policy FIFO --queue_depth 32
```

## Trace Files (Trace 檔案)

The repository includes several generated trace files for testing different access patterns and data sizes:
<!-- 專案包含多個生成的 Trace 檔案，用於測試不同的存取模式與資料大小： -->

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

### Timing Config (`configs/LP4_32_cfg.json`)
Defines timing parameters, clock frequency, and data bus width (BitWidth).
We provide configurations for LPDDR4 and LPDDR5 with different BitWidths (16-bit, 32-bit, 64-bit).
<!-- 定義時序參數、時脈頻率與資料匯流排寬度 (BitWidth)。我們提供 LPDDR4 與 LPDDR5 的不同 BitWidth (16-bit, 32-bit, 64-bit) 設定檔。 -->

Available config files (可用的設定檔):
- `configs/LP4_16_cfg.json`
- `configs/LP4_32_cfg.json`
- `configs/LP4_64_cfg.json`
- `configs/LP5_16_cfg.json`
- `configs/LP5_32_cfg.json`
- `configs/LP5_64_cfg.json`

```json
{
    "ClockFrequencyMHz": 3200,
    "Prefetch": 16,
    "BitWidth": 32,
    "tRP": 60,
    "tRCD": 60,
    ...
}
```

### Address Mapping (`configs/mapping_*.json`)
Defines which bits of the physical address correspond to DRAM hierarchy levels. Format: `[[MSB, LSB], ...]`
We provide single-channel (`mapping_1ch.json`) and dual-channel (`mapping_2ch.json`) mapping examples.
<!-- 定義實體位址的哪些位元對應到 DRAM 階層。格式：`[[MSB, LSB], ...]` 我們提供單通道與雙通道的映射範例。 -->

```json
{
    "Channel": [[10, 10]],
    "Rank": [[11, 11]],
    "Bank": [[17, 15]],
    "Row": [[30, 18]],
    "Column": [[9, 4], [14, 12]]
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
