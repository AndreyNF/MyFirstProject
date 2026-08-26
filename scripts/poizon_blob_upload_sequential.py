#!/usr/bin/env python3
"""Upload POIZON page blob via Kovcheg MCP — one chunk per invocation.

Usage:
  python3 scripts/poizon_blob_upload_sequential.py 0          # chunk 0 (reset)
  python3 scripts/poizon_blob_upload_sequential.py N BLOB_ID  # chunk N with blob_id

Prints JSON arguments for wordpress_content_blob_append.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/poizon-blob-5k")


def main() -> int:
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    elif step > 0:
        if not blob_id:
            print("blob_id required for step > 0", file=sys.stderr)
            return 2
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
