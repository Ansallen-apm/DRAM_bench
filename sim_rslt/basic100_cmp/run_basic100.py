import os
import glob
import subprocess
import re

def run_simulation(trace_file, queue_depth, config_file="../../configs/LP4_32_cfg.json"):
    cmd = [
        "python3", "../../src/main.py",
        "--config", config_file,
        "--mapping", "../../configs/mapping_2ch.json",
        "--trace", trace_file,
        "--policy", "FIFO",
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
        "Avg Queue Depth": 0.0,
    }

    patterns = {
        "Total Cycles": r"Total Cycles \(總週期\): (\d+)",
        "Bandwidth (GB/s)": r"Bandwidth \(頻寬\): ([\d\.]+) GB/s",
        "Utilization (%)": r"Utilization \(利用率\): ([\d\.]+) %",
        "Avg Queue Depth": r"Average Queue Depth \(平均隊列深度\): ([\d\.]+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, output)
        if match:
            if key in ["Bandwidth (GB/s)", "Utilization (%)", "Avg Queue Depth"]:
                metrics[key] = float(match.group(1))
            else:
                metrics[key] = int(match.group(1))

    return metrics

def main():
    trace_files = glob.glob("../../traces/basic100/*.trace")
    trace_files.sort()

    results = {}
    config_file = "../../configs/LP4_32_cfg.json"

    print("Running simulations for basic100 traces...")
    for trace_file in trace_files:
        basename = os.path.basename(trace_file)
        results[basename] = {"QD16": {}, "QD64": {}}

        # Run QD=16
        out_16 = run_simulation(trace_file, 16, config_file)
        if out_16:
            results[basename]["QD16"] = parse_output(out_16)

        # Run QD=64
        out_64 = run_simulation(trace_file, 64, config_file)
        if out_64:
            results[basename]["QD64"] = parse_output(out_64)

    output_file = "basic100_cmp.md"
    with open(output_file, "w") as f:
        f.write("# DRAM Simulator basic100 Benchmark Results (QD=16 vs QD=64)\n")
        f.write("Configuration: `configs/LP4_32_cfg.json`\n\n")

        headers = ["Trace File", "Metric", "QD=16", "QD=64", "Difference"]
        f.write("| " + " | ".join(headers) + " |\n")
        f.write("| " + " | ".join(["---"] * len(headers)) + " |\n")

        for trace_file, data in results.items():
            qd16 = data.get("QD16", {})
            qd64 = data.get("QD64", {})

            if not qd16 or not qd64:
                continue

            metrics_order = ["Total Cycles", "Bandwidth (GB/s)", "Utilization (%)", "Avg Queue Depth"]

            for i, metric in enumerate(metrics_order):
                val16 = qd16.get(metric, 0)
                val64 = qd64.get(metric, 0)

                # Format appropriately
                if metric == "Total Cycles":
                    v16_str = str(val16)
                    v64_str = str(val64)
                    diff_str = f"{(val64 - val16):+d}"
                else:
                    v16_str = f"{val16:.2f}"
                    v64_str = f"{val64:.2f}"
                    diff_str = f"{(val64 - val16):+.2f}"

                trace_name_cell = f"**{trace_file}**" if i == 0 else ""
                row = [trace_name_cell, metric, v16_str, v64_str, diff_str]
                f.write("| " + " | ".join(row) + " |\n")

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
