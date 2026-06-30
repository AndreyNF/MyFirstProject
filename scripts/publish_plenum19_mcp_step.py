#!/usr/bin/env python3
"""Emit wordpress_content_blob_append args for plenum19 page."""
from __future__ import annotations

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/.cursor/plenum19-blob-calls")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: publish_plenum19_mcp_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    path = CHUNK_DIR / f"{step:02d}.json"
    if not path.is_file():
        print(f"missing {path}", file=sys.stderr)
        return 2
    args = json.loads(path.read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            print("blob_id required for step > 0", file=sys.stderr)
            return 2
        args["blob_id"] = blob_id
        args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
