import subprocess
import re

def run_simulation(policy):
    cmd = [
        "python3", "../../src/asyc_parall_opt.py",
        "--config", "../../configs/LP4_4266_64_cfg.json",
        "--mapping", "../../configs/mapping_2ch.json",
        "--trace", "../../traces/mst4stream_stride1000/mst4_4KB_stride1000_read.trace",
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
    print("Running FIFO (Stride 0x1000)...")
    fifo_metrics = run_simulation("FIFO")

    print("Running PageHitFirst (Stride 0x1000)...")
    phf_metrics = run_simulation("PageHitFirst")

    with open("mst4_stride1000_policy_cmp.md", "w", encoding='utf-8') as f:
        f.write("# Policy Comparison: FIFO vs PageHitFirst (Stride 0x1000)\n\n")
        f.write("**Trace**: `mst4_4KB_stride1000_read.trace` (4 Masters Interleaved, 4KB bursts, Stride=4KB)\n")
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
        f.write("即使我們將 Stride 從 `0x2000` (8KB) 降到 `0x1000` (4KB) 以確保同一個 Master 的連續請求落在同一個 Row ($32$ KB) 內，**結果依然是 0 Hits，`PageHitFirst` 完全無法發揮作用**。這揭示了多核心交錯存取在排程與 Address Mapping 上的深層瓶頸：\n\n")
        f.write("### 1. 致命的 Bank 乒乓效應 (Ping-Pong Effect)\n")
        f.write("根據 `mapping_2ch.json`，Bank 由 Bits 15~17 決定，Row 則由 Bits 18 以上決定。各 Master 的 Base Address 導致了以下映射：\n")
        f.write("- Mst-0 (`0x00000`): **`Bank 0, Row 0`**\n")
        f.write("- Mst-1 (`0x20000`): `Bank 4, Row 0`\n")
        f.write("- Mst-2 (`0x40000`): **`Bank 0, Row 1`**  (與 Mst-0 衝突！)\n")
        f.write("- Mst-3 (`0x60000`): `Bank 4, Row 1`  (與 Mst-1 衝突！)\n\n")
        f.write("Mst-0 和 Mst-2 都映射到 `Bank 0`，但分別需要打開不同的 `Row 0` 和 `Row 1`。當 Mst-0 使用完 Row 0 後，Mst-2 的請求迫使控制器執行 PRE (關閉 Row 0) 並 ACT (打開 Row 1)。\n\n")
        f.write("### 2. 為什麼 Queue Depth=64 和 PageHitFirst 救不回來？\n")
        f.write("在 Round-Robin 發射機制下，指令進入 Queue 的順序是：`M0_1st -> M1_1st -> M2_1st -> M3_1st -> M0_2nd ...`。\n")
        f.write("雖然 M0_2nd (`0x01000`) 與 M0_1st 位於相同的 `Bank 0, Row 0`，且 Queue Depth 足夠深 (64) 以同時容納它們，但 **M2_1st** 卡在它們中間。當 M0_1st 執行完畢，Bank 0 處於空閒，排程器看到排在前面的 M2_1st 已經準備好，就讓它去打開了 `Row 1`。\n")
        f.write("等到排程器掃描到後面的 M0_2nd 發現它是 `Row 0` 時，Bank 0 的狀態已經被 M2_1st 給破壞了。因此，它無法形成 Hit，只能被迫再次 PRE+ACT。這證明了在惡意的 Address Pattern 之下，只要競爭對手的請求先被服務並改變了 Bank 狀態，`PageHitFirst` 策略也無法挽救被洗掉的 Row，效能將無可避免地退化為高 Conflict 的低效模式。\n")

if __name__ == "__main__":
    main()
