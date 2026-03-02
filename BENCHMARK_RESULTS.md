# DRAM Simulator Benchmark Results

## Simulation Results (LPDDR4 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9822 | 22.94 | 89.59 | 15.89 | 1 | 32 | 517 |
| rand_read_256B.trace | 18133 | 24.85 | 97.06 | 15.85 | 0 | 32 | 518 |
| rand_read_512B.trace | 35825 | 25.15 | 98.26 | 15.93 | 0 | 32 | 518 |
| rand_read_64B.trace | 7995 | 14.09 | 55.03 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 10007 | 22.51 | 87.94 | 15.86 | 0 | 32 | 518 |
| rand_write_256B.trace | 18222 | 24.73 | 96.59 | 15.79 | 0 | 32 | 518 |
| rand_write_512B.trace | 36250 | 24.86 | 97.10 | 15.82 | 0 | 32 | 518 |
| rand_write_64B.trace | 8429 | 13.36 | 52.20 | 15.81 | 0 | 32 | 518 |
| seq_read_128B.trace | 9016 | 24.99 | 97.60 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 17784 | 25.34 | 98.97 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 35448 | 25.42 | 99.30 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 4575 | 24.62 | 96.17 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 9012 | 25.00 | 97.65 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 17780 | 25.34 | 98.99 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 35444 | 25.42 | 99.31 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 4571 | 24.64 | 96.26 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7674 | 29.36 | 57.34 | 15.85 | 1 | 32 | 517 |
| rand_read_256B.trace | 9673 | 46.58 | 90.97 | 15.82 | 0 | 32 | 518 |
| rand_read_512B.trace | 18104 | 49.77 | 97.22 | 15.91 | 0 | 32 | 518 |
| rand_read_64B.trace | 7905 | 14.25 | 27.83 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8122 | 27.74 | 54.17 | 15.85 | 0 | 32 | 518 |
| rand_write_256B.trace | 9892 | 45.55 | 88.96 | 15.81 | 0 | 32 | 518 |
| rand_write_512B.trace | 18306 | 49.23 | 96.14 | 15.82 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 26.54 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 8952 | 50.33 | 98.30 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 17784 | 50.67 | 98.97 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 3301 | 34.12 | 66.65 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 8948 | 50.35 | 98.35 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 17780 | 50.68 | 98.99 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 3297 | 34.16 | 66.73 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR4 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7615 | 29.58 | 28.89 | 15.84 | 1 | 32 | 517 |
| rand_read_256B.trace | 7890 | 57.11 | 55.77 | 15.80 | 0 | 32 | 518 |
| rand_read_512B.trace | 9715 | 92.76 | 90.58 | 15.86 | 0 | 32 | 518 |
| rand_read_64B.trace | 7905 | 14.25 | 13.92 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8007 | 28.14 | 27.48 | 15.82 | 0 | 32 | 518 |
| rand_write_256B.trace | 8382 | 53.75 | 52.49 | 15.82 | 0 | 32 | 518 |
| rand_write_512B.trace | 9977 | 90.32 | 88.20 | 15.81 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 13.27 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 2548 | 88.41 | 86.34 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 4536 | 99.33 | 97.00 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 8952 | 100.66 | 98.30 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 3301 | 34.12 | 33.32 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 2544 | 88.55 | 86.48 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 4532 | 99.42 | 97.09 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 8948 | 100.71 | 98.35 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 3297 | 34.16 | 33.36 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9822 | 22.94 | 89.59 | 15.89 | 1 | 32 | 517 |
| rand_read_256B.trace | 18133 | 24.85 | 97.06 | 15.85 | 0 | 32 | 518 |
| rand_read_512B.trace | 35825 | 25.15 | 98.26 | 15.93 | 0 | 32 | 518 |
| rand_read_64B.trace | 7995 | 14.09 | 55.03 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 10007 | 22.51 | 87.94 | 15.86 | 0 | 32 | 518 |
| rand_write_256B.trace | 18222 | 24.73 | 96.59 | 15.79 | 0 | 32 | 518 |
| rand_write_512B.trace | 36250 | 24.86 | 97.10 | 15.82 | 0 | 32 | 518 |
| rand_write_64B.trace | 8429 | 13.36 | 52.20 | 15.81 | 0 | 32 | 518 |
| seq_read_128B.trace | 9016 | 24.99 | 97.60 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 17784 | 25.34 | 98.97 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 35448 | 25.42 | 99.30 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 4575 | 24.62 | 96.17 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 9012 | 25.00 | 97.65 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 17780 | 25.34 | 98.99 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 35444 | 25.42 | 99.31 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 4571 | 24.64 | 96.26 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7674 | 29.36 | 57.34 | 15.85 | 1 | 32 | 517 |
| rand_read_256B.trace | 9673 | 46.58 | 90.97 | 15.82 | 0 | 32 | 518 |
| rand_read_512B.trace | 18104 | 49.77 | 97.22 | 15.91 | 0 | 32 | 518 |
| rand_read_64B.trace | 7905 | 14.25 | 27.83 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8122 | 27.74 | 54.17 | 15.85 | 0 | 32 | 518 |
| rand_write_256B.trace | 9892 | 45.55 | 88.96 | 15.81 | 0 | 32 | 518 |
| rand_write_512B.trace | 18306 | 49.23 | 96.14 | 15.82 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 26.54 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 8952 | 50.33 | 98.30 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 17784 | 50.67 | 98.97 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 3301 | 34.12 | 66.65 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 8948 | 50.35 | 98.35 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 17780 | 50.68 | 98.99 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 3297 | 34.16 | 66.73 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR5 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7615 | 29.58 | 28.89 | 15.84 | 1 | 32 | 517 |
| rand_read_256B.trace | 7890 | 57.11 | 55.77 | 15.80 | 0 | 32 | 518 |
| rand_read_512B.trace | 9715 | 92.76 | 90.58 | 15.86 | 0 | 32 | 518 |
| rand_read_64B.trace | 7905 | 14.25 | 13.92 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8007 | 28.14 | 27.48 | 15.82 | 0 | 32 | 518 |
| rand_write_256B.trace | 8382 | 53.75 | 52.49 | 15.82 | 0 | 32 | 518 |
| rand_write_512B.trace | 9977 | 90.32 | 88.20 | 15.81 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 13.27 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 2548 | 88.41 | 86.34 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 4536 | 99.33 | 97.00 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 8952 | 100.66 | 98.30 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 3301 | 34.12 | 33.32 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 2544 | 88.55 | 86.48 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 4532 | 99.42 | 97.09 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 8948 | 100.71 | 98.35 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 3297 | 34.16 | 33.36 | 15.85 | 543 | 7 | 0 |
