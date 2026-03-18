import argparse
import os
import sys
from collections import deque

# Add repository root and src directory to PYTHONPATH
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'src'))

from src.config import load_mapping
from src.mapper import AddressMapper

def parse_trace_line(line):
    # Example line: ARx 0000000000000000 6 3F
    parts = line.strip().split()
    if len(parts) < 4:
        return None
    rw_type = parts[0]
    base_addr = int(parts[1], 16)
    bus_width_log2 = int(parts[2])
    burst_code_hex = int(parts[3], 16)
    size = (1 << bus_width_log2) * (burst_code_hex + 1)
    return rw_type, base_addr, size

def get_bank_id(mapped_addr):
    # Create a unique tuple for a bank considering Channel, Rank, and Bank
    return (mapped_addr.get('Channel', 0), mapped_addr.get('Rank', 0), mapped_addr.get('Bank', 0))

def format_bank_id(bank_id):
    return f"CH{bank_id[0]}_R{bank_id[1]}_B{bank_id[2]}"

def main():
    parser = argparse.ArgumentParser(description="Analyze trace mapping and bank interleaving.")
    parser.add_argument('--trace', type=str, required=True, help='Path to trace file')
    parser.add_argument('--mapping', type=str, required=True, help='Path to mapping JSON')
    parser.add_argument('--queue_depth', type=int, default=16, help='Command queue depth (window size)')
    parser.add_argument('--chunk_size', type=int, default=256, help='Queue chunk data size in bytes (e.g., 256 or 128)')
    parser.add_argument('--out', type=str, default='analyze_script/trace_analysis.md', help='Output Markdown file')
    args = parser.parse_args()

    # Load mapping
    try:
        mapping_data = load_mapping(args.mapping)
        mapper = AddressMapper(mapping_data)
    except Exception as e:
        print(f"Error loading mapping: {e}")
        return

    # Phase 1 & 2: Parse trace and chunk
    all_chunks = [] # List of tuples: (chunk_addr, chunk_size, mapped_addr)
    bytes_per_beat = 64 # Assume standard 64B per beat for initial chunking

    print(f"Reading and parsing trace file: {args.trace}...")
    with open(args.trace, 'r') as f:
        for line in f:
            parsed = parse_trace_line(line)
            if not parsed:
                continue
            rw_type, base_addr, total_size = parsed

            # Replace complex heuristic chunking with exact TraceReader get_next_boundary behavior
            curr_addr = base_addr
            remaining_size = total_size

            while remaining_size > 0:
                next_boundary = mapper.get_next_boundary(curr_addr)
                # Chunk size is limited by the remaining size, the next hardware boundary, and the 2BL max limit.
                chunk_size = min(remaining_size, next_boundary - curr_addr, args.chunk_size)

                mapped = mapper.map_address(curr_addr)
                all_chunks.append({
                    'addr': curr_addr,
                    'size': chunk_size,
                    'bank_id': get_bank_id(mapped),
                    'mapped': mapped
                })

                curr_addr += chunk_size
                remaining_size -= chunk_size

    print(f"Total logical queue chunks generated: {len(all_chunks)}")

    # Phase 3: Sliding window simulation
    window = deque(maxlen=args.queue_depth)

    # Stats
    total_bank_switches = 0
    window_stats = [] # Store unique bank counts for each full window step

    print("Running sliding window simulation...")
    prev_bank_id = None

    for i, chunk in enumerate(all_chunks):
        current_bank_id = chunk['bank_id']

        # Check bank switch for consecutive requests
        if prev_bank_id is not None and current_bank_id != prev_bank_id:
            total_bank_switches += 1
        prev_bank_id = current_bank_id

        # Add to window
        window.append(chunk)

        # Evaluate window if full
        if len(window) == args.queue_depth:
            unique_banks = set(c['bank_id'] for c in window)
            num_unique_banks = len(unique_banks)

            # Simple bitmap/distribution representation
            distribution = {}
            for c in window:
                bid = format_bank_id(c['bank_id'])
                distribution[bid] = distribution.get(bid, 0) + 1

            window_stats.append({
                'step': i - args.queue_depth + 1,
                'unique_banks': num_unique_banks,
                'distribution': distribution
            })

    # Phase 4: Output Markdown
    print(f"Generating markdown report: {args.out}...")
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)

    with open(args.out, 'w') as f:
        f.write("# Trace Mapping and Bank Interleaving Analysis\n\n")
        f.write("## 1. Configuration (設定摘要)\n")
        f.write(f"- **Trace File**: `{args.trace}`\n")
        f.write(f"- **Mapping Config**: `{args.mapping}`\n")
        f.write(f"- **Queue Depth**: `{args.queue_depth}`\n")
        f.write(f"- **Queue Chunk Size**: `{args.chunk_size}` Bytes\n\n")

        f.write("## 2. Overall Statistics (整體統計)\n")
        f.write(f"- **Total Queue Chunks**: `{len(all_chunks)}`\n")
        f.write(f"- **Total Consecutive Bank Switches (連續 Bank 切換次數)**: `{total_bank_switches}`\n")

        if window_stats:
            avg_unique_banks = sum(s['unique_banks'] for s in window_stats) / len(window_stats)
            max_unique_banks = max(s['unique_banks'] for s in window_stats)
            min_unique_banks = min(s['unique_banks'] for s in window_stats)

            f.write(f"- **Average Unique Banks per Window (平均 Queue Bank 數量)**: `{avg_unique_banks:.2f}`\n")
            f.write(f"- **Max Unique Banks (最大 Bank 數量)**: `{max_unique_banks}`\n")
            f.write(f"- **Min Unique Banks (最小 Bank 數量)**: `{min_unique_banks}`\n\n")

            f.write("## 3. Sliding Window Log (視窗滑動歷程)\n")
            f.write("*(Showing first 50 steps, peak interleaving steps, and last 50 steps to avoid massive file size)*\n\n")

            # Helper to write step
            def write_step(s):
                dist_str = ", ".join([f"{k}:{v}" for k, v in sorted(s['distribution'].items())])
                f.write(f"- **Step {s['step']}**: Unique Banks: `{s['unique_banks']}` | Distribution: `[{dist_str}]`\n")

            total_steps = len(window_stats)

            f.write("### Initial Steps (初始階段)\n")
            for s in window_stats[:50]:
                write_step(s)

            if total_steps > 100:
                f.write("\n...\n\n### Peak Interleaving Steps (最大交錯階段)\n")
                # Find steps with max unique banks (limit to 20 to avoid spam)
                peak_steps = [s for s in window_stats if s['unique_banks'] == max_unique_banks]
                for s in peak_steps[:20]:
                    write_step(s)

                f.write("\n...\n\n### Final Steps (最終階段)\n")
                for s in window_stats[-50:]:
                    write_step(s)
        else:
            f.write("\n*Warning: Not enough chunks to fill a single queue window.*\n")

    print("Done!")

if __name__ == "__main__":
    main()
