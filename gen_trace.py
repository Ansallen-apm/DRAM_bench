import random
import os

def generate_trace(mode, rw_type, size_bytes, num_transactions, filename):
    """
    Generates a memory trace file.
    Args:
        mode (str): 'seq' for sequential, 'rand' for random.
        rw_type (str): 'R' for Read, 'W' for Write.
        size_bytes (int): Size in bytes (128, 256, 512).
        num_transactions (int): Number of transactions.
        filename (str): Output filename.
    """

    # New Format:
    # Col 3: Bus_Width_Log2. Fixed to 6 (64 Bytes).
    # Col 4: Burst_Length_Code. Size = (2^6) * (Code + 1).
    # Code = (Size / 64) - 1.

    bus_width_log2 = 6
    bytes_per_beat = 64

    # Calculate beats
    beats = max(1, size_bytes // bytes_per_beat)
    burst_code_val = beats - 1
    burst_code_hex = f"{burst_code_val:02X}"

    with open(filename, 'w') as f:
        current_addr = 0x10000000 # Base address
        stride = size_bytes

        for i in range(num_transactions):
            if mode == 'seq':
                addr = current_addr + (i * stride)
            else:
                # Random 36-bit address aligned to 64 bytes
                addr = random.randint(0, (2**36) // 64) * 64

            rw_str = f"A{rw_type}x"
            addr_str = f"{addr:016X}"

            line = f"{rw_str} {addr_str} {bus_width_log2} {burst_code_hex}\n"
            f.write(line)

    print(f"Generated {filename}")

if __name__ == "__main__":
    os.makedirs("traces", exist_ok=True)

    sizes = [128, 256, 512]
    modes = ['seq', 'rand']
    rw_types = ['R', 'W']

    for mode in modes:
        for rw in rw_types:
            for size in sizes:
                # Filename: mode_rw_size.trace
                # e.g., seq_read_128B.trace
                rw_name = "read" if rw == 'R' else "write"
                filename = f"traces/{mode}_{rw_name}_{size}B.trace"
                generate_trace(mode, rw, size, 550, filename)
