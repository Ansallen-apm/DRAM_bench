#!/bin/bash

# Default Parameters
# 預設參數
CONFIG="configs/LP4_cfg.json"
MAPPING="configs/mapping.json"
TRACE="traces/sample.trace"
POLICY="FIFO"
QUEUE_DEPTH=16

# Run Simulation
# 執行模擬
echo "Running DRAM Simulator with the following parameters:"
echo "Config: $CONFIG"
echo "Mapping: $MAPPING"
echo "Trace: $TRACE"
echo "Policy: $POLICY"
echo "Queue Depth: $QUEUE_DEPTH"
echo "---------------------------------------------------"

python3 src/main.py --config "$CONFIG" --mapping "$MAPPING" --trace "$TRACE" --policy "$POLICY" --queue_depth "$QUEUE_DEPTH"
