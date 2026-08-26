#!/usr/bin/env python3
"""Load MCP append args for steps 2-4 from prepared JSON files."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def load_step(step: int, blob_id: str) -> dict:
    p = Path(f"/workspace/.cursor/blob-args-gumanizaciya/chunk-0{step}.json")
    d = json.loads(p.read_text(encoding="utf-8"))
    args = {"chunk": d["chunk"], "blob_id": blob_id}
    if d.get("finalize"):
        args["finalize"] = True
    if "PLACEHOLDER" in args["chunk"]:
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")
    return args


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: gum_mcp_upload_remaining.py STEP BLOB_ID", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2]
    args = load_step(step, blob_id)
    out = Path(f"/tmp/gum-mcp-step{step}-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
