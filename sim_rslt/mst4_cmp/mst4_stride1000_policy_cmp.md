# Policy Comparison: FIFO vs PageHitFirst (Stride 0x1000)

**Trace**: `mst4_4KB_stride1000_read.trace` (4 Masters Interleaved, 4KB bursts, Stride=4KB)
**Config**: `LP4_4266_64_cfg.json`, `mapping_2ch.json`
**Queue Depth**: 64

| Metric | FIFO | PageHitFirst | 差異 (Diff) |
| --- | --- | --- | --- |
| **Cycles** | 17082 | 17219 | +137 |
| **Bandwidth** | 65.47 | 64.95 | -0.52 |
| **Utilization** | 95.91 | 95.15 | -0.76 |
| **Hits** | 0 | 0 | +0 |
| **Misses** | 24 | 24 | +0 |
| **Conflicts** | 488 | 488 | +0 |

## 深度分析與結論 (Deep Analysis & Conclusion)
即使我們將 Stride 從 `0x2000` (8KB) 降到 `0x1000` (4KB) 以確保同一個 Master 的連續請求落在同一個 Row ($32$ KB) 內，**結果依然是 0 Hits，`PageHitFirst` 完全無法發揮作用**。這揭示了多核心交錯存取在排程與 Address Mapping 上的深層瓶頸：

### 1. 致命的 Bank 乒乓效應 (Ping-Pong Effect)
根據 `mapping_2ch.json`，Bank 由 Bits 15~17 決定，Row 則由 Bits 18 以上決定。各 Master 的 Base Address 導致了以下映射：
- Mst-0 (`0x00000`): **`Bank 0, Row 0`**
- Mst-1 (`0x20000`): `Bank 4, Row 0`
- Mst-2 (`0x40000`): **`Bank 0, Row 1`**  (與 Mst-0 衝突！)
- Mst-3 (`0x60000`): `Bank 4, Row 1`  (與 Mst-1 衝突！)

Mst-0 和 Mst-2 都映射到 `Bank 0`，但分別需要打開不同的 `Row 0` 和 `Row 1`。當 Mst-0 使用完 Row 0 後，Mst-2 的請求迫使控制器執行 PRE (關閉 Row 0) 並 ACT (打開 Row 1)。

### 2. 為什麼 Queue Depth=64 和 PageHitFirst 救不回來？
在 Round-Robin 發射機制下，指令進入 Queue 的順序是：`M0_1st -> M1_1st -> M2_1st -> M3_1st -> M0_2nd ...`。
雖然 M0_2nd (`0x01000`) 與 M0_1st 位於相同的 `Bank 0, Row 0`，且 Queue Depth 足夠深 (64) 以同時容納它們，但 **M2_1st** 卡在它們中間。當 M0_1st 執行完畢，Bank 0 處於空閒，排程器看到排在前面的 M2_1st 已經準備好，就讓它去打開了 `Row 1`。
等到排程器掃描到後面的 M0_2nd 發現它是 `Row 0` 時，Bank 0 的狀態已經被 M2_1st 給破壞了。因此，它無法形成 Hit，只能被迫再次 PRE+ACT。這證明了在惡意的 Address Pattern 之下，只要競爭對手的請求先被服務並改變了 Bank 狀態，`PageHitFirst` 策略也無法挽救被洗掉的 Row，效能將無可避免地退化為高 Conflict 的低效模式。

### 3. 違反直覺的極高 Utilization：完美的 Latency Hiding (時間隱藏)
在上述分析中，我們確認了 0 Hits 與大量 Conflicts 的存在。一般而言，頻繁的 PRE 與 ACT 會帶來嚴重的效能懲罰，使 Data Bus 大量空轉。然而，測試結果中的 **Utilization 卻高達 95% 以上**！
透過 Pipeline 視覺化腳本 (`analyze_pipeline.py`) 追蹤指令發射時序，我們找出了根本原因：
- **傳輸時間極長**：Trace 發送的區塊 (Chunk) 是 **1KB**。在 LPDDR4-4266 **x64** 架構下 (每 Cycle 傳輸 16 Bytes)，傳輸 1KB 需要連續霸佔 Data Bus 高達 **64 個 Cycles**。
- **背景冷卻時間被完全隱藏**：DRAM 發生 Conflict 時，最痛的是必須等待 `tRP` (PRE) + `tRCD` (ACT) 才能傳資料。但這 64 Cycles 的超長傳輸時間，給了**其他 Bank 非常充裕的時間在背景默默完成 PRE 與 ACT** 的冷卻動作。
- 當目前 Bank 的 64 Cycles 資料一傳完，下一個 Bank 早就已經準備好資料了！因此 Data Bus 從頭到尾都沒有斷掉，達到了「無縫接軌」的完美時間隱藏效應 (Latency Hiding)。這就是為什麼在充滿 Conflict 的惡劣條件下，只要 Request 夠大，系統依舊能跑到 95%+ 的超高利用率。
