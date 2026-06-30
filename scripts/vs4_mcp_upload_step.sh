#!/usr/bin/env bash
# Print MCP args JSON for step N (0-4). Agent: mcp_call_tool Kovcheg wordpress_content_blob_append
set -euo pipefail
STEP="${1:?step 0-4}"
BLOB_ID="${2:-}"
python3 - "$STEP" "$BLOB_ID" <<'PY'
import json, sys
from pathlib import Path
step = int(sys.argv[1])
blob_id = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else ""
chunks = Path("/workspace/.cursor/vs4-blob-chunks")
chunk = (chunks / f"chunk{step}.txt").read_text(encoding="utf-8")
args = {"chunk": chunk}
if step == 0:
    args["reset"] = True
elif blob_id:
    args["blob_id"] = blob_id
if step == 4:
    args["finalize"] = True
if "PLACEHOLDER" in args.get("chunk", ""):
    raise SystemExit("refusing placeholder chunk")
print(json.dumps(args, ensure_ascii=False))
PY
