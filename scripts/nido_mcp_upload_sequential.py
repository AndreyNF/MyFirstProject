#!/usr/bin/env python3
"""Load NIDO blob step args and print MCP metadata (agent calls mcp_call_tool per step).

Usage:
  python3 scripts/nido_mcp_upload_sequential.py STEP [BLOB_ID]

Prints path to args JSON on stdout for agent mcp_call_tool invocation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

DIR = Path("/workspace/.cursor/nido-blob-calls")
OUT = Path("/tmp/nido-mcp-active-args.json")


def load_step(step: int, blob_id: str = "") -> dict:
    args = json.loads((DIR / f"call-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: nido_mcp_upload_sequential.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    OUT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "args_path": str(OUT),
                "chunk_len": len(args["chunk"]),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
                "blob_id": args.get("blob_id"),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
