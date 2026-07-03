#!/bin/bash
# Upload google-earth blob chunks via Kovcheg MCP (agent must call mcp per step).
# Prints step metadata; agent reads args from /tmp/ge-mcp-step{N}.json and calls mcp_call_tool.
set -euo pipefail
STEP="${1:-0}"
BLOB_ID="${2:-}"
python3 /workspace/scripts/ge_mcp_run_step.py "$STEP" $BLOB_ID
echo "MCP_ARGS=/tmp/ge-mcp-run-step$(printf '%02d' "$STEP").json"
