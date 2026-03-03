# DRAM Simulator Benchmark Results (Queue Depth = 64)

## Simulation Results (LPDDR4-6400 (32-bit)) - QD=64 - Policy=FIFO

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

## Simulation Results (LPDDR4-6400 (32-bit)) - QD=64 - Policy=PageHitFirst

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5263 | 42.80 | 83.60 | 60.46 | 1 | 32 | 517 |
| rand_read_256B.trace | 9347 | 48.20 | 94.15 | 61.77 | 0 | 32 | 518 |
| rand_read_512B.trace | 17890 | 50.37 | 98.38 | 62.13 | 0 | 32 | 518 |
| rand_read_64B.trace | 6147 | 18.32 | 35.79 | 59.68 | 0 | 32 | 518 |
| rand_write_128B.trace | 6487 | 34.73 | 67.83 | 60.06 | 0 | 32 | 518 |
| rand_write_256B.trace | 9244 | 48.74 | 95.20 | 60.90 | 0 | 32 | 518 |
| rand_write_512B.trace | 17780 | 50.68 | 98.99 | 62.45 | 0 | 32 | 518 |
| rand_write_64B.trace | 6110 | 18.44 | 36.01 | 59.01 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 8952 | 50.33 | 98.30 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 17784 | 50.67 | 98.97 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2416 | 46.62 | 91.06 | 60.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 8948 | 50.35 | 98.35 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 17780 | 50.68 | 98.99 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2412 | 46.70 | 91.21 | 60.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-6400 (64-bit)) - QD=64 - Policy=FIFO

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

## Simulation Results (LPDDR4-6400 (64-bit)) - QD=64 - Policy=PageHitFirst

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5241 | 42.98 | 41.98 | 59.45 | 1 | 32 | 517 |
| rand_read_256B.trace | 5856 | 76.94 | 75.14 | 60.14 | 0 | 32 | 518 |
| rand_read_512B.trace | 9133 | 98.67 | 96.35 | 61.79 | 0 | 32 | 518 |
| rand_read_64B.trace | 6147 | 18.32 | 35.79 | 59.68 | 0 | 32 | 518 |
| rand_write_128B.trace | 6308 | 35.71 | 34.88 | 59.88 | 0 | 32 | 518 |
| rand_write_256B.trace | 6644 | 67.81 | 66.23 | 59.95 | 0 | 32 | 518 |
| rand_write_512B.trace | 9392 | 95.95 | 93.70 | 61.52 | 0 | 32 | 518 |
| rand_write_64B.trace | 6110 | 18.44 | 36.01 | 59.01 | 0 | 32 | 518 |
| seq_read_128B.trace | 2384 | 94.50 | 92.28 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 4536 | 99.33 | 97.00 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 8952 | 100.66 | 98.30 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2416 | 46.62 | 91.06 | 60.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 2380 | 94.66 | 92.44 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 4532 | 99.42 | 97.09 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 8948 | 100.71 | 98.35 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2412 | 46.70 | 91.21 | 60.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (32-bit)) - QD=64 - Policy=FIFO

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

## Simulation Results (LPDDR4-4266 (32-bit)) - QD=64 - Policy=PageHitFirst

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 4672 | 32.14 | 94.18 | 60.81 | 1 | 32 | 517 |
| rand_read_256B.trace | 9072 | 33.10 | 97.00 | 62.05 | 0 | 32 | 518 |
| rand_read_512B.trace | 17744 | 33.85 | 99.19 | 62.59 | 0 | 32 | 518 |
| rand_read_64B.trace | 4134 | 18.16 | 53.22 | 59.41 | 0 | 32 | 518 |
| rand_write_128B.trace | 4780 | 31.41 | 92.05 | 60.55 | 0 | 32 | 518 |
| rand_write_256B.trace | 9215 | 32.59 | 95.50 | 61.33 | 0 | 32 | 518 |
| rand_write_512B.trace | 17742 | 33.85 | 99.20 | 62.48 | 0 | 32 | 518 |
| rand_write_64B.trace | 4179 | 17.97 | 52.64 | 59.54 | 0 | 32 | 518 |
| seq_read_128B.trace | 4528 | 33.16 | 97.17 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 8912 | 33.70 | 98.74 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 17744 | 33.85 | 99.19 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2331 | 32.21 | 94.38 | 58.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 4526 | 33.18 | 97.22 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 8910 | 33.71 | 98.77 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 17742 | 33.85 | 99.20 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2329 | 32.24 | 94.46 | 58.08 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (64-bit)) - QD=64 - Policy=FIFO

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

## Simulation Results (LPDDR4-4266 (64-bit)) - QD=64 - Policy=PageHitFirst

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 3548 | 42.32 | 62.01 | 59.68 | 1 | 32 | 517 |
| rand_read_256B.trace | 5011 | 59.93 | 87.81 | 61.03 | 0 | 32 | 518 |
| rand_read_512B.trace | 8961 | 67.03 | 98.20 | 62.05 | 0 | 32 | 518 |
| rand_read_64B.trace | 4134 | 18.16 | 53.22 | 59.41 | 0 | 32 | 518 |
| rand_write_128B.trace | 4340 | 34.60 | 50.69 | 59.58 | 0 | 32 | 518 |
| rand_write_256B.trace | 4903 | 61.25 | 89.74 | 60.59 | 0 | 32 | 518 |
| rand_write_512B.trace | 9012 | 66.65 | 97.65 | 62.00 | 0 | 32 | 518 |
| rand_write_64B.trace | 4179 | 17.97 | 52.64 | 59.54 | 0 | 32 | 518 |
| seq_read_128B.trace | 2319 | 64.75 | 94.87 | 59.85 | 538 | 12 | 0 |
| seq_read_256B.trace | 4496 | 66.80 | 97.86 | 60.30 | 530 | 20 | 0 |
| seq_read_512B.trace | 8912 | 67.40 | 98.74 | 60.45 | 514 | 32 | 4 |
| seq_read_64B.trace | 2331 | 32.21 | 94.38 | 58.08 | 543 | 7 | 0 |
| seq_write_128B.trace | 2317 | 64.81 | 94.95 | 59.85 | 538 | 12 | 0 |
| seq_write_256B.trace | 4494 | 66.83 | 97.91 | 60.30 | 530 | 20 | 0 |
| seq_write_512B.trace | 8910 | 67.41 | 98.77 | 60.45 | 514 | 32 | 4 |
| seq_write_64B.trace | 2329 | 32.24 | 94.46 | 58.08 | 543 | 7 | 0 |
