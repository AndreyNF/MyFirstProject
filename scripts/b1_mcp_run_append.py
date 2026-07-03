#!/usr/bin/env python3
"""Print JSON args for wordpress_content_blob_append (B1 page)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/b1-blob-ordered")


def main() -> int:
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
