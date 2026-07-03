#!/usr/bin/env python3
"""Load vs-komp blob append args for step N; write to /tmp for agent mcp_call_tool.

Usage:
  python3 scripts/vs-komp-mcp-run-step.py STEP [BLOB_ID]

Prints absolute path to args JSON. Agent: json.load(path) → mcp_call_tool Kovcheg wordpress_content_blob_append.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vs-komp-blob-mcp")


def load_step(step: int, blob_id: str = "") -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            raise SystemExit(f"blob_id required for step {step}")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs-komp-mcp-run-step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    out = Path(f"/tmp/vs-komp-mcp-run-step{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    meta = {
        "path": str(out),
        "step": step,
        "chunk_len": len(args["chunk"]),
        "reset": bool(args.get("reset")),
        "finalize": bool(args.get("finalize")),
        "blob_id": args.get("blob_id"),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
