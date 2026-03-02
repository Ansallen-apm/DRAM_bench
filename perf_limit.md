# DRAM Simulator 效能極限分析 (20k 交易壓力測試)

本報告基於 `traces/perf_limit/` 目錄下的大型 Trace 檔案 (每檔 20,000 筆交易)，在雙通道 (`mapping_2ch.json`) 架構下，分析 LPDDR4-6400 與 LPDDR5-6400 在不同匯流排寬度 (16-bit, 32-bit, 64-bit) 下的效能表現。

## 核心觀察與分析

### 1. 循序存取 (Sequential Access) 的頻寬天花板
在循序存取的負載下 (例如 `seq_read_256B.trace`)，Page Hit Rate 極高，記憶體能夠以最高效率運作。
*   **16-bit 雙通道**: 理論頻寬為 25.6 GB/s。模擬結果顯示 **25.60 GB/s**，達到 99.98% 利用率。
*   **32-bit 雙通道**: 理論頻寬為 51.2 GB/s。模擬結果顯示 **51.18 GB/s**，達到 99.96% 利用率。
*   **64-bit 雙通道**: 理論頻寬為 102.4 GB/s。模擬結果顯示 **101.47 GB/s**，達到 99.09% 利用率。
*   **結論**: 模擬器正確地反映了通道數量與匯流排寬度對極限頻寬的線性縮放能力。

### 2. 隨機存取 (Random Access) 的效能瓶頸
在隨機存取負載下 (例如 `rand_read_128B.trace`)，由於 Page Miss 與 Conflict 頻繁發生，DRAM 必須花費大量時間執行 PRE (預充充電) 和 ACT (行啟動) 指令，導致實際頻寬大幅低於理論極限。
*   **16-bit 架構**: 雖然傳輸時間長，但剛好掩蓋了部分時序開銷，Utilization 仍能維持在 91% 左右。
*   **64-bit 架構**: 傳輸資料極快 (Burst 時間短)，導致資料匯流排經常處於閒置狀態等待下一個 ACT 指令完成。在 `rand_read_128B` 下，Utilization 僅剩 **30.25%**，實際頻寬約為 **30.97 GB/s** (遠低於 102.4 GB/s 的極限)。

### 3. 過度抓取 (Overfetching) 現象
在 64-bit 架構下 (單一 Channel 寬度為 8 Bytes，Prefetch 16)，一次最小的 Burst 會讀取/寫入 128 Bytes。
*   當我們執行 `128B` 的 trace 時，Utilization 為 30.25%。
*   當我們執行 `256B` 的 trace 時，因為單次請求資料量變大，攤平了時序開銷，Utilization 提升至 59.70%，頻寬提升至 **61.14 GB/s**。
這證實了在寬匯流排架構下，若存取粒度過小，會造成嚴重的頻寬浪費與利用率低下。

---

## 詳細模擬結果

### LPDDR4-6400 (16-bit)
| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 349197 | 23.46 | 91.64 | 16.00 | 5 | 33 | 19962 |
| rand_read_256B.trace | 663216 | 24.70 | 96.50 | 16.00 | 1 | 33 | 19966 |
| rand_write_128B.trace | 363425 | 22.54 | 88.05 | 16.00 | 3 | 32 | 19965 |
| rand_write_256B.trace | 663293 | 24.70 | 96.49 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 320120 | 25.59 | 99.96 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 640120 | 25.60 | 99.98 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 320116 | 25.59 | 99.96 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 640116 | 25.60 | 99.98 | 15.99 | 19372 | 32 | 596 |

### LPDDR4-6400 (32-bit)
| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 266809 | 30.70 | 59.97 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 346688 | 47.26 | 92.30 | 16.00 | 2 | 32 | 19966 |
| rand_write_128B.trace | 307389 | 26.65 | 52.05 | 16.00 | 4 | 32 | 19964 |
| rand_write_256B.trace | 364175 | 44.99 | 87.87 | 16.00 | 2 | 32 | 19966 |
| seq_read_128B.trace | 162827 | 50.31 | 98.26 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 320120 | 51.18 | 99.96 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 162823 | 50.31 | 98.27 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 320116 | 51.18 | 99.96 | 15.99 | 19372 | 32 | 596 |

### LPDDR4-6400 (64-bit)
| Trace File | Total Cycles | Bandwidth (GB/s) | Utilization (%) | Avg Queue Depth | Page Hits | Page Misses | Page Conflicts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 264501 | 30.97 | 30.25 | 16.00 | 6 | 32 | 19962 |
| rand_read_256B.trace | 267990 | 61.14 | 59.70 | 15.99 | 2 | 32 | 19966 |
| rand_write_128B.trace | 304209 | 26.93 | 26.30 | 15.99 | 4 | 32 | 19964 |
| rand_write_256B.trace | 308898 | 53.04 | 51.80 | 15.99 | 2 | 32 | 19966 |
| seq_read_128B.trace | 93494 | 87.62 | 85.57 | 15.99 | 19684 | 32 | 284 |
| seq_read_256B.trace | 161477 | 101.46 | 99.09 | 15.99 | 19372 | 32 | 596 |
| seq_write_128B.trace | 93490 | 87.62 | 85.57 | 15.99 | 19684 | 32 | 284 |
| seq_write_256B.trace | 161473 | 101.47 | 99.09 | 15.99 | 19372 | 32 | 596 |

*(註：由於 LPDDR4 與 LPDDR5 於 6400MHz 的核心時序配置在本次測試中被設定為相同，其效能數據亦完全一致，故在此省略重複的 LPDDR5 表格。)*