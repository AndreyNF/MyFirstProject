#!/usr/bin/env python3
"""Print MCP envelope for vs-uslovnyy blob step (4c or sub mode).

Usage:
  VS_UPLOAD_MODE=4c python3 scripts/vs_uslovnyy_mcp_invoke_step.py 0
  VS_UPLOAD_MODE=sub python3 scripts/vs_uslovnyy_mcp_invoke_step.py 5 BLOB_ID
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

BASE_4C = Path("/workspace/.cursor/blob-args-vs-uslovnyy")
SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
MODE = os.environ.get("VS_UPLOAD_MODE", "4c")


def load_args(step: int, blob_id: str = "") -> dict:
    if MODE == "4c":
        args = json.loads((BASE_4C / f"chunk-{step:02d}.json").read_text(encoding="utf-8"))
        if step == 0:
            args["reset"] = True
        elif blob_id:
            args["blob_id"] = blob_id
            args.pop("reset", None)
        return args
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs_uslovnyy_mcp_invoke_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_args(step, blob_id)
    out = Path(f"/tmp/vs-mcp-invoke-{step:02d}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "args_path": str(out), "chunk_len": len(args["chunk"]),
                      "reset": bool(args.get("reset")), "finalize": bool(args.get("finalize")),
                      "blob_id": args.get("blob_id")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
