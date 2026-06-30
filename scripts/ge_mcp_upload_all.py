#!/usr/bin/env python3
"""Upload google-earth blob chunks 0-4 via Kovcheg MCP (agent runs mcp_call_tool per step).

Prints one JSON object per line with step metadata. Agent must call
wordpress_content_blob_append for each step using args from ge_mcp_run_step.py.

This script validates chunks only; MCP calls are done via mcp_call_tool.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/google-earth-blob-mcp")
HTML = Path("/workspace/.cursor/page-content-natasha-google-earth.html")


def main() -> int:
    if not HTML.is_file():
        print(f"Missing {HTML}", file=sys.stderr)
        return 1
    text = HTML.read_text(encoding="utf-8")
    total = 0
    for i in range(5):
        args = json.loads((BASE / f"{i:02d}.json").read_text(encoding="utf-8"))
        total += len(args["chunk"])
        if "PLACEHOLDER" in args.get("chunk", ""):
            print(f"ERROR: placeholder in chunk {i}", file=sys.stderr)
            return 1
    print(json.dumps({"ok": True, "chunks": 5, "total_chars": total, "html_chars": len(text)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
