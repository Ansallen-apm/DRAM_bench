import os
import glob
import subprocess
import re

def run_simulation(trace_file):
    cmd = [
        "python3", "src/main.py",
        "--config", "configs/LP4_cfg.json",
        "--mapping", "configs/mapping.json",
        "--trace", trace_file,
        "--policy", "FIFO",
        "--queue_depth", "16"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running simulation for {trace_file}: {e}")
        return None

def parse_output(output):
    metrics = {
        "Total Cycles": 0,
        "Bandwidth (GB/s)": 0.0,
        "Utilization (%)": 0.0,
        "Avg Queue Depth": 0.0,
        "Page Hits": 0,
        "Page Misses": 0,
        "Page Conflicts": 0
    }

    patterns = {
        "Total Cycles": r"Total Cycles \(總週期\): (\d+)",
        "Bandwidth (GB/s)": r"Bandwidth \(頻寬\): ([\d\.]+) GB/s",
        "Utilization (%)": r"Utilization \(利用率\): ([\d\.]+) %",
        "Avg Queue Depth": r"Average Queue Depth \(平均隊列深度\): ([\d\.]+)",
        "Page Hits": r"Page Hits \(Page 命中\): (\d+)",
        "Page Misses": r"Page Misses \(Page 未命中\): (\d+)",
        "Page Conflicts": r"Page Conflicts \(Page 衝突\): (\d+)"
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
    trace_files = glob.glob("traces/*.trace")
    # Filter out basic traces
    trace_files = [f for f in trace_files if "basic" not in f and "basic100" not in f]
    trace_files.sort()

    print(f"Found {len(trace_files)} trace files to process.")

    results = []

    for trace_file in trace_files:
        print(f"Running simulation for {trace_file}...")
        output = run_simulation(trace_file)
        if output:
            metrics = parse_output(output)
            metrics["Trace File"] = os.path.basename(trace_file)
            results.append(metrics)

    # Print Markdown Table
    print("\n## Simulation Results\n")
    headers = ["Trace File", "Total Cycles", "Bandwidth (GB/s)", "Utilization (%)", "Avg Queue Depth", "Page Hits", "Page Misses", "Page Conflicts"]

    # Print Header
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["---"] * len(headers)) + " |")

    for res in results:
        row = [
            res["Trace File"],
            str(res["Total Cycles"]),
            f"{res['Bandwidth (GB/s)']:.2f}",
            f"{res['Utilization (%)']:.2f}",
            f"{res['Avg Queue Depth']:.2f}",
            str(res["Page Hits"]),
            str(res["Page Misses"]),
            str(res["Page Conflicts"])
        ]
        print("| " + " | ".join(row) + " |")

if __name__ == "__main__":
    main()
