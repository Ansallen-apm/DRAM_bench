import subprocess
import re

configs = {
    "3200": "configs/LP4_3200_64_cfg.json",
    "4266": "configs/LP4_4266_64_cfg.json",
    "6400": "configs/LP4_64_cfg.json"
}
queue_depths = ["16", "32", "64"]
trace = "traces/seq_read_64B.trace"

def run_sim(cfg_path, q_depth):
    cmd = [
        "python3", "src/main.py",
        "--config", cfg_path,
        "--mapping", "configs/mapping.json",
        "--trace", trace,
        "--policy", "FIFO",
        "--queue_depth", q_depth
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Extract Utilization (%)
        match = re.search(r"Utilization \(利用率\): ([\d\.]+) %", result.stdout)
        if match:
            return match.group(1)
        return "N/A"
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

print("=== Analysis of seq_read_64B (LPDDR4 x64) ===")
print("Queue Depth\tData Rate\tUtilization (%)")
print("-" * 50)

for dr, cfg in configs.items():
    for qd in queue_depths:
        urate = run_sim(cfg, qd)
        print(f"{qd}\t\t{dr}\t\t{urate}%")
