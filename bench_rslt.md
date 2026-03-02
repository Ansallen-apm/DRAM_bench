# DRAM Simulator Benchmark Results (Queue Depth = 64)

## Simulation Results (LPDDR4-6400 (16-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9308 | 24.20 | 94.54 | 61.44 | 1 | 32 | 517 |
| rand_read_256B.trace | 18105 | 24.89 | 97.21 | 62.04 | 0 | 32 | 518 |
| rand_read_512B.trace | 35448 | 25.42 | 99.30 | 62.53 | 0 | 32 | 518 |
| rand_read_64B.trace | 6173 | 18.25 | 71.28 | 60.05 | 0 | 32 | 518 |
| rand_write_128B.trace | 9173 | 24.56 | 95.93 | 61.16 | 0 | 32 | 518 |
| rand_write_256B.trace | 18250 | 24.69 | 96.44 | 61.58 | 0 | 32 | 518 |
| rand_write_512B.trace | 35452 | 25.42 | 99.29 | 62.50 | 0 | 32 | 518 |
| rand_write_64B.trace | 6241 | 18.05 | 70.50 | 59.92 | 0 | 32 | 518 |
| seq_read_128B.trace | 9016 | 24.99 | 97.60 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 17784 | 25.34 | 98.97 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 35448 | 25.42 | 99.30 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 4568 | 24.66 | 96.32 | 59.81 | 543 | 7 | 0 |
| seq_write_128B.trace | 9012 | 25.00 | 97.65 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 17780 | 25.34 | 98.99 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 35444 | 25.42 | 99.31 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 4564 | 24.68 | 96.41 | 59.81 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-6400 (32-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5262 | 42.81 | 83.62 | 60.18 | 1 | 32 | 517 |
| rand_read_256B.trace | 9335 | 48.27 | 94.27 | 61.39 | 0 | 32 | 518 |
| rand_read_512B.trace | 17893 | 50.36 | 98.36 | 62.22 | 0 | 32 | 518 |
| rand_read_64B.trace | 6151 | 18.31 | 35.77 | 59.15 | 0 | 32 | 518 |
| rand_write_128B.trace | 6485 | 34.74 | 67.85 | 60.09 | 0 | 32 | 518 |
| rand_write_256B.trace | 9306 | 48.42 | 94.56 | 61.04 | 0 | 32 | 518 |
| rand_write_512B.trace | 17898 | 50.35 | 98.34 | 62.13 | 0 | 32 | 518 |
| rand_write_64B.trace | 6113 | 18.43 | 35.99 | 59.10 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 8952 | 50.33 | 98.30 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 17784 | 50.67 | 98.97 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2416 | 46.62 | 91.06 | 60.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 8948 | 50.35 | 98.35 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 17780 | 50.68 | 98.99 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2412 | 46.70 | 91.21 | 60.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-6400 (64-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5254 | 42.88 | 41.87 | 59.67 | 1 | 32 | 517 |
| rand_read_256B.trace | 5674 | 79.41 | 77.55 | 59.87 | 0 | 32 | 518 |
| rand_read_512B.trace | 9158 | 98.40 | 96.09 | 61.82 | 0 | 32 | 518 |
| rand_read_64B.trace | 6151 | 18.31 | 35.77 | 59.15 | 0 | 32 | 518 |
| rand_write_128B.trace | 6316 | 35.67 | 34.83 | 60.02 | 0 | 32 | 518 |
| rand_write_256B.trace | 6644 | 67.81 | 66.23 | 59.83 | 0 | 32 | 518 |
| rand_write_512B.trace | 9386 | 96.01 | 93.76 | 61.22 | 0 | 32 | 518 |
| rand_write_64B.trace | 6113 | 18.43 | 35.99 | 59.10 | 0 | 32 | 518 |
| seq_read_128B.trace | 2384 | 94.50 | 92.28 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 4536 | 99.33 | 97.00 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 8952 | 100.66 | 98.30 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2416 | 46.62 | 91.06 | 60.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 2380 | 94.66 | 92.44 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 4532 | 99.42 | 97.09 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 8948 | 100.71 | 98.35 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2412 | 46.70 | 91.21 | 60.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (16-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9270 | 16.20 | 94.93 | 61.76 | 1 | 32 | 517 |
| rand_read_256B.trace | 18064 | 16.63 | 97.43 | 62.51 | 0 | 32 | 518 |
| rand_read_512B.trace | 35461 | 16.94 | 99.26 | 62.32 | 0 | 32 | 518 |
| rand_read_64B.trace | 4650 | 16.15 | 94.62 | 61.07 | 0 | 32 | 518 |
| rand_write_128B.trace | 9083 | 16.53 | 96.88 | 61.75 | 0 | 32 | 518 |
| rand_write_256B.trace | 18249 | 16.46 | 96.44 | 61.77 | 0 | 32 | 518 |
| rand_write_512B.trace | 35548 | 16.90 | 99.02 | 62.24 | 0 | 32 | 518 |
| rand_write_64B.trace | 4845 | 15.50 | 90.82 | 60.28 | 0 | 32 | 518 |
| seq_read_128B.trace | 8976 | 16.73 | 98.04 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 17744 | 16.93 | 99.19 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 35408 | 16.96 | 99.41 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 4528 | 16.58 | 97.17 | 59.81 | 543 | 7 | 0 |
| seq_write_128B.trace | 8974 | 16.73 | 98.06 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 17742 | 16.93 | 99.20 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 35406 | 16.96 | 99.42 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 4526 | 16.59 | 97.22 | 59.81 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (32-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 4682 | 32.07 | 93.98 | 61.06 | 1 | 32 | 517 |
| rand_read_256B.trace | 9076 | 33.09 | 96.96 | 61.88 | 0 | 32 | 518 |
| rand_read_512B.trace | 17745 | 33.85 | 99.18 | 62.41 | 0 | 32 | 518 |
| rand_read_64B.trace | 4136 | 18.15 | 53.19 | 59.47 | 0 | 32 | 518 |
| rand_write_128B.trace | 4912 | 30.57 | 89.58 | 60.49 | 0 | 32 | 518 |
| rand_write_256B.trace | 9178 | 32.72 | 95.88 | 61.33 | 0 | 32 | 518 |
| rand_write_512B.trace | 17743 | 33.85 | 99.19 | 62.37 | 0 | 32 | 518 |
| rand_write_64B.trace | 4182 | 17.95 | 52.61 | 59.92 | 0 | 32 | 518 |
| seq_read_128B.trace | 4528 | 33.16 | 97.17 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 8912 | 33.70 | 98.74 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 17744 | 33.85 | 99.19 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2331 | 32.21 | 94.38 | 58.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 4526 | 33.18 | 97.22 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 8910 | 33.71 | 98.77 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 17742 | 33.85 | 99.20 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2329 | 32.24 | 94.46 | 58.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (64-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 3547 | 42.34 | 62.02 | 59.64 | 1 | 32 | 517 |
| rand_read_256B.trace | 5005 | 60.01 | 87.91 | 61.05 | 0 | 32 | 518 |
| rand_read_512B.trace | 8984 | 66.86 | 97.95 | 61.95 | 0 | 32 | 518 |
| rand_read_64B.trace | 4136 | 18.15 | 53.19 | 59.47 | 0 | 32 | 518 |
| rand_write_128B.trace | 4361 | 34.43 | 50.45 | 59.82 | 0 | 32 | 518 |
| rand_write_256B.trace | 4891 | 61.40 | 89.96 | 60.91 | 0 | 32 | 518 |
| rand_write_512B.trace | 8997 | 66.76 | 97.81 | 61.78 | 0 | 32 | 518 |
| rand_write_64B.trace | 4182 | 17.95 | 52.61 | 59.92 | 0 | 32 | 518 |
| seq_read_128B.trace | 2319 | 64.75 | 94.87 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 4496 | 66.80 | 97.86 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 8912 | 67.40 | 98.74 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2331 | 32.21 | 94.38 | 58.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 2317 | 64.81 | 94.95 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 4494 | 66.83 | 97.91 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 8910 | 67.41 | 98.77 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2329 | 32.24 | 94.46 | 58.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (16-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9308 | 24.20 | 94.54 | 61.44 | 1 | 32 | 517 |
| rand_read_256B.trace | 18105 | 24.89 | 97.21 | 62.04 | 0 | 32 | 518 |
| rand_read_512B.trace | 35448 | 25.42 | 99.30 | 62.53 | 0 | 32 | 518 |
| rand_read_64B.trace | 6173 | 18.25 | 71.28 | 60.05 | 0 | 32 | 518 |
| rand_write_128B.trace | 9173 | 24.56 | 95.93 | 61.16 | 0 | 32 | 518 |
| rand_write_256B.trace | 18250 | 24.69 | 96.44 | 61.58 | 0 | 32 | 518 |
| rand_write_512B.trace | 35452 | 25.42 | 99.29 | 62.50 | 0 | 32 | 518 |
| rand_write_64B.trace | 6241 | 18.05 | 70.50 | 59.92 | 0 | 32 | 518 |
| seq_read_128B.trace | 9016 | 24.99 | 97.60 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 17784 | 25.34 | 98.97 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 35448 | 25.42 | 99.30 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 4568 | 24.66 | 96.32 | 59.81 | 543 | 7 | 0 |
| seq_write_128B.trace | 9012 | 25.00 | 97.65 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 17780 | 25.34 | 98.99 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 35444 | 25.42 | 99.31 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 4564 | 24.68 | 96.41 | 59.81 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (32-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5262 | 42.81 | 83.62 | 60.18 | 1 | 32 | 517 |
| rand_read_256B.trace | 9335 | 48.27 | 94.27 | 61.39 | 0 | 32 | 518 |
| rand_read_512B.trace | 17893 | 50.36 | 98.36 | 62.22 | 0 | 32 | 518 |
| rand_read_64B.trace | 6151 | 18.31 | 35.77 | 59.15 | 0 | 32 | 518 |
| rand_write_128B.trace | 6485 | 34.74 | 67.85 | 60.09 | 0 | 32 | 518 |
| rand_write_256B.trace | 9306 | 48.42 | 94.56 | 61.04 | 0 | 32 | 518 |
| rand_write_512B.trace | 17898 | 50.35 | 98.34 | 62.13 | 0 | 32 | 518 |
| rand_write_64B.trace | 6113 | 18.43 | 35.99 | 59.10 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 8952 | 50.33 | 98.30 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 17784 | 50.67 | 98.97 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2416 | 46.62 | 91.06 | 60.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 8948 | 50.35 | 98.35 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 17780 | 50.68 | 98.99 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2412 | 46.70 | 91.21 | 60.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (64-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5254 | 42.88 | 41.87 | 59.67 | 1 | 32 | 517 |
| rand_read_256B.trace | 5674 | 79.41 | 77.55 | 59.87 | 0 | 32 | 518 |
| rand_read_512B.trace | 9158 | 98.40 | 96.09 | 61.82 | 0 | 32 | 518 |
| rand_read_64B.trace | 6151 | 18.31 | 35.77 | 59.15 | 0 | 32 | 518 |
| rand_write_128B.trace | 6316 | 35.67 | 34.83 | 60.02 | 0 | 32 | 518 |
| rand_write_256B.trace | 6644 | 67.81 | 66.23 | 59.83 | 0 | 32 | 518 |
| rand_write_512B.trace | 9386 | 96.01 | 93.76 | 61.22 | 0 | 32 | 518 |
| rand_write_64B.trace | 6113 | 18.43 | 35.99 | 59.10 | 0 | 32 | 518 |
| seq_read_128B.trace | 2384 | 94.50 | 92.28 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 4536 | 99.33 | 97.00 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 8952 | 100.66 | 98.30 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2416 | 46.62 | 91.06 | 60.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 2380 | 94.66 | 92.44 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 4532 | 99.42 | 97.09 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 8948 | 100.71 | 98.35 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2412 | 46.70 | 91.21 | 60.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (16-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9351 | 32.12 | 94.11 | 61.13 | 1 | 32 | 517 |
| rand_read_256B.trace | 18145 | 33.10 | 97.00 | 62.06 | 0 | 32 | 518 |
| rand_read_512B.trace | 35531 | 33.81 | 99.07 | 62.58 | 0 | 32 | 518 |
| rand_read_64B.trace | 8229 | 18.25 | 53.47 | 59.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 9545 | 31.46 | 92.19 | 61.30 | 0 | 32 | 518 |
| rand_write_256B.trace | 18469 | 32.52 | 95.29 | 61.39 | 0 | 32 | 518 |
| rand_write_512B.trace | 35483 | 33.86 | 99.20 | 62.58 | 0 | 32 | 518 |
| rand_write_64B.trace | 8141 | 18.45 | 54.05 | 60.13 | 0 | 32 | 518 |
| seq_read_128B.trace | 9056 | 33.16 | 97.17 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 17824 | 33.70 | 98.74 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 35488 | 33.85 | 99.19 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 4662 | 32.21 | 94.38 | 57.98 | 543 | 7 | 0 |
| seq_write_128B.trace | 9051 | 33.18 | 97.23 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 17819 | 33.71 | 98.77 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 35483 | 33.86 | 99.20 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 4657 | 32.24 | 94.48 | 57.98 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (32-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7045 | 42.63 | 62.46 | 59.90 | 1 | 32 | 517 |
| rand_read_256B.trace | 9949 | 60.37 | 88.45 | 61.26 | 0 | 32 | 518 |
| rand_read_512B.trace | 18026 | 66.64 | 97.64 | 61.97 | 0 | 32 | 518 |
| rand_read_64B.trace | 8202 | 18.31 | 26.82 | 59.50 | 0 | 32 | 518 |
| rand_write_128B.trace | 8451 | 35.54 | 52.06 | 59.84 | 0 | 32 | 518 |
| rand_write_256B.trace | 9804 | 61.27 | 89.76 | 60.95 | 0 | 32 | 518 |
| rand_write_512B.trace | 17890 | 67.15 | 98.38 | 62.29 | 0 | 32 | 518 |
| rand_write_64B.trace | 8065 | 18.62 | 27.28 | 59.87 | 0 | 32 | 518 |
| seq_read_128B.trace | 4638 | 64.75 | 94.87 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 8992 | 66.80 | 97.86 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 17824 | 67.40 | 98.74 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 3148 | 47.70 | 69.89 | 59.01 | 543 | 7 | 0 |
| seq_write_128B.trace | 4633 | 64.82 | 94.97 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 8987 | 66.84 | 97.92 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 17819 | 67.42 | 98.77 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 3143 | 47.78 | 70.00 | 59.01 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (64-bit)) - QD=64

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7012 | 42.83 | 31.37 | 59.97 | 1 | 32 | 517 |
| rand_read_256B.trace | 7146 | 84.05 | 61.57 | 59.81 | 0 | 32 | 518 |
| rand_read_512B.trace | 9211 | 130.42 | 95.54 | 61.38 | 0 | 32 | 518 |
| rand_read_64B.trace | 8202 | 18.31 | 26.82 | 59.50 | 0 | 32 | 518 |
| rand_write_128B.trace | 8380 | 35.84 | 26.25 | 59.48 | 0 | 32 | 518 |
| rand_write_256B.trace | 8794 | 68.30 | 50.03 | 60.26 | 0 | 32 | 518 |
| rand_write_512B.trace | 10262 | 117.06 | 85.75 | 60.90 | 0 | 32 | 518 |
| rand_write_64B.trace | 8065 | 18.62 | 27.28 | 59.87 | 0 | 32 | 518 |
| seq_read_128B.trace | 3000 | 100.11 | 73.33 | 59.69 | 538 | 12 | 0 |
| seq_read_256B.trace | 4594 | 130.75 | 95.78 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 8992 | 133.60 | 97.86 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 3148 | 47.70 | 69.89 | 59.01 | 543 | 7 | 0 |
| seq_write_128B.trace | 2995 | 100.28 | 73.46 | 59.69 | 538 | 12 | 0 |
| seq_write_256B.trace | 4589 | 130.89 | 95.88 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 8987 | 133.67 | 97.92 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 3143 | 47.78 | 70.00 | 59.01 | 543 | 7 | 0 |
