import os
import sys
import json
import argparse

# Add repository root and src directory to PYTHONPATH
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'src'))

from src.mapper import AddressMapper

def main():
    parser = argparse.ArgumentParser(description='Analyze Trace Mapping & Interleaving Pattern')
    parser.add_argument('--mapping', type=str, required=True, help='Path to address mapping JSON (位址映射檔路徑)')
    parser.add_argument('--trace', type=str, required=True, help='Path to trace file (Trace 檔案路徑)')
    parser.add_argument('--req_count', type=int, default=4, help='Number of requests to simulate (模擬的請求數量)')
    parser.add_argument('--chunk_size', type=int, default=1024, help='Simulated Request Size in Bytes before hardware chunking (原始請求位元組大小)')
    args = parser.parse_args()

    with open(args.mapping, "r") as f:
        config = json.load(f)

    mapper = AddressMapper(config)
    trace_file = args.trace

    ch_counts = {}
    bank_counts = {}

    print(f"Analyzing Mapping: {args.mapping}")
    print(f"Analyzing Trace: {args.trace}")
    print(f"Analyzing First {args.req_count} Requests with Size: {args.chunk_size} Bytes")

    with open(trace_file, 'r') as f:
        for i in range(args.req_count):
            line = f.readline().strip().split()
            if not line: break
            addr = int(line[1], 16)

            print(f"\n--- Request {i+1} Original Addr: {hex(addr)} ---")
            curr_addr = addr
            remaining_size = args.chunk_size
            chunk_idx = 1

            while remaining_size > 0:
                mapped = mapper.map_address(curr_addr)
                ch = mapped['Channel']
                bank = mapped['Bank']

                ch_counts[ch] = ch_counts.get(ch, 0) + 1
                bank_counts[(ch, bank)] = bank_counts.get((ch, bank), 0) + 1

                next_boundary = mapper.get_next_boundary(curr_addr)
                # Note: We simulate boundary chunking here to show interleaved distribution
                chunk_size = min(remaining_size, next_boundary - curr_addr)

                print(f"  Chunk {chunk_idx} Addr: {hex(curr_addr)} ({chunk_size} Bytes) -> CH: {ch}, Rank: {mapped['Rank']}, Bank: {bank}, Row: {mapped['Row']}")

                curr_addr += chunk_size
                remaining_size -= chunk_size
                chunk_idx += 1

    print("\nAggregate Distribution Counts:")
    print(f"Channels: {ch_counts}")
    print(f"Banks: {bank_counts}")

if __name__ == "__main__":
    main()
