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
python3 src/main.py --config <config_file> --mapping <mapping_file> --trace <trace_file> --policy <FIFO|PageHitFirst>
```

### Example (範例)

```bash
python3 src/main.py --config configs/LP4_cfg.json --mapping configs/mapping.json --trace traces/sample.trace --policy FIFO
```

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
    "tCL": 28,
    "tCWL": 26,
    "tRAS": 67,
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

### Trace Format (Trace 格式)
Each line represents a memory request:
<!-- 每一行代表一個記憶體請求： -->
`[R/W] [Address] [Size_Power_of_2] [Burst_Code]`

- `ARx 0000000126B52000 6 00`: Read 64B ($2^6$), 1 Burst.
- `AWx 0000000126B52000 6 01`: Write 64B, 2 Bursts.

## Output (輸出)
The simulator outputs performance statistics:
<!-- 模擬器輸出效能統計數據： -->

- **Total Cycles**: Execution time in clock cycles.
  <!-- 總執行週期。 -->
- **Bandwidth**: Effective data transfer rate (GB/s).
  <!-- 有效資料傳輸率 (GB/s)。 -->
- **Utilization**: Percentage of time data bus was busy.
  <!-- 資料匯流排忙碌時間百分比。 -->
- **Page Stats**: Hits, Misses, Conflicts count.
  <!-- Page 狀態統計：Hits, Misses, Conflicts 次數。 -->
