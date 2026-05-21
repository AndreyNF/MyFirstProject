#!/usr/bin/env python3
"""Print MCP args JSON for chunk index — agent pipes to mcp_call_tool."""
import json
import sys
from pathlib import Path

idx = int(sys.argv[1])
blob = sys.argv[2] if len(sys.argv) > 2 else None
p = Path(f"/workspace/.cursor/ready_{idx:02d}.json")
if not p.exists():
    p = Path(f"/workspace/.cursor/repub4k/chunk-{idx:02d}.json")
    data = json.loads(p.read_text(encoding="utf-8"))
    args = {"chunk": data["chunk"]}
    if idx == 0:
        args["reset"] = True
    elif blob:
        args["blob_id"] = blob
    if data.get("finalize"):
        args["finalize"] = True
else:
    args = json.loads(p.read_text(encoding="utf-8"))
    if blob:
        args["blob_id"] = blob
sys.stdout.write(json.dumps(args, ensure_ascii=False))
