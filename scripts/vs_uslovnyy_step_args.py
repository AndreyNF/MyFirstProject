#!/usr/bin/env python3
"""Print MCP args JSON for sub-chunk STEP (with blob_id from state)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def main() -> int:
    step = int(sys.argv[1])
    s = json.loads(STATE.read_text(encoding="utf-8"))
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = s["blob_id"]
        args.pop("reset", None)
    out = Path(f"/workspace/.cursor/vs-mcp-step{step:02d}-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "path": str(out), "len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
