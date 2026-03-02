import os
import glob
import subprocess
import re

def run_simulation(trace_file, config_file="configs/LP4_32_cfg.json"):
    cmd = [
        "python3", "src/main.py",
        "--config", config_file,
        "--mapping", "configs/mapping.json",
        "--trace", trace_file,
        "--policy", "FIFO",
        "--queue_depth", "16"
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

def run_benchmark(config_file, config_name, output_file):
    print(f"\nRunning benchmark for {config_name}...")
    trace_files = glob.glob("traces/*.trace")
    # Filter out basic traces
    trace_files = [f for f in trace_files if "basic" not in f and "basic100" not in f]
    trace_files.sort()

    results = []

    for trace_file in trace_files:
        print(f"Running simulation for {trace_file}...")
        output = run_simulation(trace_file, config_file)
        if output:
            metrics = parse_output(output)
            metrics["Trace File"] = os.path.basename(trace_file)
            results.append(metrics)

    # Generate Markdown Table
    markdown_output = []
    markdown_output.append(f"\n## Simulation Results ({config_name})\n")
    headers = ["Trace File", "Total Cycles", "Bandwidth (GB/s)", "Utilization (%)", "Avg Queue Depth", "Page Hits", "Page Misses", "Page Conflicts"]

    # Header
    markdown_output.append("| " + " | ".join(headers) + " |")
    markdown_output.append("| " + " | ".join(["---"] * len(headers)) + " |")

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
        markdown_output.append("| " + " | ".join(row) + " |")

    # Print to console and append to file
    final_output = "\n".join(markdown_output) + "\n"
    print(final_output)
    with open(output_file, "a") as f:
        f.write(final_output)

def main():
    output_file = "BENCHMARK_RESULTS.md"
    # Clear existing file contents
    with open(output_file, "w") as f:
        f.write("# DRAM Simulator Benchmark Results\n")

    configs = [
        ("configs/LP4_16_cfg.json", "LPDDR4-6400 (16-bit)"),
        ("configs/LP4_32_cfg.json", "LPDDR4-6400 (32-bit)"),
        ("configs/LP4_64_cfg.json", "LPDDR4-6400 (64-bit)"),
        ("configs/LP4_4266_16_cfg.json", "LPDDR4-4266 (16-bit)"),
        ("configs/LP4_4266_32_cfg.json", "LPDDR4-4266 (32-bit)"),
        ("configs/LP4_4266_64_cfg.json", "LPDDR4-4266 (64-bit)"),
        ("configs/LP5_16_cfg.json", "LPDDR5-6400 (16-bit)"),
        ("configs/LP5_32_cfg.json", "LPDDR5-6400 (32-bit)"),
        ("configs/LP5_64_cfg.json", "LPDDR5-6400 (64-bit)"),
        ("configs/LP5_8533_16_cfg.json", "LPDDR5-8533 (16-bit)"),
        ("configs/LP5_8533_32_cfg.json", "LPDDR5-8533 (32-bit)"),
        ("configs/LP5_8533_64_cfg.json", "LPDDR5-8533 (64-bit)")
    ]

    for config_path, config_name in configs:
        run_benchmark(config_path, config_name, output_file)

if __name__ == "__main__":
    main()
