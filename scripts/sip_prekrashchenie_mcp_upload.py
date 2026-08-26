#!/usr/bin/env python3
"""Emit wordpress_content_blob_append args for sip-prekrashchenie page chunks.

Usage:
  python3 scripts/sip_prekrashchenie_mcp_upload.py STEP [BLOB_ID]

STEP 0-9. Prints one JSON line (arguments only) for mcp_call_tool.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/.cursor/sip-blob-chunks")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: sip_prekrashchenie_mcp_upload.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    chunk_path = CHUNK_DIR / f"chunk{step}.txt"
    if not chunk_path.is_file():
        print(f"missing {chunk_path}", file=sys.stderr)
        return 2
    chunk = chunk_path.read_text(encoding="utf-8")
    args: dict = {"chunk": chunk}
    if step == 0:
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
    else:
        print("blob_id required for step > 0", file=sys.stderr)
        return 2
    if step == 9:
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
