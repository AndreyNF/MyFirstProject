#!/usr/bin/env python3
"""Load MCP args JSON for chunk index (1-8). Usage: a15_load_mcp_args.py 4"""
import json
import sys
from pathlib import Path

n = int(sys.argv[1])
p = Path(f"/workspace/.cursor/a15-blob-calls/mcp-args/run-{n}.json")
if not p.is_file():
    p = Path(f"/workspace/.cursor/a15-blob-calls/mcp-args/upload-{n:02d}.json")
print(p.read_text(encoding="utf-8"))
