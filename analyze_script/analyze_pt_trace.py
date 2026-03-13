import sys

def analyze(filepath):
    reads = 0
    writes = 0
    sizes = {}
    total_bytes = 0

    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts: continue

            cmd = parts[0]
            if cmd == 'ARx': reads += 1
            elif cmd == 'AWx': writes += 1

            # burst_len_code: beat
            beat_hex = parts[3]
            beat = int(beat_hex, 16)

            # size in bytes: 2^6 * (beat + 1) = 64 * (beat + 1)
            # Assuming bus_width_log2 is always 6 (64 bytes) for this format based on earlier context
            bus_width_log2 = int(parts[2])
            bus_width = 1 << bus_width_log2
            size = bus_width * (beat + 1)

            if size not in sizes:
                sizes[size] = 0
            sizes[size] += 1
            total_bytes += size

    total_reqs = reads + writes
    print(f"Total Requests: {total_reqs}")
    print(f"Reads: {reads} ({reads/total_reqs*100:.2f}%)")
    print(f"Writes: {writes} ({writes/total_reqs*100:.2f}%)")
    print(f"Total Bytes Transferred: {total_bytes / 1024 / 1024:.2f} MB")
    print("\nTransaction Sizes:")
    for size, count in sorted(sizes.items()):
        print(f"  {size} Bytes: {count} requests ({count/total_reqs*100:.2f}%) - Beat Hex: {hex(int(size/64)-1).upper().replace('0X', '')}")

if __name__ == '__main__':
    analyze('traces/PT_test/pt_test.trace')
