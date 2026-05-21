#!/usr/bin/env python3
"""Extract MCP arguments dict from prepared chunk file."""
import json
import sys
from pathlib import Path

idx = int(sys.argv[1])
args = json.loads(
    Path(f"/workspace/.cursor/mcp4k_ready/args_{idx:02d}.json").read_text(encoding="utf-8")
)
sys.stdout.write(json.dumps(args, ensure_ascii=False))
