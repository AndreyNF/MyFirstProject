#!/usr/bin/env python3
"""Upload remaining sub-chunks 2-13 via stdout JSON lines for agent mcp_call_tool."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "kNrHC826DPUpEOuqgXsYtw2k"
START = int(sys.argv[1]) if len(sys.argv) > 1 else 2
END = int(sys.argv[2]) if len(sys.argv) > 2 else 13

for i in range(START, END + 1):
    args = json.loads(Path(f"/tmp/vs-sub-upload-{i:02d}.json").read_text(encoding="utf-8"))
    args["blob_id"] = BLOB
    print(json.dumps({"step": i, "arguments": args}, ensure_ascii=False))
