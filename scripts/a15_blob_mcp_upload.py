#!/usr/bin/env python3
"""Load blob chunk args from JSON files for sequential MCP upload.

Prints one JSON line per chunk for agent mcp_call_tool(wordpress_content_blob_append).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB_ID = "CDnXxXroQLOOFZ0ff56syCab"
BASE = Path("/workspace/.cursor/a15-blob-calls")


def main() -> int:
    idx = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    if idx < 0 or idx > 8:
        print("Usage: a15_blob_mcp_upload.py <0-8>", file=sys.stderr)
        return 1
    path = BASE / f"{idx:02d}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    args: dict = {"chunk": data["chunk"]}
    if idx == 0:
        args["reset"] = True
    else:
        args["blob_id"] = BLOB_ID
        args["reset"] = False
    if data.get("finalize"):
        args["finalize"] = True
    else:
        args["finalize"] = False
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
