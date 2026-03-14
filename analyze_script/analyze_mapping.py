from src.mapper import AddressMapper
import json
import sys

with open("configs/mapping_2ch.json", "r") as f:
    config = json.load(f)

mapper = AddressMapper(config)
trace_file = "traces/PT_test/pt_test.trace"

ch_counts = {0: 0, 1: 0}
bank_counts = {}

# Process first 4 requests (one interleaving cycle)
with open(trace_file, 'r') as f:
    for i in range(4):
        line = f.readline().strip().split()
        if not line: break
        addr = int(line[1], 16)

        # Simulating chunking behavior (4 chunks per 4KB request)
        print(f"\n--- Request {i+1} Original Addr: {hex(addr)} ---")
        curr_addr = addr
        for j in range(4):
            mapped = mapper.map_address(curr_addr)
            ch = mapped['Channel']
            bank = mapped['Bank']
            ch_counts[ch] += 1
            bank_counts[(ch, bank)] = bank_counts.get((ch, bank), 0) + 1
            print(f"  Chunk {j+1} Addr: {hex(curr_addr)} -> CH: {ch}, Bank: {bank}, Row: {mapped['Row']}")

            # move to next 1KB boundary
            curr_addr = mapper.get_next_boundary(curr_addr)

print("\nAggregate counts:")
print(f"Channels: {ch_counts}")
print(f"Banks: {bank_counts}")
