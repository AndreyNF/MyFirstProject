#!/usr/bin/env python3
"""Emit MCP append args for subs 01-11 (agent calls mcp_call_tool per line)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = sys.argv[1] if len(sys.argv) > 1 else ""
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end = int(sys.argv[3]) if len(sys.argv) > 3 else 11

for i in range(start, end + 1):
    args = json.loads(Path(f"/tmp/a16-subs-call-{i:02d}.json").read_text(encoding="utf-8"))
    if BLOB and i < 11:
        args["blob_id"] = BLOB
    print(json.dumps({"step": i, "arguments": args}, ensure_ascii=False))
