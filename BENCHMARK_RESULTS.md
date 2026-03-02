# DRAM Simulator Benchmark Results

## Simulation Results (LPDDR4 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 17657 | 6.38 | 99.68 | 15.94 | 1 | 32 | 517 |
| rand_read_64B.trace | 8857 | 6.36 | 99.36 | 15.89 | 0 | 32 | 518 |
| rand_write_128B.trace | 17655 | 6.38 | 99.69 | 15.92 | 0 | 32 | 518 |
| rand_write_64B.trace | 8859 | 6.36 | 99.33 | 15.91 | 0 | 32 | 518 |
| seq_read_128B.trace | 17657 | 6.38 | 99.68 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 8857 | 6.36 | 99.36 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 17655 | 6.38 | 99.69 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 8855 | 6.36 | 99.38 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 8859 | 12.71 | 99.33 | 15.92 | 1 | 32 | 517 |
| rand_read_64B.trace | 4594 | 12.26 | 95.78 | 15.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 8885 | 12.68 | 99.04 | 15.89 | 0 | 32 | 518 |
| rand_write_64B.trace | 4726 | 11.92 | 93.10 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 8857 | 12.72 | 99.36 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 4457 | 12.64 | 98.72 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8855 | 12.72 | 99.38 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 4455 | 12.64 | 98.77 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 4502 | 25.02 | 97.73 | 15.88 | 1 | 32 | 517 |
| rand_read_64B.trace | 4594 | 12.26 | 95.78 | 15.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 4640 | 24.28 | 94.83 | 15.85 | 0 | 32 | 518 |
| rand_write_64B.trace | 4726 | 11.92 | 93.10 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 4457 | 25.27 | 98.72 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 4457 | 12.64 | 98.72 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 4455 | 25.28 | 98.77 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 4455 | 12.64 | 98.77 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 17721 | 12.71 | 99.32 | 15.93 | 1 | 32 | 517 |
| rand_read_64B.trace | 9118 | 12.35 | 96.51 | 15.86 | 0 | 32 | 518 |
| rand_write_128B.trace | 17791 | 12.66 | 98.93 | 15.90 | 0 | 32 | 518 |
| rand_write_64B.trace | 9708 | 11.60 | 90.65 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 17720 | 12.71 | 99.32 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 8920 | 12.63 | 98.65 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 17716 | 12.72 | 99.35 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 8916 | 12.63 | 98.70 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9001 | 25.03 | 97.77 | 15.90 | 1 | 32 | 517 |
| rand_read_64B.trace | 9118 | 12.35 | 96.51 | 15.86 | 0 | 32 | 518 |
| rand_write_128B.trace | 9378 | 24.02 | 93.84 | 15.87 | 0 | 32 | 518 |
| rand_write_64B.trace | 9708 | 11.60 | 90.65 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 8920 | 25.26 | 98.65 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 8920 | 12.63 | 98.65 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8916 | 25.27 | 98.70 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 8916 | 12.63 | 98.70 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9001 | 25.03 | 97.77 | 15.90 | 1 | 32 | 517 |
| rand_read_64B.trace | 9118 | 12.35 | 96.51 | 15.86 | 0 | 32 | 518 |
| rand_write_128B.trace | 9378 | 24.02 | 93.84 | 15.87 | 0 | 32 | 518 |
| rand_write_64B.trace | 9708 | 11.60 | 90.65 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 8920 | 25.26 | 98.65 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 8920 | 12.63 | 98.65 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8916 | 25.27 | 98.70 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 8916 | 12.63 | 98.70 | 15.78 | 543 | 7 | 0 |
