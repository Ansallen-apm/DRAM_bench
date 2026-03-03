import re

def parse_md(filepath):
    results = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()

    current_config = ""
    current_policy = ""
    for line in lines:
        # Match config headers like "## Simulation Results (LPDDR4-6400 (32-bit)) - QD=64 - Policy=FIFO"
        config_match = re.search(r"## Simulation Results \((.*)\) - QD=\d+ - Policy=(.*)", line)
        if config_match:
            current_config = config_match.group(1).strip()
            current_policy = config_match.group(2).strip()
            if current_config not in results:
                results[current_config] = {}
            if current_policy not in results[current_config]:
                results[current_config][current_policy] = {}
            continue

        if current_config and current_policy and "|" in line and "Trace File" not in line and "---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 8:
                trace_file = parts[0]
                total_cycles = int(parts[1])
                utilization = float(parts[3])
                page_hits = int(parts[5])

                results[current_config][current_policy][trace_file] = {
                    "cycles": total_cycles,
                    "util": utilization,
                    "page_hits": page_hits
                }
    return results

def main():
    res = parse_md("bench_rslt.md")

    with open("policy_cmp.md", "w", encoding='utf-8') as f:
        f.write("# DRAM Simulator Policy Comparison (FIFO vs PageHitFirst)\n")
        f.write("This file compares the performance metrics between `FIFO` and `PageHitFirst` policies at Queue Depth 64.\n\n")

        all_configs = sorted(list(res.keys()))

        for config in all_configs:
            f.write(f"\n## {config}\n\n")
            f.write("| Trace File | FIFO Cycles | PHF Cycles | Cycles Diff (%) | FIFO Util (%) | PHF Util (%) | Util Diff | FIFO Hits | PHF Hits |\n")
            f.write("| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")

            traces_fifo = res[config].get("FIFO", {})
            traces_phf = res[config].get("PageHitFirst", {})
            all_traces = sorted(list(set(traces_fifo.keys()) | set(traces_phf.keys())))

            for trace in all_traces:
                t_fifo = traces_fifo.get(trace)
                t_phf = traces_phf.get(trace)

                if t_fifo and t_phf:
                    cyc_fifo = t_fifo["cycles"]
                    cyc_phf = t_phf["cycles"]
                    util_fifo = t_fifo["util"]
                    util_phf = t_phf["util"]
                    hits_fifo = t_fifo["page_hits"]
                    hits_phf = t_phf["page_hits"]

                    cyc_diff_pct = ((cyc_fifo - cyc_phf) / cyc_fifo) * 100
                    util_diff = util_phf - util_fifo

                    f.write(f"| {trace} | {cyc_fifo} | {cyc_phf} | {cyc_diff_pct:+.2f}% | {util_fifo:.2f} | {util_phf:.2f} | {util_diff:+.2f} | {hits_fifo} | {hits_phf} |\n")
                else:
                    f.write(f"| {trace} | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |\n")

if __name__ == "__main__":
    main()
