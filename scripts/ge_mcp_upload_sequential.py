#!/usr/bin/env python3
"""Print blob-append arguments JSON for step N (stdout for agent mcp_call_tool).

Usage:
  python3 scripts/ge_mcp_upload_sequential.py STEP [BLOB_ID]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/google-earth-blob-mcp")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: ge_mcp_upload_sequential.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            print("blob_id required for step > 0", file=sys.stderr)
            return 2
        args["blob_id"] = blob_id
        args.pop("reset", None)
    out: dict = {"chunk": args["chunk"]}
    if args.get("reset"):
        out["reset"] = True
    if args.get("blob_id"):
        out["blob_id"] = args["blob_id"]
    if args.get("finalize"):
        out["finalize"] = True
    else:
        out["finalize"] = False
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
