# DRAM Simulator Benchmark Results

## Simulation Results (LPDDR4 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 17721 | 12.71 | 99.32 | 15.93 | 1 | 32 | 517 |
| rand_read_256B.trace | 35320 | 12.76 | 99.66 | 15.93 | 0 | 32 | 518 |
| rand_read_512B.trace | 70520 | 12.78 | 99.83 | 15.91 | 0 | 32 | 518 |
| rand_read_64B.trace | 9118 | 12.35 | 96.51 | 15.86 | 0 | 32 | 518 |
| rand_write_128B.trace | 17748 | 12.69 | 99.17 | 15.90 | 0 | 32 | 518 |
| rand_write_256B.trace | 35439 | 12.71 | 99.33 | 15.87 | 0 | 32 | 518 |
| rand_write_512B.trace | 70519 | 12.78 | 99.83 | 15.89 | 0 | 32 | 518 |
| rand_write_64B.trace | 9562 | 11.78 | 92.03 | 15.84 | 0 | 32 | 518 |
| seq_read_128B.trace | 17720 | 12.71 | 99.32 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 35320 | 12.76 | 99.66 | 15.79 | 530 | 20 | 0 |
| seq_read_512B.trace | 70520 | 12.78 | 99.83 | 15.79 | 514 | 32 | 4 |
| seq_read_64B.trace | 8920 | 12.63 | 98.65 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 17716 | 12.72 | 99.35 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 35316 | 12.76 | 99.67 | 15.79 | 530 | 20 | 0 |
| seq_write_512B.trace | 70516 | 12.78 | 99.84 | 15.79 | 514 | 32 | 4 |
| seq_write_64B.trace | 8916 | 12.63 | 98.70 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9001 | 25.03 | 97.77 | 15.90 | 1 | 32 | 517 |
| rand_read_256B.trace | 17720 | 25.43 | 99.32 | 15.90 | 0 | 32 | 518 |
| rand_read_512B.trace | 35368 | 25.48 | 99.52 | 15.90 | 0 | 32 | 518 |
| rand_read_64B.trace | 7927 | 14.21 | 55.51 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 9328 | 24.15 | 94.34 | 15.86 | 0 | 32 | 518 |
| rand_write_256B.trace | 17806 | 25.30 | 98.84 | 15.86 | 0 | 32 | 518 |
| rand_write_512B.trace | 35500 | 25.38 | 99.15 | 15.87 | 0 | 32 | 518 |
| rand_write_64B.trace | 8380 | 13.44 | 52.51 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 8920 | 25.26 | 98.65 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 17720 | 25.43 | 99.32 | 15.79 | 530 | 20 | 0 |
| seq_read_512B.trace | 35320 | 25.51 | 99.66 | 15.79 | 514 | 32 | 4 |
| seq_read_64B.trace | 4573 | 24.63 | 96.22 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8916 | 25.27 | 98.70 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 17716 | 25.43 | 99.35 | 15.79 | 530 | 20 | 0 |
| seq_write_512B.trace | 35316 | 25.52 | 99.67 | 15.79 | 514 | 32 | 4 |
| seq_write_64B.trace | 4569 | 24.65 | 96.30 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7653 | 29.44 | 57.49 | 15.85 | 1 | 32 | 517 |
| rand_read_256B.trace | 9419 | 47.84 | 93.43 | 15.85 | 0 | 32 | 518 |
| rand_read_512B.trace | 17801 | 50.62 | 98.87 | 15.88 | 0 | 32 | 518 |
| rand_read_64B.trace | 7927 | 14.21 | 55.51 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8079 | 27.88 | 54.46 | 15.83 | 0 | 32 | 518 |
| rand_write_256B.trace | 9417 | 47.85 | 93.45 | 15.82 | 0 | 32 | 518 |
| rand_write_512B.trace | 17806 | 50.61 | 98.84 | 15.86 | 0 | 32 | 518 |
| rand_write_64B.trace | 8380 | 13.44 | 52.51 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 4560 | 49.40 | 96.49 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 8920 | 50.51 | 98.65 | 15.79 | 530 | 20 | 0 |
| seq_read_512B.trace | 17720 | 50.85 | 99.32 | 15.79 | 514 | 32 | 4 |
| seq_read_64B.trace | 4573 | 24.63 | 96.22 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 4556 | 49.45 | 96.58 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 8916 | 50.53 | 98.70 | 15.79 | 530 | 20 | 0 |
| seq_write_512B.trace | 17716 | 50.86 | 99.35 | 15.79 | 514 | 32 | 4 |
| seq_write_64B.trace | 4569 | 24.65 | 96.30 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 17721 | 12.71 | 99.32 | 15.93 | 1 | 32 | 517 |
| rand_read_256B.trace | 35320 | 12.76 | 99.66 | 15.93 | 0 | 32 | 518 |
| rand_read_512B.trace | 70520 | 12.78 | 99.83 | 15.91 | 0 | 32 | 518 |
| rand_read_64B.trace | 9118 | 12.35 | 96.51 | 15.86 | 0 | 32 | 518 |
| rand_write_128B.trace | 17748 | 12.69 | 99.17 | 15.90 | 0 | 32 | 518 |
| rand_write_256B.trace | 35439 | 12.71 | 99.33 | 15.87 | 0 | 32 | 518 |
| rand_write_512B.trace | 70519 | 12.78 | 99.83 | 15.89 | 0 | 32 | 518 |
| rand_write_64B.trace | 9562 | 11.78 | 92.03 | 15.84 | 0 | 32 | 518 |
| seq_read_128B.trace | 17720 | 12.71 | 99.32 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 35320 | 12.76 | 99.66 | 15.79 | 530 | 20 | 0 |
| seq_read_512B.trace | 70520 | 12.78 | 99.83 | 15.79 | 514 | 32 | 4 |
| seq_read_64B.trace | 8920 | 12.63 | 98.65 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 17716 | 12.72 | 99.35 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 35316 | 12.76 | 99.67 | 15.79 | 530 | 20 | 0 |
| seq_write_512B.trace | 70516 | 12.78 | 99.84 | 15.79 | 514 | 32 | 4 |
| seq_write_64B.trace | 8916 | 12.63 | 98.70 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9001 | 25.03 | 97.77 | 15.90 | 1 | 32 | 517 |
| rand_read_256B.trace | 17720 | 25.43 | 99.32 | 15.90 | 0 | 32 | 518 |
| rand_read_512B.trace | 35368 | 25.48 | 99.52 | 15.90 | 0 | 32 | 518 |
| rand_read_64B.trace | 7927 | 14.21 | 55.51 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 9328 | 24.15 | 94.34 | 15.86 | 0 | 32 | 518 |
| rand_write_256B.trace | 17806 | 25.30 | 98.84 | 15.86 | 0 | 32 | 518 |
| rand_write_512B.trace | 35500 | 25.38 | 99.15 | 15.87 | 0 | 32 | 518 |
| rand_write_64B.trace | 8380 | 13.44 | 52.51 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 8920 | 25.26 | 98.65 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 17720 | 25.43 | 99.32 | 15.79 | 530 | 20 | 0 |
| seq_read_512B.trace | 35320 | 25.51 | 99.66 | 15.79 | 514 | 32 | 4 |
| seq_read_64B.trace | 4573 | 24.63 | 96.22 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8916 | 25.27 | 98.70 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 17716 | 25.43 | 99.35 | 15.79 | 530 | 20 | 0 |
| seq_write_512B.trace | 35316 | 25.52 | 99.67 | 15.79 | 514 | 32 | 4 |
| seq_write_64B.trace | 4569 | 24.65 | 96.30 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7653 | 29.44 | 57.49 | 15.85 | 1 | 32 | 517 |
| rand_read_256B.trace | 9419 | 47.84 | 93.43 | 15.85 | 0 | 32 | 518 |
| rand_read_512B.trace | 17801 | 50.62 | 98.87 | 15.88 | 0 | 32 | 518 |
| rand_read_64B.trace | 7927 | 14.21 | 55.51 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8079 | 27.88 | 54.46 | 15.83 | 0 | 32 | 518 |
| rand_write_256B.trace | 9417 | 47.85 | 93.45 | 15.82 | 0 | 32 | 518 |
| rand_write_512B.trace | 17806 | 50.61 | 98.84 | 15.86 | 0 | 32 | 518 |
| rand_write_64B.trace | 8380 | 13.44 | 52.51 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 4560 | 49.40 | 96.49 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 8920 | 50.51 | 98.65 | 15.79 | 530 | 20 | 0 |
| seq_read_512B.trace | 17720 | 50.85 | 99.32 | 15.79 | 514 | 32 | 4 |
| seq_read_64B.trace | 4573 | 24.63 | 96.22 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 4556 | 49.45 | 96.58 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 8916 | 50.53 | 98.70 | 15.79 | 530 | 20 | 0 |
| seq_write_512B.trace | 17716 | 50.86 | 99.35 | 15.79 | 514 | 32 | 4 |
| seq_write_64B.trace | 4569 | 24.65 | 96.30 | 15.78 | 543 | 7 | 0 |
