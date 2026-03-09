import subprocess
import os
import re

def run_simulation(script, trace):
    cmd = [
        "python3", script,
        "--config", "../../configs/LP4_32_cfg.json",
        "--mapping", "../../configs/mapping_2ch.json",
        "--trace", f"../../{trace}",
        "--policy", "PageHitFirst",
        "--queue_depth", "64"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Parse the Overall output
    output = result.stdout

    metrics = {
        'cycles': 0,
        'bandwidth': 0.0,
        'utilization': 0.0,
        'bytes': 0,
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

    bytes_match = re.search(r"Total Bytes\s*\(總位元組\):\s*(\d+)", output)
    if bytes_match:
        metrics['bytes'] = int(bytes_match.group(1))

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
    trace_dir = "../../traces/basic100/"
    traces = [f"traces/basic100/{f}" for f in os.listdir(trace_dir) if f.endswith(".trace")]

    all_passed = True
    print("Testing basic100 traces for Zero-Error validation (asyc_parall vs asyc_parall_opt)...\n")
    print(f"{'Trace File':<25} | {'Result':<6} | {'Mismatches (if any)'}")
    print("-" * 80)

    for trace in traces:
        trace_name = os.path.basename(trace)

        orig_metrics = run_simulation("../../src/asyc_parall.py", trace)
        opt_metrics = run_simulation("../../src/asyc_parall_opt.py", trace)

        mismatches = []
        for key in orig_metrics:
            if orig_metrics[key] != opt_metrics[key]:
                mismatches.append(f"{key}: {orig_metrics[key]} != {opt_metrics[key]}")

        if len(mismatches) == 0:
            print(f"{trace_name:<25} | \033[92mPASS\033[0m   | None")
        else:
            print(f"{trace_name:<25} | \033[91mFAIL\033[0m   | " + ", ".join(mismatches))
            all_passed = False

    print("\n" + "=" * 80)
    if all_passed:
        print("\033[92mValidation SUCCESS: ZERO errors found.\033[0m")
        print("The optimization does not introduce any data inaccuracy.")
    else:
        print("\033[91mValidation FAILED: Errors found.\033[0m")
        print("The caching logic missed some state invalidations (e.g., cross-bank global timings).")

if __name__ == "__main__":
    main()
