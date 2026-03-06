# DRAM Simulator basic100 Benchmark Results (QD=16 vs QD=64)
Configuration: `configs/LP4_32_cfg.json`

| Trace File | Metric | QD=16 | QD=64 | Difference |
| --- | --- | --- | --- | --- |
| **rand_read_128B.trace** | Total Cycles | 1443 | 1359 | -84 |
|  | Bandwidth (GB/s) | 28.39 | 30.14 | +1.75 |
|  | Utilization (%) | 55.44 | 58.87 | +3.43 |
|  | Avg Queue Depth | 14.82 | 42.19 | +27.37 |
| **rand_read_256B.trace** | Total Cycles | 2134 | 2070 | -64 |
|  | Bandwidth (GB/s) | 38.39 | 39.57 | +1.18 |
|  | Utilization (%) | 74.98 | 77.29 | +2.31 |
|  | Avg Queue Depth | 15.05 | 45.98 | +30.93 |
| **rand_read_512B.trace** | Total Cycles | 3640 | 3648 | +8 |
|  | Bandwidth (GB/s) | 45.01 | 44.91 | -0.10 |
|  | Utilization (%) | 87.91 | 87.72 | -0.19 |
|  | Avg Queue Depth | 15.24 | 48.13 | +32.89 |
| **rand_write_128B.trace** | Total Cycles | 1694 | 1653 | -41 |
|  | Bandwidth (GB/s) | 24.18 | 24.78 | +0.60 |
|  | Utilization (%) | 47.23 | 48.40 | +1.17 |
|  | Avg Queue Depth | 14.78 | 40.77 | +25.99 |
| **rand_write_256B.trace** | Total Cycles | 1918 | 1980 | +62 |
|  | Bandwidth (GB/s) | 42.71 | 41.37 | -1.34 |
|  | Utilization (%) | 83.42 | 80.81 | -2.61 |
|  | Avg Queue Depth | 14.88 | 47.21 | +32.33 |
| **rand_write_512B.trace** | Total Cycles | 3781 | 3600 | -181 |
|  | Bandwidth (GB/s) | 43.33 | 45.51 | +2.18 |
|  | Utilization (%) | 84.63 | 88.89 | +4.26 |
|  | Avg Queue Depth | 14.92 | 48.72 | +33.80 |
| **sample.trace** | Total Cycles | 190 | 190 | +0 |
|  | Bandwidth (GB/s) | 5.39 | 5.39 | +0.00 |
|  | Utilization (%) | 21.05 | 21.05 | +0.00 |
|  | Avg Queue Depth | 2.67 | 2.67 | +0.00 |
| **seq_read_128B.trace** | Total Cycles | 952 | 952 | +0 |
|  | Bandwidth (GB/s) | 43.03 | 43.03 | +0.00 |
|  | Utilization (%) | 84.03 | 84.03 | +0.00 |
|  | Avg Queue Depth | 14.43 | 42.94 | +28.51 |
| **seq_read_256B.trace** | Total Cycles | 1784 | 1784 | +0 |
|  | Bandwidth (GB/s) | 45.92 | 45.92 | +0.00 |
|  | Utilization (%) | 89.69 | 89.69 | +0.00 |
|  | Avg Queue Depth | 14.42 | 42.94 | +28.52 |
| **seq_read_512B.trace** | Total Cycles | 3320 | 3320 | +0 |
|  | Bandwidth (GB/s) | 49.35 | 49.35 | +0.00 |
|  | Utilization (%) | 96.39 | 96.39 | +0.00 |
|  | Avg Queue Depth | 14.94 | 45.28 | +30.34 |
| **seq_read_64B.trace** | Total Cycles | 863 | 624 | -239 |
|  | Bandwidth (GB/s) | 23.73 | 32.82 | +9.09 |
|  | Utilization (%) | 46.35 | 64.10 | +17.75 |
|  | Avg Queue Depth | 14.85 | 43.96 | +29.11 |
| **seq_write_128B.trace** | Total Cycles | 948 | 948 | +0 |
|  | Bandwidth (GB/s) | 43.21 | 43.21 | +0.00 |
|  | Utilization (%) | 84.39 | 84.39 | +0.00 |
|  | Avg Queue Depth | 14.43 | 42.94 | +28.51 |
| **seq_write_256B.trace** | Total Cycles | 1780 | 1780 | +0 |
|  | Bandwidth (GB/s) | 46.02 | 46.02 | +0.00 |
|  | Utilization (%) | 89.89 | 89.89 | +0.00 |
|  | Avg Queue Depth | 14.42 | 42.94 | +28.52 |
| **seq_write_512B.trace** | Total Cycles | 3316 | 3316 | +0 |
|  | Bandwidth (GB/s) | 49.41 | 49.41 | +0.00 |
|  | Utilization (%) | 96.50 | 96.50 | +0.00 |
|  | Avg Queue Depth | 14.94 | 45.28 | +30.34 |
| **seq_write_64B.trace** | Total Cycles | 859 | 620 | -239 |
|  | Bandwidth (GB/s) | 23.84 | 33.03 | +9.19 |
|  | Utilization (%) | 46.57 | 64.52 | +17.95 |
|  | Avg Queue Depth | 14.85 | 43.96 | +29.11 |
