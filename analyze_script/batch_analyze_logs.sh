#!/bin/bash

LOG_DIR=${1:-LOG}
REQ_THRESHOLD=${2:-0}

if [ ! -d "$LOG_DIR" ]; then
    echo "Error: Directory $LOG_DIR does not exist."
    exit 1
fi

echo "=========================================================================================="
echo " Batch Analysis of Interval Logs in: $LOG_DIR (Req Threshold <= $REQ_THRESHOLD)"
echo "=========================================================================================="
printf "%-35s | %-6s | %-6s | %-6s | %-6s | %-8s | %-8s\n" "Log File" "Avg %" "P50 %" "Min %" "Max %" "Max Idle" "Starved"
echo "------------------------------------------------------------------------------------------"

for log_file in "$LOG_DIR"/interval_*.log; do
    if [ ! -f "$log_file" ]; then
        continue
    fi

    # Determine directory of this script to safely call the python companion
    SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

    # Use the python script to get a JSON summary
    JSON_OUT=$(python3 "$SCRIPT_DIR/analyze_interval_log.py" --log "$log_file" --req_threshold "$REQ_THRESHOLD" --json)

    # Simple JSON extraction using grep/sed (since jq might not be installed in all sandboxes)
    # E.g., "avg_util": 95.15
    avg=$(echo "$JSON_OUT" | grep -o '"avg_util": [0-9.]*' | awk '{print $2}')
    p50=$(echo "$JSON_OUT" | grep -o '"median_util": [0-9.]*' | awk '{print $2}')
    min=$(echo "$JSON_OUT" | grep -o '"min_util": [0-9.]*' | awk '{print $2}')
    max=$(echo "$JSON_OUT" | grep -o '"max_util": [0-9.]*' | awk '{print $2}')
    max_idle=$(echo "$JSON_OUT" | grep -o '"max_idle_cycles": [0-9]*' | awk '{print $2}')
    starved=$(echo "$JSON_OUT" | grep -o '"starved_count": [0-9]*' | awk '{print $2}')

    filename=$(basename "$log_file")
    # Truncate filename if too long for clean output
    short_filename=$(echo "$filename" | cut -c 1-35)

    if [ -z "$avg" ]; then
        printf "%-35s | %s\n" "$short_filename" "Invalid or empty log"
    else
        printf "%-35s | %-6s | %-6s | %-6s | %-6s | %-8s | %-8s\n" "$short_filename" "$avg" "$p50" "$min" "$max" "$max_idle" "$starved"
    fi
done

echo "=========================================================================================="
echo "Tip: Run 'python3 analyze_script/analyze_interval_log.py --log <file>' for deep dive into a specific log."
