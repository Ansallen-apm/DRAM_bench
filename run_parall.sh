#!/bin/bash

# Configuration and Trace Arrays
# Define the configurations and traces you want to run in parallel.
CONFIGS=(
    "configs/LP4_32_cfg.json"
    # "configs/LP4_64_cfg.json"
    # "configs/LP5_32_cfg.json"
)

TRACES=(
    "traces/basic100/sample.trace"
    "traces/basic100/seq_read_64B.trace"
    "traces/basic100/seq_write_64B.trace"
)

# Common parameters
MAPPING="configs/mapping_2ch.json"
QUEUE_DEPTH=64
INTERVAL_US=0.1
POLICY="PageHitFirst"
SCRIPT="src/asyc_parall.py"

# Parse arguments for the -o / --opt flag
for arg in "$@"; do
    if [ "$arg" == "-o" ] || [ "$arg" == "--opt" ]; then
        SCRIPT="src/asyc_parall_opt.py"
        echo "[INFO] Using the optimized caching simulator: $SCRIPT"
    fi
done

echo "Starting parallel simulation batch..."
echo "Simulator: $SCRIPT"
echo "Total Configs: ${#CONFIGS[@]}"
echo "Total Traces: ${#TRACES[@]}"
echo "=========================================="

# Loop through all configurations and traces
for CONFIG in "${CONFIGS[@]}"; do
    for TRACE in "${TRACES[@]}"; do

        echo "Launching: Config=$CONFIG, Trace=$TRACE"

        # Run python in background using &
        python3 "$SCRIPT" \
            --config "$CONFIG" \
            --mapping "$MAPPING" \
            --trace "$TRACE" \
            --policy "$POLICY" \
            --queue_depth "$QUEUE_DEPTH" \
            --interval_us "$INTERVAL_US" &

    done
done

# Wait for all background jobs to finish
wait

echo "=========================================="
echo "All parallel simulations completed successfully!"
