import argparse
import sys
import os

# Add src to path if needed, or assume running from root
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from config import load_config, load_mapping
from mapper import AddressMapper
from dram_sim import DRAMController

class TraceReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration

        parts = line.strip().split()
        if not parts:
            return self.__next__()

        type_str = parts[0]
        addr_str = parts[1]
        size_pow2 = int(parts[2])
        burst_code = parts[3]

        is_write = 'W' in type_str
        address = int(addr_str, 16)
        burst_count = int(burst_code, 16) + 1

        return {
            'is_write': is_write,
            'address': address,
            'size': 2**size_pow2,
            'burst_count': burst_count
        }

def main():
    parser = argparse.ArgumentParser(description='Simple DRAM Simulator')
    parser.add_argument('--config', required=True, help='Path to timing config JSON')
    parser.add_argument('--mapping', required=True, help='Path to address mapping JSON')
    parser.add_argument('--trace', required=True, help='Path to trace file')
    parser.add_argument('--policy', default='FIFO', choices=['FIFO', 'PageHitFirst'], help='Scheduling policy')
    parser.add_argument('--queue_depth', type=int, default=16, help='Command queue depth')

    args = parser.parse_args()

    # Load Configs
    try:
        config = load_config(args.config)
        mapping = load_mapping(args.mapping)
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return

    # Initialize Components
    mapper = AddressMapper(mapping)
    controller = DRAMController(config, mapper, scheduler_type=args.policy, queue_depth=args.queue_depth)

    # Trace Reader
    trace_reader = TraceReader(args.trace)
    trace_iter = iter(trace_reader)

    print(f"Starting simulation with {args.config} and {args.mapping}")
    print(f"Policy: {args.policy}, Queue Depth: {args.queue_depth}")

    # Simulation Loop
    next_req = next(trace_iter, None)

    while next_req is not None or len(controller.queue) > 0:
        # Fill Queue
        while next_req is not None and len(controller.queue) < args.queue_depth:
            controller.queue.append(next_req)
            next_req = next(trace_iter, None)

        # Run Simulator Step
        controller.tick()

    # Stats Calculation
    stats = controller.stats
    # Total cycles should account for the last data transfer completion
    total_cycles = max(controller.current_time, controller.data_bus_free_time)
    # Avoid div by zero
    total_cycles = max(1, total_cycles)

    freq_mhz = config['ClockFrequencyMHz']
    cycle_time_ns = 1000.0 / freq_mhz
    total_time_ns = total_cycles * cycle_time_ns
    total_time_sec = total_time_ns / 1e9

    bw_gbs = (stats['total_bytes'] / 1e9) / total_time_sec if total_time_sec > 0 else 0
    utilization = (stats['bus_busy_cycles'] / total_cycles) * 100

    print("\nSimulation Results:")
    print(f"Total Cycles: {total_cycles}")
    print(f"Total Bytes: {stats['total_bytes']}")
    print(f"Bandwidth: {bw_gbs:.2f} GB/s")
    print(f"Utilization: {utilization:.2f} %")
    print("-" * 30)
    print(f"Page Hits: {stats['page_hits']}")
    print(f"Page Misses: {stats['page_misses']}")
    print(f"Page Conflicts: {stats['page_conflicts']}")

if __name__ == "__main__":
    main()
