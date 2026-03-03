# DRAM Simulator Performance Limit Results (20k Transactions)
此測試使用 `traces/perf_limit/` 目錄下的 20,000 筆交易 trace 進行壓力測試，並使用雙通道 (`mapping_2ch.json`) 架構。


## Simulation Results (LPDDR4-6400 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 349197 | 23.46 | 91.64 | 16.00 | 5 | 33 | 19962 |
| rand_read_256B.trace | 663216 | 24.70 | 96.50 | 16.00 | 1 | 33 | 19966 |
| rand_write_128B.trace | 363425 | 22.54 | 88.05 | 16.00 | 3 | 32 | 19965 |
| rand_write_256B.trace | 663293 | 24.70 | 96.49 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 320120 | 25.59 | 99.96 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 640120 | 25.60 | 99.98 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 320116 | 25.59 | 99.96 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 640116 | 25.60 | 99.98 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR4-6400 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 266809 | 30.70 | 59.97 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 346688 | 47.26 | 92.30 | 16.00 | 2 | 32 | 19966 |
| rand_write_128B.trace | 307389 | 26.65 | 52.05 | 16.00 | 4 | 32 | 19964 |
| rand_write_256B.trace | 364175 | 44.99 | 87.87 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 162827 | 50.31 | 98.26 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320120 | 51.18 | 99.96 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 162823 | 50.31 | 98.27 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320116 | 51.18 | 99.96 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR4-6400 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 264501 | 30.97 | 30.25 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 267990 | 61.14 | 59.70 | 15.99 | 2 | 32 | 19966 |
| rand_write_128B.trace | 304209 | 26.93 | 26.30 | 15.99 | 4 | 32 | 19964 |
| rand_write_256B.trace | 308898 | 53.04 | 51.80 | 15.99 | 2 | 32 | 19966 |
| seq_read_128B.trace | 93494 | 87.62 | 85.57 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 161477 | 101.46 | 99.09 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 93490 | 87.62 | 85.57 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 161473 | 101.47 | 99.09 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR4-4266 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 192233 | 28.41 | 83.23 | 16.00 | 5 | 33 | 19962 |
| rand_read_256B.trace | 334255 | 32.67 | 95.74 | 16.00 | 1 | 33 | 19966 |
| rand_write_128B.trace | 216223 | 25.25 | 74.00 | 15.99 | 4 | 32 | 19964 |
| rand_write_256B.trace | 336745 | 32.43 | 95.03 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 160114 | 34.10 | 99.93 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320080 | 34.12 | 99.98 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 160112 | 34.10 | 99.93 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320078 | 34.12 | 99.98 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-6400 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 349197 | 23.46 | 91.64 | 16.00 | 5 | 33 | 19962 |
| rand_read_256B.trace | 663216 | 24.70 | 96.50 | 16.00 | 1 | 33 | 19966 |
| rand_write_128B.trace | 363425 | 22.54 | 88.05 | 16.00 | 3 | 32 | 19965 |
| rand_write_256B.trace | 663293 | 24.70 | 96.49 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 320120 | 25.59 | 99.96 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 640120 | 25.60 | 99.98 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 320116 | 25.59 | 99.96 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 640116 | 25.60 | 99.98 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-6400 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 266809 | 30.70 | 59.97 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 346688 | 47.26 | 92.30 | 16.00 | 2 | 32 | 19966 |
| rand_write_128B.trace | 307389 | 26.65 | 52.05 | 16.00 | 4 | 32 | 19964 |
| rand_write_256B.trace | 364175 | 44.99 | 87.87 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 162827 | 50.31 | 98.26 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320120 | 51.18 | 99.96 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 162823 | 50.31 | 98.27 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320116 | 51.18 | 99.96 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-6400 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 264501 | 30.97 | 30.25 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 267990 | 61.14 | 59.70 | 15.99 | 2 | 32 | 19966 |
| rand_write_128B.trace | 304209 | 26.93 | 26.30 | 15.99 | 4 | 32 | 19964 |
| rand_write_256B.trace | 308898 | 53.04 | 51.80 | 15.99 | 2 | 32 | 19966 |
| seq_read_128B.trace | 93494 | 87.62 | 85.57 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 161477 | 101.46 | 99.09 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 93490 | 87.62 | 85.57 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 161473 | 101.47 | 99.09 | 15.99 | 19372 | 32 | 596 |

## Simulation Results (LPDDR5-8533 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 353650 | 30.88 | 45.24 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 382447 | 57.11 | 83.67 | 16.00 | 2 | 32 | 19966 |
| rand_write_128B.trace | 404617 | 26.99 | 39.54 | 16.00 | 4 | 32 | 19964 |
| rand_write_256B.trace | 426414 | 51.22 | 75.04 | 15.99 | 2 | 32 | 19966 |
| seq_read_128B.trace | 170818 | 63.93 | 93.67 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320160 | 68.22 | 99.95 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 170813 | 63.94 | 93.67 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320155 | 68.22 | 99.95 | 15.99 | 19372 | 32 | 596 |
