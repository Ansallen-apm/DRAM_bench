# DRAM Simulator Benchmark Utilization Comparison (QD=16 vs QD=64)
This file compares the Utilization (%) between the default Queue Depth 16 (`BENCHMARK_RESULTS.md`) and Queue Depth 64 (`bench_rslt.md`).


## LPDDR4-4266 (16-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 94.31 | N/A | N/A |
| rand_read_256B.trace | 97.43 | N/A | N/A |
| rand_read_512B.trace | 98.40 | N/A | N/A |
| rand_read_64B.trace | 78.14 | N/A | N/A |
| rand_write_128B.trace | 93.83 | N/A | N/A |
| rand_write_256B.trace | 96.50 | N/A | N/A |
| rand_write_512B.trace | 96.80 | N/A | N/A |
| rand_write_64B.trace | 72.55 | N/A | N/A |
| seq_read_128B.trace | 98.04 | N/A | N/A |
| seq_read_256B.trace | 99.19 | N/A | N/A |
| seq_read_512B.trace | 99.41 | N/A | N/A |
| seq_read_64B.trace | 97.17 | N/A | N/A |
| seq_write_128B.trace | 98.06 | N/A | N/A |
| seq_write_256B.trace | 99.20 | N/A | N/A |
| seq_write_512B.trace | 99.42 | N/A | N/A |
| seq_write_64B.trace | 97.22 | N/A | N/A |

## LPDDR4-4266 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 80.73 | 94.18 | +13.45 |
| rand_read_256B.trace | 95.76 | 97.00 | +1.24 |
| rand_read_512B.trace | 97.85 | 99.19 | +1.34 |
| rand_read_64B.trace | 41.29 | 53.22 | +11.93 |
| rand_write_128B.trace | 76.31 | 92.05 | +15.74 |
| rand_write_256B.trace | 94.31 | 95.50 | +1.19 |
| rand_write_512B.trace | 96.71 | 99.20 | +2.49 |
| rand_write_64B.trace | 38.91 | 52.64 | +13.73 |
| seq_read_128B.trace | 97.17 | 97.17 | +0.00 |
| seq_read_256B.trace | 98.74 | 98.74 | +0.00 |
| seq_read_512B.trace | 99.19 | 99.19 | +0.00 |
| seq_read_64B.trace | 80.38 | 94.38 | +14.00 |
| seq_write_128B.trace | 97.22 | 97.22 | +0.00 |
| seq_write_256B.trace | 98.77 | 98.77 | +0.00 |
| seq_write_512B.trace | 99.20 | 99.20 | +0.00 |
| seq_write_64B.trace | 80.44 | 94.46 | +14.02 |

## LPDDR4-4266 (64-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 42.95 | 62.01 | +19.06 |
| rand_read_256B.trace | 78.07 | 87.81 | +9.74 |
| rand_read_512B.trace | 95.49 | 98.20 | +2.71 |
| rand_read_64B.trace | 41.29 | 53.22 | +11.93 |
| rand_write_128B.trace | 40.25 | 50.69 | +10.44 |
| rand_write_256B.trace | 74.54 | 89.74 | +15.20 |
| rand_write_512B.trace | 95.95 | 97.65 | +1.70 |
| rand_write_64B.trace | 38.91 | 52.64 | +13.73 |
| seq_read_128B.trace | 93.78 | 94.87 | +1.09 |
| seq_read_256B.trace | 97.86 | 97.86 | +0.00 |
| seq_read_512B.trace | 98.74 | 98.74 | +0.00 |
| seq_read_64B.trace | 80.38 | 94.38 | +14.00 |
| seq_write_128B.trace | 93.86 | 94.95 | +1.09 |
| seq_write_256B.trace | 97.91 | 97.91 | +0.00 |
| seq_write_512B.trace | 98.77 | 98.77 | +0.00 |
| seq_write_64B.trace | 80.44 | 94.46 | +14.02 |

## LPDDR4-6400 (16-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 89.59 | N/A | N/A |
| rand_read_256B.trace | 97.06 | N/A | N/A |
| rand_read_512B.trace | 98.26 | N/A | N/A |
| rand_read_64B.trace | 55.03 | N/A | N/A |
| rand_write_128B.trace | 87.94 | N/A | N/A |
| rand_write_256B.trace | 96.59 | N/A | N/A |
| rand_write_512B.trace | 97.10 | N/A | N/A |
| rand_write_64B.trace | 52.20 | N/A | N/A |
| seq_read_128B.trace | 97.60 | N/A | N/A |
| seq_read_256B.trace | 98.97 | N/A | N/A |
| seq_read_512B.trace | 99.30 | N/A | N/A |
| seq_read_64B.trace | 96.17 | N/A | N/A |
| seq_write_128B.trace | 97.65 | N/A | N/A |
| seq_write_256B.trace | 98.99 | N/A | N/A |
| seq_write_512B.trace | 99.31 | N/A | N/A |
| seq_write_64B.trace | 96.26 | N/A | N/A |

## LPDDR4-6400 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 57.34 | 83.60 | +26.26 |
| rand_read_256B.trace | 90.97 | 94.15 | +3.18 |
| rand_read_512B.trace | 97.22 | 98.38 | +1.16 |
| rand_read_64B.trace | 27.83 | 35.79 | +7.96 |
| rand_write_128B.trace | 54.17 | 67.83 | +13.66 |
| rand_write_256B.trace | 88.96 | 95.20 | +6.24 |
| rand_write_512B.trace | 96.14 | 98.99 | +2.85 |
| rand_write_64B.trace | 26.54 | 36.01 | +9.47 |
| seq_read_128B.trace | 96.32 | 96.32 | +0.00 |
| seq_read_256B.trace | 98.30 | 98.30 | +0.00 |
| seq_read_512B.trace | 98.97 | 98.97 | +0.00 |
| seq_read_64B.trace | 66.65 | 91.06 | +24.41 |
| seq_write_128B.trace | 96.41 | 96.41 | +0.00 |
| seq_write_256B.trace | 98.35 | 98.35 | +0.00 |
| seq_write_512B.trace | 98.99 | 98.99 | +0.00 |
| seq_write_64B.trace | 66.73 | 91.21 | +24.48 |

## LPDDR4-6400 (64-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 28.89 | 41.98 | +13.09 |
| rand_read_256B.trace | 55.77 | 75.14 | +19.37 |
| rand_read_512B.trace | 90.58 | 96.35 | +5.77 |
| rand_read_64B.trace | 27.83 | 35.79 | +7.96 |
| rand_write_128B.trace | 27.48 | 34.88 | +7.40 |
| rand_write_256B.trace | 52.49 | 66.23 | +13.74 |
| rand_write_512B.trace | 88.20 | 93.70 | +5.50 |
| rand_write_64B.trace | 26.54 | 36.01 | +9.47 |
| seq_read_128B.trace | 86.34 | 92.28 | +5.94 |
| seq_read_256B.trace | 97.00 | 97.00 | +0.00 |
| seq_read_512B.trace | 98.30 | 98.30 | +0.00 |
| seq_read_64B.trace | 66.65 | 91.06 | +24.41 |
| seq_write_128B.trace | 86.48 | 92.44 | +5.96 |
| seq_write_256B.trace | 97.09 | 97.09 | +0.00 |
| seq_write_512B.trace | 98.35 | 98.35 | +0.00 |
| seq_write_64B.trace | 66.73 | 91.21 | +24.48 |

## LPDDR5-6400 (16-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 89.59 | N/A | N/A |
| rand_read_256B.trace | 97.06 | N/A | N/A |
| rand_read_512B.trace | 98.26 | N/A | N/A |
| rand_read_64B.trace | 55.03 | N/A | N/A |
| rand_write_128B.trace | 87.94 | N/A | N/A |
| rand_write_256B.trace | 96.59 | N/A | N/A |
| rand_write_512B.trace | 97.10 | N/A | N/A |
| rand_write_64B.trace | 52.20 | N/A | N/A |
| seq_read_128B.trace | 97.60 | N/A | N/A |
| seq_read_256B.trace | 98.97 | N/A | N/A |
| seq_read_512B.trace | 99.30 | N/A | N/A |
| seq_read_64B.trace | 96.17 | N/A | N/A |
| seq_write_128B.trace | 97.65 | N/A | N/A |
| seq_write_256B.trace | 98.99 | N/A | N/A |
| seq_write_512B.trace | 99.31 | N/A | N/A |
| seq_write_64B.trace | 96.26 | N/A | N/A |

## LPDDR5-6400 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 57.34 | N/A | N/A |
| rand_read_256B.trace | 90.97 | N/A | N/A |
| rand_read_512B.trace | 97.22 | N/A | N/A |
| rand_read_64B.trace | 27.83 | N/A | N/A |
| rand_write_128B.trace | 54.17 | N/A | N/A |
| rand_write_256B.trace | 88.96 | N/A | N/A |
| rand_write_512B.trace | 96.14 | N/A | N/A |
| rand_write_64B.trace | 26.54 | N/A | N/A |
| seq_read_128B.trace | 96.32 | N/A | N/A |
| seq_read_256B.trace | 98.30 | N/A | N/A |
| seq_read_512B.trace | 98.97 | N/A | N/A |
| seq_read_64B.trace | 66.65 | N/A | N/A |
| seq_write_128B.trace | 96.41 | N/A | N/A |
| seq_write_256B.trace | 98.35 | N/A | N/A |
| seq_write_512B.trace | 98.99 | N/A | N/A |
| seq_write_64B.trace | 66.73 | N/A | N/A |

## LPDDR5-6400 (64-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 28.89 | N/A | N/A |
| rand_read_256B.trace | 55.77 | N/A | N/A |
| rand_read_512B.trace | 90.58 | N/A | N/A |
| rand_read_64B.trace | 27.83 | N/A | N/A |
| rand_write_128B.trace | 27.48 | N/A | N/A |
| rand_write_256B.trace | 52.49 | N/A | N/A |
| rand_write_512B.trace | 88.20 | N/A | N/A |
| rand_write_64B.trace | 26.54 | N/A | N/A |
| seq_read_128B.trace | 86.34 | N/A | N/A |
| seq_read_256B.trace | 97.00 | N/A | N/A |
| seq_read_512B.trace | 98.30 | N/A | N/A |
| seq_read_64B.trace | 66.65 | N/A | N/A |
| seq_write_128B.trace | 86.48 | N/A | N/A |
| seq_write_256B.trace | 97.09 | N/A | N/A |
| seq_write_512B.trace | 98.35 | N/A | N/A |
| seq_write_64B.trace | 66.73 | N/A | N/A |

## LPDDR5-8533 (16-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 81.17 | N/A | N/A |
| rand_read_256B.trace | 95.67 | N/A | N/A |
| rand_read_512B.trace | 97.86 | N/A | N/A |
| rand_read_64B.trace | 41.60 | N/A | N/A |
| rand_write_128B.trace | 77.17 | N/A | N/A |
| rand_write_256B.trace | 94.65 | N/A | N/A |
| rand_write_512B.trace | 97.27 | N/A | N/A |
| rand_write_64B.trace | 39.88 | N/A | N/A |
| seq_read_128B.trace | 97.17 | N/A | N/A |
| seq_read_256B.trace | 98.74 | N/A | N/A |
| seq_read_512B.trace | 99.19 | N/A | N/A |
| seq_read_64B.trace | 80.41 | N/A | N/A |
| seq_write_128B.trace | 97.23 | N/A | N/A |
| seq_write_256B.trace | 98.77 | N/A | N/A |
| seq_write_512B.trace | 99.20 | N/A | N/A |
| seq_write_64B.trace | 80.48 | N/A | N/A |

## LPDDR5-8533 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 43.17 | N/A | N/A |
| rand_read_256B.trace | 78.31 | N/A | N/A |
| rand_read_512B.trace | 95.62 | N/A | N/A |
| rand_read_64B.trace | 20.89 | N/A | N/A |
| rand_write_128B.trace | 41.25 | N/A | N/A |
| rand_write_256B.trace | 75.28 | N/A | N/A |
| rand_write_512B.trace | 96.11 | N/A | N/A |
| rand_write_64B.trace | 20.05 | N/A | N/A |
| seq_read_128B.trace | 93.90 | N/A | N/A |
| seq_read_256B.trace | 97.86 | N/A | N/A |
| seq_read_512B.trace | 98.74 | N/A | N/A |
| seq_read_64B.trace | 49.14 | N/A | N/A |
| seq_write_128B.trace | 94.00 | N/A | N/A |
| seq_write_256B.trace | 97.92 | N/A | N/A |
| seq_write_512B.trace | 98.77 | N/A | N/A |
| seq_write_64B.trace | 49.19 | N/A | N/A |

## LPDDR5-8533 (64-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 21.66 | N/A | N/A |
| rand_read_256B.trace | 42.04 | N/A | N/A |
| rand_read_512B.trace | 82.08 | N/A | N/A |
| rand_read_64B.trace | 20.89 | N/A | N/A |
| rand_write_128B.trace | 20.75 | N/A | N/A |
| rand_write_256B.trace | 39.88 | N/A | N/A |
| rand_write_512B.trace | 74.05 | N/A | N/A |
| rand_write_64B.trace | 20.05 | N/A | N/A |
| seq_read_128B.trace | 63.25 | N/A | N/A |
| seq_read_256B.trace | 95.69 | N/A | N/A |
| seq_read_512B.trace | 97.86 | N/A | N/A |
| seq_read_64B.trace | 49.14 | N/A | N/A |
| seq_write_128B.trace | 63.35 | N/A | N/A |
| seq_write_256B.trace | 95.80 | N/A | N/A |
| seq_write_512B.trace | 97.92 | N/A | N/A |
| seq_write_64B.trace | 49.19 | N/A | N/A |
