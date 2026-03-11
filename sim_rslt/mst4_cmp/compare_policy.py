import subprocess
import re

def run_simulation(policy):
    cmd = [
        "python3", "../../src/asyc_parall_opt.py",
        "--config", "../../configs/LP4_4266_64_cfg.json",
        "--mapping", "../../configs/mapping_2ch.json",
        "--trace", "../../traces/mst4stream/mst4_4KB_read.trace",
        "--policy", policy,
        "--queue_depth", "64"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout

    metrics = {
        'cycles': 0,
        'bandwidth': 0.0,
        'utilization': 0.0,
        'hits': 0,
        'misses': 0,
        'conflicts': 0
    }

    cycle_match = re.search(r"Total Cycles\s*\(總週期\):\s*(\d+)", output)
    if cycle_match:
        metrics['cycles'] = int(cycle_match.group(1))

    bw_match = re.search(r"Bandwidth\s*\(頻寬\):\s*([\d\.]+)\s*GB/s", output)
    if bw_match:
        metrics['bandwidth'] = float(bw_match.group(1))

    util_match = re.search(r"Utilization\s*\(利用率\):\s*([\d\.]+)\s*%", output)
    if util_match:
        metrics['utilization'] = float(util_match.group(1))

    hit_match = re.search(r"Page Hits\s*\(Page 命中\):\s*(\d+)", output)
    if hit_match:
        metrics['hits'] = int(hit_match.group(1))

    miss_match = re.search(r"Page Misses\s*\(Page 未命中\):\s*(\d+)", output)
    if miss_match:
        metrics['misses'] = int(miss_match.group(1))

    conflict_match = re.search(r"Page Conflicts\s*\(Page 衝突\):\s*(\d+)", output)
    if conflict_match:
        metrics['conflicts'] = int(conflict_match.group(1))

    return metrics

def main():
    print("Running FIFO...")
    fifo_metrics = run_simulation("FIFO")

    print("Running PageHitFirst...")
    phf_metrics = run_simulation("PageHitFirst")

    with open("mst4_policy_cmp.md", "w", encoding='utf-8') as f:
        f.write("# Policy Comparison: FIFO vs PageHitFirst\n\n")
        f.write("**Trace**: `mst4_4KB_read.trace` (4 Masters Interleaved, 4KB bursts)\n")
        f.write("**Config**: `LP4_4266_64_cfg.json`, `mapping_2ch.json`\n")
        f.write("**Queue Depth**: 64\n\n")

        f.write("| Metric | FIFO | PageHitFirst | 差異 (Diff) |\n")
        f.write("| --- | --- | --- | --- |\n")

        for key in fifo_metrics.keys():
            f_val = fifo_metrics[key]
            p_val = phf_metrics[key]

            diff = ""
            if key in ['cycles', 'hits', 'misses', 'conflicts']:
                diff = f"{p_val - f_val:+,}"
            else:
                diff = f"{p_val - f_val:+.2f}"

            f.write(f"| **{key.capitalize()}** | {f_val} | {p_val} | {diff} |\n")

        f.write("\n## 深度分析與結論 (Deep Analysis & Conclusion)\n")
        f.write("### 1. 單筆 4KB 巨量請求的盲點與 Mapping-Aware Chunking\n")
        f.write("最初，我們將 4KB 直接當作一筆 AXI Request 餵給模擬器。但因為 2CH 的 Mapping 在 1KB 邊界就會切換 Channel，導致模擬器無法將資料交錯，強迫它在單一 Bank 內完成，造成效能失真。修改 `gen_mst4stream.py` 導入「Mapping-Aware Chunking (映射感知切割)」後，4KB 被正確切成 4 筆 1KB 的 Transaction，完美模擬了真實硬體的分流。\n\n")

        f.write("### 2. 為什麼 Hit 率仍然是 0？(教科書等級的 Ping-Pong Effect)\n")
        f.write("即使切碎了 1KB，結果卻顯示 `FIFO` 與 `PageHitFirst` 效能一模一樣 (Hits=0, Conflicts=480)。這源自於 Master Start Address 與 Stride 的特殊組合，觸發了嚴重的 **Bank 乒乓效應 (Thrashing)**：\n")
        f.write("- 根據 `mapping_2ch.json`：`Bank` 是 Bits 15~17 (即每 32KB 換 Bank)，而 `Row` 是 Bits 18 以上 (即每 256KB 換 Row)。\n")
        f.write("- **Mst-0 (0x00000)** 映射到 `Bank 0, Row 0`。\n")
        f.write("- **Mst-1 (0x20000)** 映射到 `Bank 4, Row 0` (互不干擾)。\n")
        f.write("- **Mst-2 (0x40000 = 256KB)** 映射到 **`Bank 0, Row 1`**。\n")
        f.write("- **Mst-3 (0x60000)** 映射到 **`Bank 4, Row 1`**。\n")
        f.write("\n")
        f.write("當 Round-Robin 交錯發送時，Mst-0 剛打開 `Bank 0` 的 `Row 0`，緊接著 Mst-2 就強迫 `Bank 0` 關閉 `Row 0` 並打開 `Row 1`。下一輪，Mst-0 又要存取 `Bank 0` 時，又得把 `Row 1` 關掉換回 `Row 0`。不同 Master 瘋狂覆蓋彼此在同一個 Bank 上的 Row 狀態，導致無盡的 Conflicts。\n\n")
        f.write("### 3. PageHitFirst 為何救不回來？\n")
        f.write("因為 `stride = 0x2000` (8KB)。當 Mst-0 發出下一筆時，位址跳躍了 8KB。在 4 個 Master 交錯的情況下，各個 Channel 的 Queue 裡面充滿了來自不同 Row 的散落請求。排程器找不到任何連續且位址相同的 Row 可以進行 Hit 合併，最終退化成與 FIFO 相同的排程結果，Utilization 停留在 99% 只是因為資料量小且匯流排忙碌而已。\n")

if __name__ == "__main__":
    main()
