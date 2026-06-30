#!/usr/bin/env python3
"""Load blob append args from JSON path; print compact meta (agent calls mcp_call_tool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: ge_mcp_call_append.py ARGS_JSON", file=sys.stderr)
        return 2
    args = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    meta = {
        "chunk_len": len(args["chunk"]),
        "blob_id": args.get("blob_id"),
        "reset": bool(args.get("reset")),
        "finalize": bool(args.get("finalize")),
        "args_path": str(Path(sys.argv[1]).resolve()),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
