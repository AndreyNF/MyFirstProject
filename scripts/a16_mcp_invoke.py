#!/usr/bin/env python3
"""Print MCP invoke envelope for wordpress_content_blob_append (step 0-5).

Usage:
  python3 scripts/a16_mcp_invoke.py 0           # reset chunk
  python3 scripts/a16_mcp_invoke.py 3 BLOB_ID   # continuation
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/a16-blob-mcp")


def main() -> int:
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if step == 0:
        args["reset"] = True
        args["finalize"] = False
    else:
        args["blob_id"] = blob_id
        args["finalize"] = bool(d.get("finalize"))
    envelope = {
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    print(json.dumps(envelope, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
