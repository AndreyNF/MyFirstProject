#!/bin/bash
# Helper: print MCP args file path per step for agent loop
BLOB_ID="${1:-}"
for i in 0 1 2 3 4 5 6; do
  if [ "$i" -eq 0 ]; then
    python3 /workspace/scripts/fns_mcp_invoke_step.py "$i" > "/tmp/fns_step_${i}.json"
  else
    python3 /workspace/scripts/fns_mcp_invoke_step.py "$i" "$BLOB_ID" > "/tmp/fns_step_${i}.json"
  fi
  echo "step=$i file=/tmp/fns_step_${i}.json bytes=$(wc -c < "/tmp/fns_step_${i}.json")"
done
