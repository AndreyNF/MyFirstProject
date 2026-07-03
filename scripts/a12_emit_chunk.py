#!/usr/bin/env python3
"""Emit MCP args JSON for A12 blob chunk index (0-3)."""
import json
import sys

i = int(sys.argv[1])
args = json.load(open(f"/workspace/.cursor/a12-blob-calls/{i:02d}.json", encoding="utf-8"))
if len(sys.argv) > 2:
    args["blob_id"] = sys.argv[2]
    args.pop("reset", None)
print(json.dumps(args, ensure_ascii=False))
