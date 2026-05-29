#!/usr/bin/env python3
"""Emit one JSON line per blob append step for agent mcp_call_tool loop."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB_ID = sys.argv[1] if len(sys.argv) > 1 else ""
BASE = Path("/workspace/.cursor/b1-blob-mcp")


def load_args(step: int, blob_id: str) -> dict:
    d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    return args


def main() -> int:
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 11
    for step in range(start, end + 1):
        print(json.dumps({"step": step, "arguments": load_args(step, BLOB_ID)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
