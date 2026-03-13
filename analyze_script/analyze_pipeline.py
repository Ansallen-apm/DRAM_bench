import re
from collections import defaultdict

import argparse

def main():
    parser = argparse.ArgumentParser(description="Visualize DRAM Pipeline from log.")
    parser.add_argument('--log', required=True, help='Path to the dram_pipeline_CHx.log file')
    args = parser.parse_args()

    events = []
    with open(args.log, "r") as f:
        for line in f:
            if "RD" in line or "WR" in line:
                m = re.search(r"(\d+): \[CH\d+ RK\d+ BK(\d+)\] (RD|WR) \(Data: (\d+) to (\d+)\)", line)
                if m:
                    issue, bk, cmd, d_start, d_end = m.groups()
                    events.append((int(d_start), int(d_end), f"BK{bk} {cmd}"))
            elif "PRE" in line or "ACT" in line:
                m = re.search(r"(\d+): \[CH\d+ RK\d+ BK(\d+)\] (PRE|ACT)", line)
                if m:
                    issue, bk, cmd = m.groups()
                    # We approximate PRE/ACT duration for visualization
                    events.append((int(issue), int(issue)+10, f"BK{bk} {cmd}"))

    events.sort(key=lambda x: x[0])

    print(f"DRAM Pipeline Timeline ({args.log}, First 400 Cycles)")
    print("-" * 60)
    for start, end, label in events:
        if start > 400: break
        print(f"Cycle {start:>3} - {end:>3} | {label}")

if __name__ == "__main__":
    main()
