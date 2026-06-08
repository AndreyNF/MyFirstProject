#!/usr/bin/env python3
"""Print one MCP append arguments JSON for step N (agent passes to mcp_call_tool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = sys.argv[2] if len(sys.argv) > 2 else ""
STEP = int(sys.argv[1])
path = Path(f"/tmp/vs-komp-live-step{STEP}.json")
if not path.is_file():
    path = Path(f"/tmp/vs-komp-payload-{STEP}.json")
    args = json.loads(path.read_text(encoding="utf-8"))
    if STEP > 0 and BLOB:
        args["blob_id"] = BLOB
        args.pop("reset", None)
else:
    args = json.loads(path.read_text(encoding="utf-8"))
print(json.dumps(args, ensure_ascii=False))
