import json
import math

# LP4_16_cfg.json content
base_config = {
    "Description": "LPDDR4-6400 Timing Configuration (16-bit)",
    "ClockFrequencyMHz": 3200,
    "Prefetch": 16,
    "BitWidth": 16,
    "tRP": 60,
    "tRCD": 60,
    "tCL": 60,
    "tCWL": 56,
    "tRAS": 140,
    "tRC": 200,
    "tWR": 60,
    "tCCD": 16,
    "tWTR": 10,
    "tRTW": 14,
    "tRRD": 20,
    "tFAW": 80
}

def scale_config(base, new_freq_mhz, new_desc, bit_width):
    ratio = new_freq_mhz / base["ClockFrequencyMHz"]
    new_cfg = base.copy()
    new_cfg["Description"] = new_desc
    new_cfg["ClockFrequencyMHz"] = new_freq_mhz
    new_cfg["BitWidth"] = bit_width

    # Scale timing parameters (rounding up to nearest integer to be safe)
    timing_params = ["tRP", "tRCD", "tCL", "tCWL", "tRAS", "tRC", "tWR", "tCCD", "tWTR", "tRTW", "tRRD", "tFAW"]
    for param in timing_params:
        new_cfg[param] = math.ceil(base[param] * ratio)

    return new_cfg

# Generate LP4-4266 configs
freq_lp4_4266 = 2133
for bw in [16, 32, 64]:
    desc = f"LPDDR4-4266 Timing Configuration ({bw}-bit)"
    cfg = scale_config(base_config, freq_lp4_4266, desc, bw)
    with open(f"configs/LP4_4266_{bw}_cfg.json", "w") as f:
        json.dump(cfg, f, indent=4)
        f.write("\n")


# Generate LP5-8533 configs
freq_lp5_8533 = 4266
for bw in [16, 32, 64]:
    desc = f"LPDDR5-8533 Timing Configuration ({bw}-bit)"
    cfg = scale_config(base_config, freq_lp5_8533, desc, bw)
    with open(f"configs/LP5_8533_{bw}_cfg.json", "w") as f:
        json.dump(cfg, f, indent=4)
        f.write("\n")
