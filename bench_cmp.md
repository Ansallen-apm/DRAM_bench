# DRAM Simulator Benchmark Utilization Comparison (QD=16 vs QD=64)
This file compares the Utilization (%) between the default Queue Depth 16 (`BENCHMARK_RESULTS.md`) and Queue Depth 64 (`bench_rslt.md`).


## LPDDR4-4266 (16-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 94.31 | 94.93 | +0.62 |
| rand_read_256B.trace | 97.43 | 97.43 | +0.00 |
| rand_read_512B.trace | 98.40 | 99.26 | +0.86 |
| rand_read_64B.trace | 78.14 | 94.62 | +16.48 |
| rand_write_128B.trace | 93.83 | 96.88 | +3.05 |
| rand_write_256B.trace | 96.50 | 96.44 | -0.06 |
| rand_write_512B.trace | 96.80 | 99.02 | +2.22 |
| rand_write_64B.trace | 72.55 | 90.82 | +18.27 |
| seq_read_128B.trace | 98.04 | 98.04 | +0.00 |
| seq_read_256B.trace | 99.19 | 99.19 | +0.00 |
| seq_read_512B.trace | 99.41 | 99.41 | +0.00 |
| seq_read_64B.trace | 97.17 | 97.17 | +0.00 |
| seq_write_128B.trace | 98.06 | 98.06 | +0.00 |
| seq_write_256B.trace | 99.20 | 99.20 | +0.00 |
| seq_write_512B.trace | 99.42 | 99.42 | +0.00 |
| seq_write_64B.trace | 97.22 | 97.22 | +0.00 |

## LPDDR4-4266 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 80.73 | 93.98 | +13.25 |
| rand_read_256B.trace | 95.76 | 96.96 | +1.20 |
| rand_read_512B.trace | 97.85 | 99.18 | +1.33 |
| rand_read_64B.trace | 41.29 | 53.19 | +11.90 |
| rand_write_128B.trace | 76.31 | 89.58 | +13.27 |
| rand_write_256B.trace | 94.31 | 95.88 | +1.57 |
| rand_write_512B.trace | 96.71 | 99.19 | +2.48 |
| rand_write_64B.trace | 38.91 | 52.61 | +13.70 |
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
| rand_read_128B.trace | 42.95 | 62.02 | +19.07 |
| rand_read_256B.trace | 78.07 | 87.91 | +9.84 |
| rand_read_512B.trace | 95.49 | 97.95 | +2.46 |
| rand_read_64B.trace | 41.29 | 53.19 | +11.90 |
| rand_write_128B.trace | 40.25 | 50.45 | +10.20 |
| rand_write_256B.trace | 74.54 | 89.96 | +15.42 |
| rand_write_512B.trace | 95.95 | 97.81 | +1.86 |
| rand_write_64B.trace | 38.91 | 52.61 | +13.70 |
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
| rand_read_128B.trace | 89.59 | 94.54 | +4.95 |
| rand_read_256B.trace | 97.06 | 97.21 | +0.15 |
| rand_read_512B.trace | 98.26 | 99.30 | +1.04 |
| rand_read_64B.trace | 55.03 | 71.28 | +16.25 |
| rand_write_128B.trace | 87.94 | 95.93 | +7.99 |
| rand_write_256B.trace | 96.59 | 96.44 | -0.15 |
| rand_write_512B.trace | 97.10 | 99.29 | +2.19 |
| rand_write_64B.trace | 52.20 | 70.50 | +18.30 |
| seq_read_128B.trace | 97.60 | 97.60 | +0.00 |
| seq_read_256B.trace | 98.97 | 98.97 | +0.00 |
| seq_read_512B.trace | 99.30 | 99.30 | +0.00 |
| seq_read_64B.trace | 96.17 | 96.32 | +0.15 |
| seq_write_128B.trace | 97.65 | 97.65 | +0.00 |
| seq_write_256B.trace | 98.99 | 98.99 | +0.00 |
| seq_write_512B.trace | 99.31 | 99.31 | +0.00 |
| seq_write_64B.trace | 96.26 | 96.41 | +0.15 |

## LPDDR4-6400 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 57.34 | 83.62 | +26.28 |
| rand_read_256B.trace | 90.97 | 94.27 | +3.30 |
| rand_read_512B.trace | 97.22 | 98.36 | +1.14 |
| rand_read_64B.trace | 27.83 | 35.77 | +7.94 |
| rand_write_128B.trace | 54.17 | 67.85 | +13.68 |
| rand_write_256B.trace | 88.96 | 94.56 | +5.60 |
| rand_write_512B.trace | 96.14 | 98.34 | +2.20 |
| rand_write_64B.trace | 26.54 | 35.99 | +9.45 |
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
| rand_read_128B.trace | 28.89 | 41.87 | +12.98 |
| rand_read_256B.trace | 55.77 | 77.55 | +21.78 |
| rand_read_512B.trace | 90.58 | 96.09 | +5.51 |
| rand_read_64B.trace | 27.83 | 35.77 | +7.94 |
| rand_write_128B.trace | 27.48 | 34.83 | +7.35 |
| rand_write_256B.trace | 52.49 | 66.23 | +13.74 |
| rand_write_512B.trace | 88.20 | 93.76 | +5.56 |
| rand_write_64B.trace | 26.54 | 35.99 | +9.45 |
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
| rand_read_128B.trace | 89.59 | 94.54 | +4.95 |
| rand_read_256B.trace | 97.06 | 97.21 | +0.15 |
| rand_read_512B.trace | 98.26 | 99.30 | +1.04 |
| rand_read_64B.trace | 55.03 | 71.28 | +16.25 |
| rand_write_128B.trace | 87.94 | 95.93 | +7.99 |
| rand_write_256B.trace | 96.59 | 96.44 | -0.15 |
| rand_write_512B.trace | 97.10 | 99.29 | +2.19 |
| rand_write_64B.trace | 52.20 | 70.50 | +18.30 |
| seq_read_128B.trace | 97.60 | 97.60 | +0.00 |
| seq_read_256B.trace | 98.97 | 98.97 | +0.00 |
| seq_read_512B.trace | 99.30 | 99.30 | +0.00 |
| seq_read_64B.trace | 96.17 | 96.32 | +0.15 |
| seq_write_128B.trace | 97.65 | 97.65 | +0.00 |
| seq_write_256B.trace | 98.99 | 98.99 | +0.00 |
| seq_write_512B.trace | 99.31 | 99.31 | +0.00 |
| seq_write_64B.trace | 96.26 | 96.41 | +0.15 |

## LPDDR5-6400 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 57.34 | 83.62 | +26.28 |
| rand_read_256B.trace | 90.97 | 94.27 | +3.30 |
| rand_read_512B.trace | 97.22 | 98.36 | +1.14 |
| rand_read_64B.trace | 27.83 | 35.77 | +7.94 |
| rand_write_128B.trace | 54.17 | 67.85 | +13.68 |
| rand_write_256B.trace | 88.96 | 94.56 | +5.60 |
| rand_write_512B.trace | 96.14 | 98.34 | +2.20 |
| rand_write_64B.trace | 26.54 | 35.99 | +9.45 |
| seq_read_128B.trace | 96.32 | 96.32 | +0.00 |
| seq_read_256B.trace | 98.30 | 98.30 | +0.00 |
| seq_read_512B.trace | 98.97 | 98.97 | +0.00 |
| seq_read_64B.trace | 66.65 | 91.06 | +24.41 |
| seq_write_128B.trace | 96.41 | 96.41 | +0.00 |
| seq_write_256B.trace | 98.35 | 98.35 | +0.00 |
| seq_write_512B.trace | 98.99 | 98.99 | +0.00 |
| seq_write_64B.trace | 66.73 | 91.21 | +24.48 |

## LPDDR5-6400 (64-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 28.89 | 41.87 | +12.98 |
| rand_read_256B.trace | 55.77 | 77.55 | +21.78 |
| rand_read_512B.trace | 90.58 | 96.09 | +5.51 |
| rand_read_64B.trace | 27.83 | 35.77 | +7.94 |
| rand_write_128B.trace | 27.48 | 34.83 | +7.35 |
| rand_write_256B.trace | 52.49 | 66.23 | +13.74 |
| rand_write_512B.trace | 88.20 | 93.76 | +5.56 |
| rand_write_64B.trace | 26.54 | 35.99 | +9.45 |
| seq_read_128B.trace | 86.34 | 92.28 | +5.94 |
| seq_read_256B.trace | 97.00 | 97.00 | +0.00 |
| seq_read_512B.trace | 98.30 | 98.30 | +0.00 |
| seq_read_64B.trace | 66.65 | 91.06 | +24.41 |
| seq_write_128B.trace | 86.48 | 92.44 | +5.96 |
| seq_write_256B.trace | 97.09 | 97.09 | +0.00 |
| seq_write_512B.trace | 98.35 | 98.35 | +0.00 |
| seq_write_64B.trace | 66.73 | 91.21 | +24.48 |

## LPDDR5-8533 (16-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 81.17 | 94.11 | +12.94 |
| rand_read_256B.trace | 95.67 | 97.00 | +1.33 |
| rand_read_512B.trace | 97.86 | 99.07 | +1.21 |
| rand_read_64B.trace | 41.60 | 53.47 | +11.87 |
| rand_write_128B.trace | 77.17 | 92.19 | +15.02 |
| rand_write_256B.trace | 94.65 | 95.29 | +0.64 |
| rand_write_512B.trace | 97.27 | 99.20 | +1.93 |
| rand_write_64B.trace | 39.88 | 54.05 | +14.17 |
| seq_read_128B.trace | 97.17 | 97.17 | +0.00 |
| seq_read_256B.trace | 98.74 | 98.74 | +0.00 |
| seq_read_512B.trace | 99.19 | 99.19 | +0.00 |
| seq_read_64B.trace | 80.41 | 94.38 | +13.97 |
| seq_write_128B.trace | 97.23 | 97.23 | +0.00 |
| seq_write_256B.trace | 98.77 | 98.77 | +0.00 |
| seq_write_512B.trace | 99.20 | 99.20 | +0.00 |
| seq_write_64B.trace | 80.48 | 94.48 | +14.00 |

## LPDDR5-8533 (32-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 43.17 | 62.46 | +19.29 |
| rand_read_256B.trace | 78.31 | 88.45 | +10.14 |
| rand_read_512B.trace | 95.62 | 97.64 | +2.02 |
| rand_read_64B.trace | 20.89 | 26.82 | +5.93 |
| rand_write_128B.trace | 41.25 | 52.06 | +10.81 |
| rand_write_256B.trace | 75.28 | 89.76 | +14.48 |
| rand_write_512B.trace | 96.11 | 98.38 | +2.27 |
| rand_write_64B.trace | 20.05 | 27.28 | +7.23 |
| seq_read_128B.trace | 93.90 | 94.87 | +0.97 |
| seq_read_256B.trace | 97.86 | 97.86 | +0.00 |
| seq_read_512B.trace | 98.74 | 98.74 | +0.00 |
| seq_read_64B.trace | 49.14 | 69.89 | +20.75 |
| seq_write_128B.trace | 94.00 | 94.97 | +0.97 |
| seq_write_256B.trace | 97.92 | 97.92 | +0.00 |
| seq_write_512B.trace | 98.77 | 98.77 | +0.00 |
| seq_write_64B.trace | 49.19 | 70.00 | +20.81 |

## LPDDR5-8533 (64-bit)

| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |
| --- | --- | --- | --- |
| rand_read_128B.trace | 21.66 | 31.37 | +9.71 |
| rand_read_256B.trace | 42.04 | 61.57 | +19.53 |
| rand_read_512B.trace | 82.08 | 95.54 | +13.46 |
| rand_read_64B.trace | 20.89 | 26.82 | +5.93 |
| rand_write_128B.trace | 20.75 | 26.25 | +5.50 |
| rand_write_256B.trace | 39.88 | 50.03 | +10.15 |
| rand_write_512B.trace | 74.05 | 85.75 | +11.70 |
| rand_write_64B.trace | 20.05 | 27.28 | +7.23 |
| seq_read_128B.trace | 63.25 | 73.33 | +10.08 |
| seq_read_256B.trace | 95.69 | 95.78 | +0.09 |
| seq_read_512B.trace | 97.86 | 97.86 | +0.00 |
| seq_read_64B.trace | 49.14 | 69.89 | +20.75 |
| seq_write_128B.trace | 63.35 | 73.46 | +10.11 |
| seq_write_256B.trace | 95.80 | 95.88 | +0.08 |
| seq_write_512B.trace | 97.92 | 97.92 | +0.00 |
| seq_write_64B.trace | 49.19 | 70.00 | +20.81 |
