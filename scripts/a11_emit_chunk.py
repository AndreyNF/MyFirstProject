#!/usr/bin/env python3
"""Emit MCP args for A11 blob chunk. Usage: a11_emit_chunk.py <0-3> [blob_id]"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/.cursor")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: a11_emit_chunk.py <0-3> [blob_id]", file=sys.stderr)
        return 2
    i = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    ch = (ROOT / f"a11-chunk-{i}.txt").read_text(encoding="utf-8")
    args: dict = {"chunk": ch}
    if i == 0:
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
    if i == 3:
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
