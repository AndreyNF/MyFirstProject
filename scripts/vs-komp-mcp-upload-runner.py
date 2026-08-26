#!/usr/bin/env python3
"""Emit MCP append args path for step N (agent calls mcp_call_tool with json.load)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vs-komp-blob-mcp")
BLOB_DEFAULT = ""


def load_step(step: int, blob_id: str) -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            raise SystemExit("blob_id required for step > 0")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs-komp-mcp-upload-runner.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    out = Path(f"/tmp/vs-komp-mcp-runner-step{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
