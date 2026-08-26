#!/usr/bin/env python3
"""Prepare obysk blob append args for step N (0-17) with blob_id injection."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-5k-upload-state.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_prepare_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    if not blob_id and STATE.is_file():
        blob_id = json.loads(STATE.read_text(encoding="utf-8")).get("blob_id") or ""

    if step == 0:
        path = Path(f"/tmp/obysk-clean-00.json")
    else:
        path = Path(f"/tmp/obysk-clean-mcp-{step:02d}.json")

    args = json.loads(path.read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            raise SystemExit("blob_id required for step > 0")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")

    out = Path("/workspace/.cursor/obysk-mcp-active-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
