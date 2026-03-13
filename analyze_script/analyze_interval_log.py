import argparse
import sys
import math
import json

def calculate_percentile(data, percentile):
    if not data:
        return 0
    size = len(data)
    idx = (size - 1) * percentile / 100.0
    if idx.is_integer():
        return data[int(idx)]
    else:
        lower = data[int(math.floor(idx))]
        upper = data[int(math.ceil(idx))]
        fraction = idx - math.floor(idx)
        return lower + (upper - lower) * fraction

def parse_log(filepath):
    data = []
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        # Skip header lines
        if "Interval Logging Enabled" in line or "Interval (us)" in line:
            continue
        if not line:
            continue

        try:
            # Format: 1,000, 99.50, 48, 1024, 12
            # Notice the first token might have commas, so we split by ','
            # But since time also has commas (e.g. 1,000), we must split carefully.
            # However, the string formatter in our simulator writes:
            # f"{formatted_time}, {interval_utilization:.2f}, {interval_reqs}, {interval_bytes}, {int(interval_idle_cycles)}"

            parts = line.split(',')
            # Since the first field (time) might contain commas, we split from the right
            # We know the last 4 fields are util, reqs, bytes, idle
            if len(parts) >= 5:
                idle = int(parts[-1].strip())
                bytes_val = int(parts[-2].strip())
                reqs = int(parts[-3].strip())
                util = float(parts[-4].strip())
                # The rest is the time string, re-join it and remove inner commas
                time_str = "".join(parts[:-4]).strip()
                time_val = int(time_str.replace(',', ''))

                data.append({
                    'time': time_val,
                    'time_str': time_str,
                    'util': util,
                    'reqs': reqs,
                    'bytes': bytes_val,
                    'idle': idle
                })
        except ValueError as e:
            continue
    return data

def main():
    parser = argparse.ArgumentParser(description="Analyze a single interval log file.")
    parser.add_argument('--log', required=True, help='Path to the interval log file')
    parser.add_argument('--top_n', type=int, default=5, help='Number of extreme intervals to show (default: 5)')
    parser.add_argument('--req_threshold', type=int, default=0, help='Threshold to find intervals with requests <= this value (default: 0)')
    parser.add_argument('--json', action='store_true', help='Output summary in JSON format for upper level script')

    args = parser.parse_args()

    data = parse_log(args.log)

    if not data:
        if args.json:
            print(json.dumps({"error": "No valid data found or file is empty"}))
        else:
            print(f"No valid data found in {args.log}.")
        return

    # Basic Statistics
    utils = sorted([d['util'] for d in data])
    avg_util = sum(utils) / len(utils)
    p25_util = calculate_percentile(utils, 25)
    p50_util = calculate_percentile(utils, 50)
    p75_util = calculate_percentile(utils, 75)
    max_util = utils[-1]
    min_util = utils[0]

    # Sortings for Top N
    sorted_by_util_asc = sorted(data, key=lambda x: x['util'])
    sorted_by_util_desc = sorted(data, key=lambda x: x['util'], reverse=True)
    sorted_by_idle_desc = sorted(data, key=lambda x: x['idle'], reverse=True)

    # Filtering for Starvation
    starved_intervals = [d for d in data if d['reqs'] <= args.req_threshold]

    if args.json:
        summary = {
            'file': args.log,
            'total_intervals': len(data),
            'avg_util': round(avg_util, 2),
            'p25_util': round(p25_util, 2),
            'median_util': round(p50_util, 2),
            'p75_util': round(p75_util, 2),
            'min_util': round(min_util, 2),
            'max_util': round(max_util, 2),
            'max_idle_cycles': sorted_by_idle_desc[0]['idle'] if sorted_by_idle_desc else 0,
            'starved_count': len(starved_intervals)
        }
        print(json.dumps(summary))
        return

    # Formatted Console Output
    print(f"=== Analysis for {args.log} ===")
    print(f"Total Intervals: {len(data)}")
    print(f"--- Utilization Statistics ---")
    print(f"Average: {avg_util:.2f}%")
    print(f"25th Percentile: {p25_util:.2f}%")
    print(f"50th Percentile (Median): {p50_util:.2f}%")
    print(f"75th Percentile: {p75_util:.2f}%")
    print("-" * 30)

    print(f"\n[ Top {args.top_n} WORST Utilization ]")
    for d in sorted_by_util_asc[:args.top_n]:
        print(f" Time: {d['time_str']:>6} us | Util: {d['util']:>5.2f}% | Idle: {d['idle']} | Reqs: {d['reqs']}")

    print(f"\n[ Top {args.top_n} BEST Utilization ]")
    for d in sorted_by_util_desc[:args.top_n]:
        print(f" Time: {d['time_str']:>6} us | Util: {d['util']:>5.2f}% | Idle: {d['idle']} | Reqs: {d['reqs']}")

    print(f"\n[ Top {args.top_n} MOST Idle Cycles ]")
    for d in sorted_by_idle_desc[:args.top_n]:
        print(f" Time: {d['time_str']:>6} us | Util: {d['util']:>5.2f}% | Idle: {d['idle']} | Reqs: {d['reqs']}")

    print(f"\n[ Starvation/Bypass (Reqs <= {args.req_threshold}) ]")
    if not starved_intervals:
        print(" -> No starved intervals found.")
    else:
        print(f" -> Found {len(starved_intervals)} intervals.")
        for d in starved_intervals[:args.top_n]:
            print(f" Time: {d['time_str']:>6} us | Util: {d['util']:>5.2f}% | Idle: {d['idle']} | Reqs: {d['reqs']} | Bytes: {d['bytes']}")
        if len(starved_intervals) > args.top_n:
            print(f" ... and {len(starved_intervals) - args.top_n} more.")

    print("=" * 40)

if __name__ == "__main__":
    main()
