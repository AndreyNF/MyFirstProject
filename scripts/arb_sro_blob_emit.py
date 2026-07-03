#!/usr/bin/env python3
"""Emit wordpress_content_blob_append args for arb-sro 2k chunk N (1-43)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "9GPJWFouleTtzarVf3xgZwnY"
DIR = Path("/tmp/arb-sro-2k")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: arb_sro_blob_emit.py CHUNK_INDEX", file=sys.stderr)
        return 2
    i = int(sys.argv[1])
    d = json.loads((DIR / f"{i:02d}.json").read_text(encoding="utf-8"))
    args = {"blob_id": BLOB, "chunk": d["chunk"], "finalize": bool(d.get("finalize", False))}
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
