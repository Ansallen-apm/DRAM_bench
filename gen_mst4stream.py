import argparse
import os
import sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from config import load_mapping
from mapper import AddressMapper

def main():
    parser = argparse.ArgumentParser(description="Generate 4-Master Round-Robin DMA Stream Trace with Mapping-Aware Chunking.")
    parser.add_argument('--burst_size', type=int, default=4096, help='Size in bytes per master request (default: 4096)')
    parser.add_argument('--trans_per_dma', type=int, default=16, help='Number of master requests per DMA stream (default: 16)')
    parser.add_argument('--stride', type=lambda x: int(x, 0), default=0x2000, help='Stride in bytes for each consecutive request within a DMA (default: 0x2000)')
    parser.add_argument('--rw_type', type=str, default='R', choices=['R', 'W', 'RW'], help='Read/Write type (default: R)')
    parser.add_argument('--mapping', type=str, default='configs/mapping_2ch.json', help='Address mapping JSON to define interleaving boundaries')
    parser.add_argument('--out_dir', type=str, default='traces/mst4stream', help='Output directory')
    parser.add_argument('--out_filename', type=str, default='mst4_4KB_read.trace', help='Output filename')

    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    out_filepath = os.path.join(args.out_dir, args.out_filename)

    try:
        mapping = load_mapping(args.mapping)
        mapper = AddressMapper(mapping)
    except Exception as e:
        print(f"Failed to load mapping: {e}")
        return

    bytes_per_beat = 64
    bus_width_log2 = 6

    # Define Master configurations
    masters_cfg = {
        0: [(0x00000, args.stride), (0x01000, args.stride)],
        1: [(0x20000, args.stride), (0x21000, args.stride)],
        2: [(0x40000, args.stride), (0x41000, args.stride)],
        3: [(0x60000, args.stride), (0x61000, args.stride)]
    }

    # State tracking for each master
    master_states = {}
    for mst_id, dmas in masters_cfg.items():
        master_states[mst_id] = {
            'dmas': dmas,
            'current_dma_idx': 0,
            'current_trans_count': 0,
            'current_addr': dmas[0][0] if len(dmas) > 0 else 0
        }

    active_masters = list(masters_cfg.keys())
    active_masters.sort()

    total_written_transactions = 0

    with open(out_filepath, 'w') as f:
        while active_masters:
            for mst_id in list(active_masters):
                state = master_states[mst_id]

                # Fetch current DMA config
                dma_idx = state['current_dma_idx']
                start_addr, stride = state['dmas'][dma_idx]
                base_addr = state['current_addr']

                # Determine R/W
                current_rw = random.choice(['R', 'W']) if args.rw_type == 'RW' else args.rw_type
                rw_str = f"A{current_rw}x"

                # Mapping-Aware Chunking: Split the massive burst_size into smaller transactions
                # whenever it crosses a Channel, Rank, Bank, or Row boundary.
                chunks = []
                current_chunk_start = base_addr
                current_chunk_size = 0

                # Use the first 64B to define the initial boundary signature
                initial_map = mapper.map_address(current_chunk_start)
                current_signature = (initial_map.get('Channel', 0), initial_map.get('Rank', 0), initial_map.get('Bank', 0), initial_map.get('Row', 0))

                for offset in range(0, args.burst_size, bytes_per_beat):
                    eval_addr = base_addr + offset
                    eval_map = mapper.map_address(eval_addr)
                    eval_signature = (eval_map.get('Channel', 0), eval_map.get('Rank', 0), eval_map.get('Bank', 0), eval_map.get('Row', 0))

                    if eval_signature != current_signature and current_chunk_size > 0:
                        # Boundary crossed, close the current chunk
                        chunks.append((current_chunk_start, current_chunk_size))
                        # Start a new chunk
                        current_chunk_start = eval_addr
                        current_chunk_size = bytes_per_beat
                        current_signature = eval_signature
                    else:
                        current_chunk_size += bytes_per_beat

                # Append the last chunk
                if current_chunk_size > 0:
                    chunks.append((current_chunk_start, current_chunk_size))

                # Write all chunks to the trace file sequentially
                for chunk_addr, chunk_size in chunks:
                    beats = max(1, chunk_size // bytes_per_beat)
                    burst_code_val = beats - 1
                    burst_code_hex = f"{burst_code_val:02X}"

                    addr_str = f"{chunk_addr:016X}"
                    line = f"{rw_str} {addr_str} {bus_width_log2} {burst_code_hex}\n"
                    f.write(line)
                    total_written_transactions += 1

                # Update state for this master
                state['current_trans_count'] += 1
                state['current_addr'] += stride

                # Check if current DMA stream is finished
                if state['current_trans_count'] >= args.trans_per_dma:
                    state['current_dma_idx'] += 1
                    state['current_trans_count'] = 0

                    # If there's another DMA stream, initialize its starting address
                    if state['current_dma_idx'] < len(state['dmas']):
                        state['current_addr'] = state['dmas'][state['current_dma_idx']][0]
                    else:
                        # Master has finished all its DMAs
                        active_masters.remove(mst_id)

    print(f"Successfully generated trace: {out_filepath}")
    print(f"Logical Requests: {4 * len(masters_cfg[0]) * args.trans_per_dma} (x {args.burst_size} Bytes)")
    print(f"Actual Trace Transactions Generated (due to chunking): {total_written_transactions}")

if __name__ == "__main__":
    main()
