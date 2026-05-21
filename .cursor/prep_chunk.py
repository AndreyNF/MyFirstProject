#!/usr/bin/env python3
"""Upload one 4k chunk via args file — prints index for logging."""
import json
import sys
from pathlib import Path

READY = Path("/workspace/.cursor/mcp4k_ready")
idx = int(sys.argv[1])
args = json.loads((READY / f"args_{idx:02d}.json").read_text(encoding="utf-8"))
Path("/workspace/.cursor/CURRENT_MCP_INVOKE.json").write_text(
    json.dumps(
        {
            "server": "Kovcheg",
            "toolName": "wordpress_content_blob_append",
            "arguments": args,
        },
        ensure_ascii=False,
    ),
    encoding="utf-8",
)
print(json.dumps({"index": idx, "len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
