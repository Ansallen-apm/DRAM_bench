# DRAM Simulator Benchmark Results

## Simulation Results (LPDDR4-6400 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9822 | 22.94 | 89.59 | 15.89 | 1 | 32 | 517 |
| rand_read_64B.trace | 7995 | 14.09 | 55.03 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 10007 | 22.51 | 87.94 | 15.86 | 0 | 32 | 518 |
| rand_write_64B.trace | 8429 | 13.36 | 52.20 | 15.81 | 0 | 32 | 518 |
| seq_read_128B.trace | 9016 | 24.99 | 97.60 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 4575 | 24.62 | 96.17 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 9012 | 25.00 | 97.65 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 4571 | 24.64 | 96.26 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-6400 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7674 | 29.36 | 57.34 | 15.85 | 1 | 32 | 517 |
| rand_read_64B.trace | 7905 | 14.25 | 27.83 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8122 | 27.74 | 54.17 | 15.85 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 26.54 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 3301 | 34.12 | 66.65 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 3297 | 34.16 | 66.73 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-6400 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7615 | 29.58 | 28.89 | 15.84 | 1 | 32 | 517 |
| rand_read_64B.trace | 7905 | 14.25 | 27.83 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8007 | 28.14 | 27.48 | 15.82 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 26.54 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 2548 | 88.41 | 86.34 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 3301 | 34.12 | 66.65 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 2544 | 88.55 | 86.48 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 3297 | 34.16 | 66.73 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9331 | 16.09 | 94.31 | 15.90 | 1 | 32 | 517 |
| rand_read_64B.trace | 5631 | 13.33 | 78.14 | 15.83 | 0 | 32 | 518 |
| rand_write_128B.trace | 9379 | 16.01 | 93.83 | 15.88 | 0 | 32 | 518 |
| rand_write_64B.trace | 6065 | 12.38 | 72.55 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 8976 | 16.73 | 98.04 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 4528 | 16.58 | 97.17 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 8974 | 16.73 | 98.06 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 4526 | 16.59 | 97.22 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5450 | 27.55 | 80.73 | 15.86 | 1 | 32 | 517 |
| rand_read_64B.trace | 5328 | 14.09 | 41.29 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 5766 | 26.04 | 76.31 | 15.84 | 0 | 32 | 518 |
| rand_write_64B.trace | 5654 | 13.28 | 38.91 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 4528 | 33.16 | 97.17 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 2737 | 27.43 | 80.38 | 15.76 | 543 | 7 | 0 |
| seq_write_128B.trace | 4526 | 33.18 | 97.22 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 2735 | 27.45 | 80.44 | 15.76 | 543 | 7 | 0 |

## Simulation Results (LPDDR4-4266 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 5122 | 29.32 | 42.95 | 15.84 | 1 | 32 | 517 |
| rand_read_64B.trace | 5328 | 14.09 | 41.29 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 5466 | 27.47 | 40.25 | 15.83 | 0 | 32 | 518 |
| rand_write_64B.trace | 5654 | 13.28 | 38.91 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 2346 | 64.01 | 93.78 | 15.79 | 538 | 12 | 0 |
| seq_read_64B.trace | 2737 | 27.43 | 80.38 | 15.76 | 543 | 7 | 0 |
| seq_write_128B.trace | 2344 | 64.06 | 93.86 | 15.79 | 538 | 12 | 0 |
| seq_write_64B.trace | 2735 | 27.45 | 80.44 | 15.76 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 9822 | 22.94 | 89.59 | 15.89 | 1 | 32 | 517 |
| rand_read_64B.trace | 7995 | 14.09 | 55.03 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 10007 | 22.51 | 87.94 | 15.86 | 0 | 32 | 518 |
| rand_write_64B.trace | 8429 | 13.36 | 52.20 | 15.81 | 0 | 32 | 518 |
| seq_read_128B.trace | 9016 | 24.99 | 97.60 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 4575 | 24.62 | 96.17 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 9012 | 25.00 | 97.65 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 4571 | 24.64 | 96.26 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7674 | 29.36 | 57.34 | 15.85 | 1 | 32 | 517 |
| rand_read_64B.trace | 7905 | 14.25 | 27.83 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8122 | 27.74 | 54.17 | 15.85 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 26.54 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 4568 | 49.32 | 96.32 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 3301 | 34.12 | 66.65 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 4564 | 49.36 | 96.41 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 3297 | 34.16 | 66.73 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-6400 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 7615 | 29.58 | 28.89 | 15.84 | 1 | 32 | 517 |
| rand_read_64B.trace | 7905 | 14.25 | 27.83 | 15.84 | 0 | 32 | 518 |
| rand_write_128B.trace | 8007 | 28.14 | 27.48 | 15.82 | 0 | 32 | 518 |
| rand_write_64B.trace | 8288 | 13.59 | 26.54 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 2548 | 88.41 | 86.34 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 3301 | 34.12 | 66.65 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 2544 | 88.55 | 86.48 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 3297 | 34.16 | 66.73 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (16-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 10841 | 27.70 | 81.17 | 15.87 | 1 | 32 | 517 |
| rand_read_64B.trace | 10577 | 14.20 | 41.60 | 15.87 | 0 | 32 | 518 |
| rand_write_128B.trace | 11404 | 26.34 | 77.17 | 15.88 | 0 | 32 | 518 |
| rand_write_64B.trace | 11032 | 13.61 | 39.88 | 15.82 | 0 | 32 | 518 |
| seq_read_128B.trace | 9056 | 33.16 | 97.17 | 15.66 | 538 | 12 | 0 |
| seq_read_64B.trace | 5472 | 27.44 | 80.41 | 15.78 | 543 | 7 | 0 |
| seq_write_128B.trace | 9051 | 33.18 | 97.23 | 15.66 | 538 | 12 | 0 |
| seq_write_64B.trace | 5467 | 27.47 | 80.48 | 15.78 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (32-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 10192 | 29.47 | 43.17 | 15.85 | 1 | 32 | 517 |
| rand_read_64B.trace | 10533 | 14.26 | 20.89 | 15.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 10667 | 28.15 | 41.25 | 15.83 | 0 | 32 | 518 |
| rand_write_64B.trace | 10975 | 13.68 | 20.05 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 4686 | 64.09 | 93.90 | 15.77 | 538 | 12 | 0 |
| seq_read_64B.trace | 4477 | 33.54 | 49.14 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 4681 | 64.16 | 94.00 | 15.77 | 538 | 12 | 0 |
| seq_write_64B.trace | 4472 | 33.58 | 49.19 | 15.85 | 543 | 7 | 0 |

## Simulation Results (LPDDR5-8533 (64-bit))

| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 10156 | 29.57 | 21.66 | 15.84 | 1 | 32 | 517 |
| rand_read_64B.trace | 10533 | 14.26 | 20.89 | 15.85 | 0 | 32 | 518 |
| rand_write_128B.trace | 10603 | 28.32 | 20.75 | 15.83 | 0 | 32 | 518 |
| rand_write_64B.trace | 10975 | 13.68 | 20.05 | 15.83 | 0 | 32 | 518 |
| seq_read_128B.trace | 3478 | 86.35 | 63.25 | 15.78 | 538 | 12 | 0 |
| seq_read_64B.trace | 4477 | 33.54 | 49.14 | 15.85 | 543 | 7 | 0 |
| seq_write_128B.trace | 3473 | 86.47 | 63.35 | 15.78 | 538 | 12 | 0 |
| seq_write_64B.trace | 4472 | 33.58 | 49.19 | 15.85 | 543 | 7 | 0 |
