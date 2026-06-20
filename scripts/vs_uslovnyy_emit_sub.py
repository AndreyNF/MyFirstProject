#!/usr/bin/env python3
"""Emit MCP append args for one sub-chunk step (stdout = arguments JSON only)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def main() -> int:
    step = int(sys.argv[1])
    s = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {"blob_id": ""}
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = s["blob_id"]
        args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
