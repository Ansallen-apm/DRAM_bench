import os
import sys
import json
import argparse

# Add repository root and src directory to PYTHONPATH
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'src'))

from src.main import TraceReader
from src.mapper import AddressMapper

def main():
    parser = argparse.ArgumentParser(description='Analyze Trace Chunking (Hardware-Aligned 2BL Splitting)')
    parser.add_argument('--mapping', type=str, required=True, help='Path to address mapping JSON (位址映射檔路徑)')
    parser.add_argument('--trace', type=str, required=True, help='Path to trace file (Trace 檔案路徑)')
    parser.add_argument('--num_chunks', type=int, default=16, help='Number of chunked requests to print (要印出的切割後請求數量)')
    args = parser.parse_args()

    with open(args.mapping, "r") as f:
        config = json.load(f)

    mapper = AddressMapper(config)
    reader = TraceReader(args.trace, mapper)
    trace_iter = iter(reader)

    print(f"Analyzing Mapping: {args.mapping}")
    print(f"Analyzing Trace: {args.trace}")
    print(f"Displaying first {args.num_chunks} chunked requests:\n")

    for i in range(args.num_chunks):
        req = next(trace_iter, None)
        if req is None:
            print("End of trace reached.")
            break
        print(f"Queue Entry {i+1:02d}: Addr: {hex(req['address'])}, Size: {req['size']} Bytes, Beats: {req['beats']}")

if __name__ == "__main__":
    main()
