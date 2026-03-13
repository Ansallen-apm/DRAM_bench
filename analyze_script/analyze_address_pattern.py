import sys

def analyze_addresses(filepath):
    addresses = []

    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts: continue

            addr_hex = parts[1]
            addr = int(addr_hex, 16)
            addresses.append(addr)

    print(f"Analyzed {len(addresses)} addresses.")

    # Calculate strides
    strides = []
    for i in range(1, len(addresses)):
        strides.append(addresses[i] - addresses[i-1])

    stride_counts = {}
    for stride in strides:
        stride_counts[stride] = stride_counts.get(stride, 0) + 1

    print("\nTop 5 Strides:")
    for stride, count in sorted(stride_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  Stride {stride} (0x{abs(stride):x}): {count} times ({count/len(strides)*100:.2f}%)")

    # Analyze if it's interleaved
    print("\nInterleaved Streams Analysis:")
    for k in range(1, 9):
        # Look at striding between every k elements
        k_strides = []
        for i in range(k, len(addresses)):
            k_strides.append(addresses[i] - addresses[i-k])

        k_stride_counts = {}
        for stride in k_strides:
            k_stride_counts[stride] = k_stride_counts.get(stride, 0) + 1

        top_k_stride = max(k_stride_counts.items(), key=lambda x: x[1])
        print(f"  Step {k} Top Stride: {top_k_stride[0]} (0x{abs(top_k_stride[0]):x}) - {top_k_stride[1]} times ({top_k_stride[1]/len(k_strides)*100:.2f}%)")

if __name__ == '__main__':
    analyze_addresses('traces/PT_test/pt_test.trace')
