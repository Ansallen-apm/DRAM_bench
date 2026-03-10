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
LOG_DIR="LOG"
MAX_JOBS=4

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -o|--opt)
            SCRIPT="src/asyc_parall_opt.py"
            echo "[INFO] Using the optimized caching simulator: $SCRIPT"
            ;;
        -j|--jobs)
            MAX_JOBS="$2"
            shift # past argument
            ;;
        -l|--log_dir)
            LOG_DIR="$2"
            shift # past argument
            ;;
    esac
    shift
done

mkdir -p "$LOG_DIR"

echo "Starting parallel simulation batch..."
echo "Simulator: $SCRIPT"
echo "Max Concurrent Jobs: $MAX_JOBS"
echo "Log Directory: $LOG_DIR"
echo "Total Configs: ${#CONFIGS[@]}"
echo "Total Traces: ${#TRACES[@]}"
echo "=========================================="

# Job control variables
RUNNING_JOBS=0

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
            --interval_us "$INTERVAL_US" \
            --log_dir "$LOG_DIR" &

        RUNNING_JOBS=$((RUNNING_JOBS+1))

        # If we reached MAX_JOBS, wait for any one job to finish before continuing
        if [[ $RUNNING_JOBS -ge $MAX_JOBS ]]; then
            wait -n
            RUNNING_JOBS=$((RUNNING_JOBS-1))
        fi

    done
done

# Wait for remaining background jobs to finish
wait

echo "=========================================="
echo "All parallel simulations completed successfully!"
