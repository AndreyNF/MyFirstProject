#!/usr/bin/env python3
"""Load blob append args for step N (0-4). Agent: mcp_call_tool with printed JSON."""
from __future__ import annotations

import json
import sys
from pathlib import Path

DIR = Path("/workspace/.cursor/ks-blob-calls")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: ks_mcp_blob_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = json.loads((DIR / f"{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
