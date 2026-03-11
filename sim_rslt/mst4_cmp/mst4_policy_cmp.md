# Policy Comparison: FIFO vs PageHitFirst

**Trace**: `mst4_4KB_read.trace` (4 Masters Interleaved, 4KB bursts)
**Config**: `LP4_4266_64_cfg.json`, `mapping_2ch.json`
**Queue Depth**: 64

| Metric | FIFO | PageHitFirst | 差異 (Diff) |
| --- | --- | --- | --- |
| **Cycles** | 16464 | 16464 | +0 |
| **Bandwidth** | 67.92 | 67.92 | +0.00 |
| **Utilization** | 99.51 | 99.51 | +0.00 |
| **Hits** | 0 | 0 | +0 |
| **Misses** | 32 | 32 | +0 |
| **Conflicts** | 480 | 480 | +0 |

## 深度分析與結論 (Deep Analysis & Conclusion)
### 1. 單筆 4KB 巨量請求的盲點與 Mapping-Aware Chunking
最初，我們將 4KB 直接當作一筆 AXI Request 餵給模擬器。但因為 2CH 的 Mapping 在 1KB 邊界就會切換 Channel，導致模擬器無法將資料交錯，強迫它在單一 Bank 內完成，造成效能失真。修改 `gen_mst4stream.py` 導入「Mapping-Aware Chunking (映射感知切割)」後，4KB 被正確切成 4 筆 1KB 的 Transaction，完美模擬了真實硬體的分流。

### 2. 為什麼 Hit 率仍然是 0？(教科書等級的 Ping-Pong Effect)
即使切碎了 1KB，結果卻顯示 `FIFO` 與 `PageHitFirst` 效能一模一樣 (Hits=0, Conflicts=480)。這源自於 Master Start Address 與 Stride 的特殊組合，觸發了嚴重的 **Bank 乒乓效應 (Thrashing)**：
- 根據 `mapping_2ch.json`：`Bank` 是 Bits 15~17 (即每 32KB 換 Bank)，而 `Row` 是 Bits 18 以上 (即每 256KB 換 Row)。
- **Mst-0 (0x00000)** 映射到 `Bank 0, Row 0`。
- **Mst-1 (0x20000)** 映射到 `Bank 4, Row 0` (互不干擾)。
- **Mst-2 (0x40000 = 256KB)** 映射到 **`Bank 0, Row 1`**。
- **Mst-3 (0x60000)** 映射到 **`Bank 4, Row 1`**。

當 Round-Robin 交錯發送時，Mst-0 剛打開 `Bank 0` 的 `Row 0`，緊接著 Mst-2 就強迫 `Bank 0` 關閉 `Row 0` 並打開 `Row 1`。下一輪，Mst-0 又要存取 `Bank 0` 時，又得把 `Row 1` 關掉換回 `Row 0`。不同 Master 瘋狂覆蓋彼此在同一個 Bank 上的 Row 狀態，導致無盡的 Conflicts。

### 3. PageHitFirst 為何救不回來？
因為 `stride = 0x2000` (8KB)。當 Mst-0 發出下一筆時，位址跳躍了 8KB。在 4 個 Master 交錯的情況下，各個 Channel 的 Queue 裡面充滿了來自不同 Row 的散落請求。排程器找不到任何連續且位址相同的 Row 可以進行 Hit 合併，最終退化成與 FIFO 相同的排程結果，Utilization 停留在 99% 只是因為資料量小且匯流排忙碌而已。
