import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate 4-Master Round-Robin DMA Stream Trace.")
    parser.add_argument('--burst_size', type=int, default=4096, help='Size in bytes per transaction (default: 4096)')
    parser.add_argument('--trans_per_dma', type=int, default=16, help='Number of transactions per DMA stream (default: 16)')
    parser.add_argument('--rw_type', type=str, default='R', choices=['R', 'W', 'RW'], help='Read/Write type (default: R)')
    parser.add_argument('--out_dir', type=str, default='traces/mst4stream', help='Output directory')
    parser.add_argument('--out_filename', type=str, default='mst4_4KB_read.trace', help='Output filename')

    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    out_filepath = os.path.join(args.out_dir, args.out_filename)

    # Calculate Burst Code for trace format
    # Trace format requires: Code = (Size / 64) - 1. E.g., 4096 / 64 - 1 = 63 = 3F
    bytes_per_beat = 64
    bus_width_log2 = 6
    beats = max(1, args.burst_size // bytes_per_beat)
    burst_code_val = beats - 1
    burst_code_hex = f"{burst_code_val:02X}"

    # Define Master configurations
    # Each master has a list of DMAs: (start_addr, stride)
    masters_cfg = {
        0: [(0x00000, 0x2000), (0x01000, 0x2000)],
        1: [(0x20000, 0x2000), (0x21000, 0x2000)],
        2: [(0x40000, 0x2000), (0x41000, 0x2000)],
        3: [(0x60000, 0x2000), (0x61000, 0x2000)]
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
    active_masters.sort() # Ensure deterministic round-robin order [0, 1, 2, 3]

    import random

    with open(out_filepath, 'w') as f:
        while active_masters:
            for mst_id in list(active_masters): # Iterate over a copy since we might remove elements
                state = master_states[mst_id]

                # Fetch current DMA config
                dma_idx = state['current_dma_idx']
                start_addr, stride = state['dmas'][dma_idx]

                addr = state['current_addr']

                # Determine R/W
                current_rw = random.choice(['R', 'W']) if args.rw_type == 'RW' else args.rw_type
                rw_str = f"A{current_rw}x"

                # Write to trace
                addr_str = f"{addr:016X}"
                line = f"{rw_str} {addr_str} {bus_width_log2} {burst_code_hex}\n"
                f.write(line)

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
    print(f"Total Transactions: {4 * len(masters_cfg[0]) * args.trans_per_dma}")
    print(f"Burst Size: {args.burst_size} Bytes (Burst Code: {burst_code_hex})")

if __name__ == "__main__":
    main()
