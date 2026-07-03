#!/usr/bin/env python3
"""Load MCP append args for step N with blob_id. Usage: step blob_id

Prints JSON args to stdout for agent mcp_call_tool (or validates chunk).
Refuses PLACEHOLDER in chunk.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor")


def load_step(step: int, blob_id: str) -> dict:
    if step == 0:
        args = json.loads((BASE / "mcp-chunk0-call.json").read_text(encoding="utf-8"))
    else:
        d = json.loads((BASE / f"gumanizaciya-mcp-call-{step}.json").read_text(encoding="utf-8"))
        chunk = (d["arguments"] if "arguments" in d else d)["chunk"]
        args = {"chunk": chunk}
        if step == 4:
            args["finalize"] = True
    if step > 0:
        if not blob_id:
            raise SystemExit("blob_id required for step > 0")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")
    return args


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: gumanizaciya_mcp_sequential_call.py STEP BLOB_ID", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2]
    args = load_step(step, blob_id)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
