#!/usr/bin/env bash
# Helper: print MCP args for step N (agent calls mcp_call_tool with printed JSON)
set -euo pipefail
STEP="${1:?step index 0-11}"
BLOB_ID="${2:-}"
python3 /workspace/scripts/a11_mcp_next_args.py "$STEP" $BLOB_ID
