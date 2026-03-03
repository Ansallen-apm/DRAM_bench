# DRAM Simulator Performance Limit Results (20k Transactions)
此測試使用 `traces/perf_limit/` 目錄下的 20,000 筆交易 trace 進行壓力測試，並使用雙通道 (`mapping_2ch.json`) 架構。


## Simulation Results (LPDDR4-6400 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 321910 | 25.45 | 99.41 | 127.64 | 1 | 37 | 19962 |
| rand_read_256B.trace | 644289 | 25.43 | 99.33 | 127.64 | 0 | 34 | 19966 |
| rand_write_128B.trace | 320892 | 25.53 | 99.72 | 127.70 | 2 | 33 | 19965 |
| rand_write_256B.trace | 643316 | 25.47 | 99.48 | 127.59 | 0 | 34 | 19966 |
| seq_read_128B.trace | 320120 | 25.59 | 99.96 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 640120 | 25.60 | 99.98 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 320116 | 25.59 | 99.96 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 640116 | 25.60 | 99.98 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR4-6400 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 162034 | 50.56 | 98.74 | 127.62 | 6 | 35 | 19959 |
| rand_read_256B.trace | 322652 | 50.78 | 99.18 | 127.61 | 0 | 34 | 19966 |
| rand_write_128B.trace | 179140 | 45.73 | 89.32 | 127.54 | 15 | 32 | 19953 |
| rand_write_256B.trace | 321880 | 50.90 | 99.42 | 127.59 | 0 | 34 | 19966 |
| seq_read_128B.trace | 160120 | 51.16 | 99.93 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320120 | 51.18 | 99.96 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 160116 | 51.16 | 99.93 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320116 | 51.18 | 99.96 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR4-6400 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 142446 | 57.51 | 56.16 | 127.51 | 15 | 32 | 19953 |
| rand_read_256B.trace | 164282 | 99.73 | 97.39 | 127.60 | 2 | 33 | 19965 |
| rand_write_128B.trace | 174436 | 46.96 | 45.86 | 127.52 | 18 | 32 | 19950 |
| rand_write_256B.trace | 177361 | 92.38 | 90.21 | 127.53 | 12 | 32 | 19956 |
| seq_read_128B.trace | 80120 | 102.25 | 99.85 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 160120 | 102.32 | 99.93 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 80116 | 102.25 | 99.86 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 160116 | 102.33 | 99.93 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR4-4266 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 161123 | 33.89 | 99.30 | 127.62 | 1 | 37 | 19962 |
| rand_read_256B.trace | 322302 | 33.88 | 99.29 | 127.61 | 0 | 34 | 19966 |
| rand_write_128B.trace | 161139 | 33.89 | 99.29 | 127.66 | 4 | 32 | 19964 |
| rand_write_256B.trace | 321678 | 33.95 | 99.48 | 127.60 | 0 | 34 | 19966 |
| seq_read_128B.trace | 160080 | 34.11 | 99.95 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320080 | 34.12 | 99.98 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 160078 | 34.11 | 99.95 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320078 | 34.12 | 99.98 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-6400 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 321910 | 25.45 | 99.41 | 127.64 | 1 | 37 | 19962 |
| rand_read_256B.trace | 644289 | 25.43 | 99.33 | 127.64 | 0 | 34 | 19966 |
| rand_write_128B.trace | 320892 | 25.53 | 99.72 | 127.70 | 2 | 33 | 19965 |
| rand_write_256B.trace | 643316 | 25.47 | 99.48 | 127.59 | 0 | 34 | 19966 |
| seq_read_128B.trace | 320120 | 25.59 | 99.96 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 640120 | 25.60 | 99.98 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 320116 | 25.59 | 99.96 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 640116 | 25.60 | 99.98 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-6400 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 162034 | 50.56 | 98.74 | 127.62 | 6 | 35 | 19959 |
| rand_read_256B.trace | 322652 | 50.78 | 99.18 | 127.61 | 0 | 34 | 19966 |
| rand_write_128B.trace | 179140 | 45.73 | 89.32 | 127.54 | 15 | 32 | 19953 |
| rand_write_256B.trace | 321880 | 50.90 | 99.42 | 127.59 | 0 | 34 | 19966 |
| seq_read_128B.trace | 160120 | 51.16 | 99.93 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320120 | 51.18 | 99.96 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 160116 | 51.16 | 99.93 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320116 | 51.18 | 99.96 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-6400 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 142446 | 57.51 | 56.16 | 127.51 | 15 | 32 | 19953 |
| rand_read_256B.trace | 164282 | 99.73 | 97.39 | 127.60 | 2 | 33 | 19965 |
| rand_write_128B.trace | 174436 | 46.96 | 45.86 | 127.52 | 18 | 32 | 19950 |
| rand_write_256B.trace | 177361 | 92.38 | 90.21 | 127.53 | 12 | 32 | 19956 |
| seq_read_128B.trace | 80120 | 102.25 | 99.85 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 160120 | 102.32 | 99.93 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 80116 | 102.25 | 99.86 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 160116 | 102.33 | 99.93 | 127.63 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-8533 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 190264 | 57.40 | 84.09 | 127.54 | 14 | 32 | 19954 |
| rand_read_256B.trace | 323030 | 67.62 | 99.06 | 127.61 | 0 | 34 | 19966 |
| rand_write_128B.trace | 232311 | 47.01 | 68.87 | 127.53 | 18 | 32 | 19950 |
| rand_write_256B.trace | 322836 | 67.66 | 99.12 | 127.63 | 4 | 33 | 19963 |
| seq_read_128B.trace | 160160 | 68.19 | 99.90 | 127.61 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320160 | 68.22 | 99.95 | 127.63 | 19372 | 32 | 596 |
| seq_write_128B.trace | 160155 | 68.19 | 99.90 | 127.61 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320155 | 68.22 | 99.95 | 127.63 | 19372 | 32 | 596 |
