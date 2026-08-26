#!/usr/bin/env python3
"""Emit MCP args for vs-kompensaciya blob chunk. Usage: vs-komp-mcp-emit.py STEP [BLOB_ID]"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vs-komp-blob-mcp")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs-komp-mcp-emit.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
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
