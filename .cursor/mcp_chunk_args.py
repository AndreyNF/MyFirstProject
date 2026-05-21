#!/usr/bin/env python3
"""Print MCP args JSON for chunk index (for agent relay)."""
import json
import sys
from pathlib import Path

idx = int(sys.argv[1])
p = Path(f"/workspace/.cursor/mcp_args_only_{idx:02d}.json")
if not p.exists():
    # fallback regenerate
    BLOB = sys.argv[2] if len(sys.argv) > 2 else None
    data = json.loads((Path("/workspace/.cursor/repub4k") / f"chunk-{idx:02d}.json").read_text(encoding="utf-8"))
    args = {"chunk": data["chunk"]}
    if BLOB:
        args["blob_id"] = BLOB
    if data.get("finalize"):
        args["finalize"] = True
else:
    args = json.loads(p.read_text(encoding="utf-8"))
sys.stdout.write(json.dumps(args, ensure_ascii=False))
