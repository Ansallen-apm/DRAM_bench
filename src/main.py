import argparse
import sys
import os

# Add src to path if needed, or assume running from root
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from config import load_config, load_mapping
from mapper import AddressMapper
from dram_sim import DRAMController

class TraceReader:
    """
    Reads and parses trace files.
    讀取並解析 Trace 檔案。
    """
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

        # Format: [R/W]x [Address] [Size_Pow2] [Burst]
        # 格式：[R/W]x [Address] [Size_Pow2] [Burst]
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
    parser.add_argument('--config', required=True, help='Path to timing config JSON (時序設定檔路徑)')
    parser.add_argument('--mapping', required=True, help='Path to address mapping JSON (位址映射檔路徑)')
    parser.add_argument('--trace', required=True, help='Path to trace file (Trace 檔案路徑)')
    parser.add_argument('--policy', default='FIFO', choices=['FIFO', 'PageHitFirst'], help='Scheduling policy (排程策略)')
    parser.add_argument('--queue_depth', type=int, default=16, help='Command queue depth (指令隊列深度)')

    args = parser.parse_args()

    # Load Configs
    # 載入設定
    try:
        config = load_config(args.config)
        mapping = load_mapping(args.mapping)
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return

    # Initialize Components
    # 初始化元件
    mapper = AddressMapper(mapping)
    controller = DRAMController(config, mapper, scheduler_type=args.policy, queue_depth=args.queue_depth)

    # Trace Reader
    # Trace 讀取器
    trace_reader = TraceReader(args.trace)
    trace_iter = iter(trace_reader)

    print(f"Starting simulation with {args.config} and {args.mapping}")
    print(f"Policy: {args.policy}, Queue Depth: {args.queue_depth}")

    # Simulation Loop
    # 模擬迴圈
    next_req = next(trace_iter, None)

    while next_req is not None or len(controller.queue) > 0:
        # Fill Queue
        # 填充隊列
        while next_req is not None and len(controller.queue) < args.queue_depth:
            controller.queue.append(next_req)
            next_req = next(trace_iter, None)

        # Run Simulator Step
        # 執行模擬器步進
        controller.tick()

    # Stats Calculation
    # 統計計算
    stats = controller.stats
    # Total cycles should account for the last data transfer completion
    # 總週期數應包含最後一次資料傳輸完成的時間
    total_cycles = max(controller.current_time, controller.data_bus_free_time)
    # Avoid div by zero
    # 避免除以零
    total_cycles = max(1, total_cycles)

    freq_mhz = config['ClockFrequencyMHz']
    cycle_time_ns = 1000.0 / freq_mhz
    total_time_ns = total_cycles * cycle_time_ns
    total_time_sec = total_time_ns / 1e9

    bw_gbs = (stats['total_bytes'] / 1e9) / total_time_sec if total_time_sec > 0 else 0
    utilization = (stats['bus_busy_cycles'] / total_cycles) * 100
    avg_queue_depth = stats['cumulative_queue_depth'] / stats['queue_depth_samples'] if stats['queue_depth_samples'] > 0 else 0

    print("\nSimulation Results:")
    print(f"Total Cycles (總週期): {total_cycles}")
    print(f"Total Bytes (總位元組): {stats['total_bytes']}")
    print(f"Bandwidth (頻寬): {bw_gbs:.2f} GB/s")
    print(f"Utilization (利用率): {utilization:.2f} %")
    print(f"Average Queue Depth (平均隊列深度): {avg_queue_depth:.2f}")
    print("-" * 30)
    print(f"Page Hits (Page 命中): {stats['page_hits']}")
    print(f"Page Misses (Page 未命中): {stats['page_misses']}")
    print(f"Page Conflicts (Page 衝突): {stats['page_conflicts']}")

if __name__ == "__main__":
    main()
