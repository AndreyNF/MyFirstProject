#!/usr/bin/env python3
"""Sequential blob upload for gumanizaciya page via Kovcheg MCP REST bridge.

Reads chunk args from /workspace/.cursor/blob-args-gumanizaciya/chunk-NN.json
and calls wordpress_content_blob_append, then update_page_from_blob + publish.

Requires agent to run via mcp_call_tool — this script prints each step envelope.
Usage: gum_kovcheg_sequential_upload.py STEP [BLOB_ID]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/blob-args-gumanizaciya")


def load_step(step: int, blob_id: str = "") -> dict:
    p = BASE / f"chunk-0{step}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if d.get("reset"):
        args["reset"] = True
    if d.get("finalize"):
        args["finalize"] = True
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
    if "PLACEHOLDER" in args["chunk"]:
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gum_kovcheg_sequential_upload.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    envelope = {
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    out = Path(f"/tmp/gum-envelope-step{step}.json")
    out.write_text(json.dumps(envelope, ensure_ascii=False), encoding="utf-8")
    meta = {
        "step": step,
        "envelope_path": str(out),
        "chunk_len": len(args["chunk"]),
        "blob_id": args.get("blob_id"),
        "reset": bool(args.get("reset")),
        "finalize": bool(args.get("finalize")),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
