# DRAM Simulator Benchmark Results

## Simulation Results (LPDDR4-6400 (16-bit))

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

## Simulation Results (LPDDR4-6400 (32-bit))

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

## Simulation Results (LPDDR4-6400 (64-bit))

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

## Simulation Results (LPDDR4-4266 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9331 | 16.09 | 94.31 | 15.90 | 1 | 32 | 517 |
| rand_read_256B.trace | 18064 | 16.63 | 97.43 | 15.87 | 0 | 32 | 518 |
| rand_read_512B.trace | 35771 | 16.79 | 98.40 | 15.92 | 0 | 32 | 518 |
| rand_read_64B.trace | 5631 | 13.33 | 78.14 | 15.83 | 0 | 32 | 518 |
| rand_write_128B.trace | 9379 | 16.01 | 93.83 | 15.88 | 0 | 32 | 518 |
| rand_write_256B.trace | 18238 | 16.47 | 96.50 | 15.75 | 0 | 32 | 518 |
| rand_write_512B.trace | 36365 | 16.52 | 96.80 | 15.87 | 0 | 32 | 518 |
| rand_write_64B.trace | 6065 | 12.38 | 72.55 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 8976 | 16.73 | 98.04 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 17744 | 16.93 | 99.19 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 35408 | 16.96 | 99.41 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 4528 | 16.58 | 97.17 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8974 | 16.73 | 98.06 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 17742 | 16.93 | 99.20 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 35406 | 16.96 | 99.42 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 4526 | 16.59 | 97.22 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5450 | 27.55 | 80.73 | 15.86 | 1 | 32 | 517 |
| rand_read_256B.trace | 9190 | 32.68 | 95.76 | 15.87 | 0 | 32 | 518 |
| rand_read_512B.trace | 17987 | 33.39 | 97.85 | 15.92 | 0 | 32 | 518 |
| rand_read_64B.trace | 5328 | 14.09 | 41.29 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 5766 | 26.04 | 76.31 | 15.84 | 0 | 32 | 518 |
| rand_write_256B.trace | 9331 | 32.19 | 94.31 | 15.80 | 0 | 32 | 518 |
| rand_write_512B.trace | 18198 | 33.01 | 96.71 | 15.85 | 0 | 32 | 518 |
| rand_write_64B.trace | 5654 | 13.28 | 38.91 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 4528 | 33.16 | 97.17 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 8912 | 33.70 | 98.74 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 17744 | 33.85 | 99.19 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 2737 | 27.43 | 80.38 | 15.76 | 543 | 7 | 0 |
| seq_write_128B.trace | 4526 | 33.18 | 97.22 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 8910 | 33.71 | 98.77 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 17742 | 33.85 | 99.20 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 2735 | 27.45 | 80.44 | 15.76 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5122 | 29.32 | 42.95 | 15.84 | 1 | 32 | 517 |
| rand_read_256B.trace | 5636 | 53.29 | 78.07 | 15.81 | 0 | 32 | 518 |
| rand_read_512B.trace | 9216 | 65.18 | 95.49 | 15.88 | 0 | 32 | 518 |
| rand_read_64B.trace | 5328 | 14.09 | 20.65 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 5466 | 27.47 | 40.25 | 15.83 | 0 | 32 | 518 |
| rand_write_256B.trace | 5903 | 50.88 | 74.54 | 15.81 | 0 | 32 | 518 |
| rand_write_512B.trace | 9171 | 65.49 | 95.95 | 15.84 | 0 | 32 | 518 |
| rand_write_64B.trace | 5654 | 13.28 | 19.46 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 2346 | 64.01 | 93.78 | 15.79 | 538 | 12 | 0 |
| seq_read_256B.trace | 4496 | 66.80 | 97.86 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 8912 | 67.40 | 98.74 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 2737 | 27.43 | 40.19 | 15.76 | 543 | 7 | 0 |
| seq_write_128B.trace | 2344 | 64.06 | 93.86 | 15.79 | 538 | 12 | 0 |
| seq_write_256B.trace | 4494 | 66.83 | 97.91 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 8910 | 67.41 | 98.77 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 2735 | 27.45 | 40.22 | 15.76 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (16-bit))

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

## Simulation Results (LPDDR5-6400 (32-bit))

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

## Simulation Results (LPDDR5-6400 (64-bit))

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

## Simulation Results (LPDDR5-8533 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 10841 | 27.70 | 81.17 | 15.87 | 1 | 32 | 517 |
| rand_read_256B.trace | 18397 | 32.65 | 95.67 | 15.88 | 0 | 32 | 518 |
| rand_read_512B.trace | 35971 | 33.40 | 97.86 | 15.92 | 0 | 32 | 518 |
| rand_read_64B.trace | 10577 | 14.20 | 41.60 | 15.87 | 0 | 32 | 518 |
| rand_write_128B.trace | 11404 | 26.34 | 77.17 | 15.88 | 0 | 32 | 518 |
| rand_write_256B.trace | 18594 | 32.30 | 94.65 | 15.81 | 0 | 32 | 518 |
| rand_write_512B.trace | 36189 | 33.20 | 97.27 | 15.86 | 0 | 32 | 518 |
| rand_write_64B.trace | 11032 | 13.61 | 39.88 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 9056 | 33.16 | 97.17 | 15.66 | 538 | 12 | 0 |
| seq_read_256B.trace | 17824 | 33.70 | 98.74 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 35488 | 33.85 | 99.19 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 5472 | 27.44 | 80.41 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 9051 | 33.18 | 97.23 | 15.66 | 538 | 12 | 0 |
| seq_write_256B.trace | 17819 | 33.71 | 98.77 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 35483 | 33.86 | 99.20 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 5467 | 27.47 | 80.48 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 10192 | 29.47 | 43.17 | 15.85 | 1 | 32 | 517 |
| rand_read_256B.trace | 11237 | 53.45 | 78.31 | 15.82 | 0 | 32 | 518 |
| rand_read_512B.trace | 18406 | 65.27 | 95.62 | 15.88 | 0 | 32 | 518 |
| rand_read_64B.trace | 10533 | 14.26 | 20.89 | 15.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 10667 | 28.15 | 41.25 | 15.83 | 0 | 32 | 518 |
| rand_write_256B.trace | 11690 | 51.38 | 75.28 | 15.80 | 0 | 32 | 518 |
| rand_write_512B.trace | 18313 | 65.60 | 96.11 | 15.85 | 0 | 32 | 518 |
| rand_write_64B.trace | 10975 | 13.68 | 20.05 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 4686 | 64.09 | 93.90 | 15.77 | 538 | 12 | 0 |
| seq_read_256B.trace | 8992 | 66.80 | 97.86 | 15.75 | 530 | 20 | 0 |
| seq_read_512B.trace | 17824 | 67.40 | 98.74 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 4477 | 33.54 | 49.14 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 4681 | 64.16 | 94.00 | 15.77 | 538 | 12 | 0 |
| seq_write_256B.trace | 8987 | 66.84 | 97.92 | 15.75 | 530 | 20 | 0 |
| seq_write_512B.trace | 17819 | 67.42 | 98.77 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 4472 | 33.58 | 49.19 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 10156 | 29.57 | 21.66 | 15.84 | 1 | 32 | 517 |
| rand_read_256B.trace | 10465 | 57.40 | 42.04 | 15.79 | 0 | 32 | 518 |
| rand_read_512B.trace | 10721 | 112.05 | 82.08 | 15.84 | 0 | 32 | 518 |
| rand_read_64B.trace | 10533 | 14.26 | 10.44 | 15.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 10603 | 28.32 | 20.75 | 15.83 | 0 | 32 | 518 |
| rand_write_256B.trace | 11032 | 54.45 | 39.88 | 15.82 | 0 | 32 | 518 |
| rand_write_512B.trace | 11884 | 101.09 | 74.05 | 15.77 | 0 | 32 | 518 |
| rand_write_64B.trace | 10975 | 13.68 | 10.02 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 3478 | 86.35 | 63.25 | 15.78 | 538 | 12 | 0 |
| seq_read_256B.trace | 4598 | 130.63 | 95.69 | 15.74 | 530 | 20 | 0 |
| seq_read_512B.trace | 8992 | 133.60 | 97.86 | 15.76 | 514 | 32 | 4 |
| seq_read_64B.trace | 4477 | 33.54 | 24.57 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 3473 | 86.47 | 63.35 | 15.78 | 538 | 12 | 0 |
| seq_write_256B.trace | 4593 | 130.78 | 95.80 | 15.74 | 530 | 20 | 0 |
| seq_write_512B.trace | 8987 | 133.67 | 97.92 | 15.76 | 514 | 32 | 4 |
| seq_write_64B.trace | 4472 | 33.58 | 24.60 | 15.85 | 543 | 7 | 0 |
