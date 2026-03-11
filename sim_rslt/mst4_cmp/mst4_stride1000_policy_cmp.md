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
