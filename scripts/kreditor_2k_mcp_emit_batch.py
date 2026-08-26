#!/usr/bin/env python3
"""Emit next N kreditor 2k chunk MCP args (with blob_id) for agent CallDynamicTool."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/kreditor-2k-upload-state.json")
CHUNKS = Path("/workspace/.cursor/kreditor-2k-chunks")


def main() -> int:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    st = json.loads(STATE.read_text(encoding="utf-8"))
    step = st["index"]
    total = st["total"]
    blob_id = st.get("blob_id")
    out = []
    for i in range(step, min(step + n, total)):
        args = json.loads((CHUNKS / f"{i:02d}.json").read_text(encoding="utf-8"))
        if i > 0 and blob_id:
            args["blob_id"] = blob_id
            args.pop("reset", None)
        out.append({"step": i, "arguments": args})
    print(json.dumps({"from_step": step, "count": len(out), "blob_id": blob_id, "items": out}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
