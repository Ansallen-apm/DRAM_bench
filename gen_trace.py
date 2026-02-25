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

    # Calculate burst count assuming BL16 (LPDDR4 default) and 16-bit channel (2 bytes/beat).
    # One burst = 16 beats * 2 bytes = 32 bytes.
    # Burst Code 00 = 1 burst (32B), 01 = 2 bursts (64B), etc.
    # Formula: burst_code = (size_bytes // 32) - 1
    # Check alignment:
    burst_count = max(1, size_bytes // 32)
    burst_code_val = burst_count - 1
    burst_code_hex = f"{burst_code_val:02X}"

    size_pow2 = int(size_bytes).bit_length() - 1 # 128 -> 7, 256 -> 8, 512 -> 9

    with open(filename, 'w') as f:
        current_addr = 0x10000000 # Base address
        stride = size_bytes # Stride for sequential

        for i in range(num_transactions):
            if mode == 'seq':
                addr = current_addr + (i * stride)
            else: # rand
                # Random 36-bit address aligned to 64 bytes
                addr = random.randint(0, (2**36) // 64) * 64

            rw_str = f"A{rw_type}x"
            addr_str = f"{addr:016X}"

            line = f"{rw_str} {addr_str} {size_pow2} {burst_code_hex}\n"
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
                generate_trace(mode, rw, size, 100, filename)
