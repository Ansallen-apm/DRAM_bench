import re

def parse_md(filepath):
    results = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()

    current_config = ""
    for line in lines:
        # Match config headers like "## Simulation Results (LPDDR4-6400 (32-bit))"
        # and "## Simulation Results (LPDDR4-6400 (32-bit)) - QD=64"
        # Using a regex that captures everything inside the outermost parentheses.
        config_match = re.search(r"## Simulation Results \((.*)\)(?: - QD=\d+)?", line)
        if config_match:
            current_config = config_match.group(1).strip()
            # If the config name still has the "- QD=64" part because it was inside the parens, clean it.
            if current_config.endswith(") - QD=64"):
                current_config = current_config[:-9]
            results[current_config] = {}
            continue

        if "|" in line and "Trace File" not in line and "---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 8:
                trace_file = parts[0]
                utilization = float(parts[3])

                results[current_config][trace_file] = utilization
    return results

def main():
    res_16 = parse_md("../BENCHMARK_RESULTS/BENCHMARK_RESULTS.md")
    res_64 = parse_md("../bench_rslt/bench_rslt.md")

    with open("bench_cmp.md", "w") as f:
        f.write("# DRAM Simulator Benchmark Utilization Comparison (QD=16 vs QD=64)\n")
        f.write("This file compares the Utilization (%) between the default Queue Depth 16 (`BENCHMARK_RESULTS.md`) and Queue Depth 64 (`bench_rslt.md`).\n\n")

        # Collect all configs from both files
        all_configs = sorted(list(set(res_16.keys()) | set(res_64.keys())))

        for config in all_configs:
            f.write(f"\n## {config}\n\n")
            f.write("| Trace File | QD=16 Utilization (%) | QD=64 Utilization (%) | Difference (%) |\n")
            f.write("| --- | --- | --- | --- |\n")

            # Collect traces for this config from both files
            traces_16 = res_16.get(config, {})
            traces_64 = res_64.get(config, {})
            all_traces = sorted(list(set(traces_16.keys()) | set(traces_64.keys())))

            for trace in all_traces:
                u16 = traces_16.get(trace, None)
                u64 = traces_64.get(trace, None)

                u16_str = f"{u16:.2f}" if u16 is not None else "N/A"
                u64_str = f"{u64:.2f}" if u64 is not None else "N/A"
                diff_str = "N/A"
                if u16 is not None and u64 is not None:
                    diff_str = f"{(u64 - u16):+.2f}"

                f.write(f"| {trace} | {u16_str} | {u64_str} | {diff_str} |\n")

if __name__ == "__main__":
    main()
