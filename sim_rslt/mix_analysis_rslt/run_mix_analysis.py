import os
import glob
import subprocess
import re

def run_simulation(trace_file, queue_depth, config_file):
    cmd = [
        "python3", "../../src/main.py",
        "--config", config_file,
        "--mapping", "../../configs/mapping_2ch.json",
        "--trace", trace_file,
        "--policy", "PageHitFirst",
        "--queue_depth", str(queue_depth)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running simulation for {trace_file} with {config_file}: {e}")
        return None

def parse_output(output):
    metrics = {
        "Total Cycles": 0,
        "Bandwidth (GB/s)": 0.0,
        "Utilization (%)": 0.0,
        "Page Hits": 0
    }

    patterns = {
        "Total Cycles": r"Total Cycles \(總週期\): (\d+)",
        "Bandwidth (GB/s)": r"Bandwidth \(頻寬\): ([\d\.]+) GB/s",
        "Utilization (%)": r"Utilization \(利用率\): ([\d\.]+) %",
        "Page Hits": r"Page Hits \(Page 命中\): (\d+)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, output)
        if match:
            if key in ["Bandwidth (GB/s)", "Utilization (%)"]:
                metrics[key] = float(match.group(1))
            else:
                metrics[key] = int(match.group(1))

    return metrics

def main():
    configs = [
        ("../../configs/LP4_16_cfg.json", "LPDDR4-6400 (16-bit)"),
        ("../../configs/LP4_32_cfg.json", "LPDDR4-6400 (32-bit)"),
        ("../../configs/LP4_64_cfg.json", "LPDDR4-6400 (64-bit)"),
        ("../../configs/LP4_4266_16_cfg.json", "LPDDR4-4266 (16-bit)"),
        ("../../configs/LP4_4266_32_cfg.json", "LPDDR4-4266 (32-bit)"),
        ("../../configs/LP4_4266_64_cfg.json", "LPDDR4-4266 (64-bit)"),
        ("../../configs/LP4_3200_64_cfg.json", "LPDDR4-3200 (64-bit)"),
        ("../../configs/LP5_8533_16_cfg.json", "LPDDR5-8533 (16-bit)"),
        ("../../configs/LP5_8533_32_cfg.json", "LPDDR5-8533 (32-bit)"),
        ("../../configs/LP5_8533_64_cfg.json", "LPDDR5-8533 (64-bit)")
    ]

    trace_files = glob.glob("../../traces/mix/*.trace")
    trace_files.sort()

    output_file = "mix_analysis_rslt.md"

    with open(output_file, "w", encoding='utf-8') as f:
        f.write("# DRAM Simulator Mix Trace Analysis\n")
        f.write("Policy: `PageHitFirst`\n")
        f.write("Comparing Queue Depths 64 and 128 for LPDDR4 and LPDDR5-8533 configurations.\n\n")

        for config_path, config_name in configs:
            print(f"\nEvaluating {config_name}...")
            f.write(f"\n## {config_name}\n\n")
            f.write("| Trace File | QD=64 Cycles | QD=128 Cycles | Cycles Diff (%) | QD=64 Util (%) | QD=128 Util (%) | QD=64 Hits | QD=128 Hits |\n")
            f.write("| --- | --- | --- | --- | --- | --- | --- | --- |\n")

            for trace_file in trace_files:
                trace_name = os.path.basename(trace_file)

                out_64 = run_simulation(trace_file, 64, config_path)
                out_128 = run_simulation(trace_file, 128, config_path)

                if out_64 and out_128:
                    m64 = parse_output(out_64)
                    m128 = parse_output(out_128)

                    c64 = m64["Total Cycles"]
                    c128 = m128["Total Cycles"]
                    u64 = m64["Utilization (%)"]
                    u128 = m128["Utilization (%)"]
                    h64 = m64["Page Hits"]
                    h128 = m128["Page Hits"]

                    if c64 > 0:
                        cyc_diff = ((c64 - c128) / c64) * 100
                    else:
                        cyc_diff = 0.0

                    f.write(f"| {trace_name} | {c64} | {c128} | {cyc_diff:+.2f}% | {u64:.2f} | {u128:.2f} | {h64} | {h128} |\n")
                else:
                    f.write(f"| {trace_name} | N/A | N/A | N/A | N/A | N/A | N/A | N/A |\n")

    print(f"\nAnalysis complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()
