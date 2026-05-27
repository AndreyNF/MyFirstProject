#!/usr/bin/env python3
"""Prepare sequential MCP upload payloads for A15 (chunks 00-08).

Prints one JSON object per line: index, blob_id placeholder, payload dict.
Agent must call wordpress_content_blob_append for each payload via MCP.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/a15-blob-calls")


def main() -> int:
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    blob_id = sys.argv[3] if len(sys.argv) > 3 else ""
    for i in range(start, end + 1):
        d = json.loads((BASE / f"{i:02d}.json").read_text(encoding="utf-8"))
        args: dict = {"chunk": d["chunk"]}
        if i == 0:
            args["reset"] = True
        elif blob_id:
            args["blob_id"] = blob_id
            args["reset"] = False
        if d.get("finalize"):
            args["finalize"] = True
        else:
            args["finalize"] = False
        print(json.dumps({"index": i, "args": args}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
