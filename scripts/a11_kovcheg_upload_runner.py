#!/usr/bin/env python3
"""Emit one-line MCP append payloads (≤8k JSON) for agent mcp_call_tool loop.

Usage:
  python3 scripts/a11_kovcheg_upload_runner.py prepare   # 4×18k from a11-chunk-*.txt
  python3 scripts/a11_kovcheg_upload_runner.py emit 0 [blob_id]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/.cursor")
OUT = Path("/tmp/a11_emit")


def prepare() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for i in range(4):
        chunk = (ROOT / f"a11-chunk-{i}.txt").read_text(encoding="utf-8")
        args: dict = {"chunk": chunk}
        if i == 0:
            args["reset"] = True
        if i == 3:
            args["finalize"] = True
        (OUT / f"step_{i}.json").write_text(
            json.dumps(args, ensure_ascii=False), encoding="utf-8"
        )
    total = sum(len((OUT / f"step_{i}.json").read_text(encoding="utf-8")) for i in range(4))
    print(json.dumps({"ok": True, "steps": 4, "total_json_bytes": total}))
    return 0


def emit(step: int, blob_id: str | None = None) -> int:
    path = OUT / f"step_{step}.json"
    if not path.is_file():
        prepare()
    args = json.loads(path.read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    line = json.dumps(args, ensure_ascii=False)
    # stdout is consumed by agent → mcp_call_tool arguments
    sys.stdout.write(line)
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: prepare | emit STEP [BLOB_ID]", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "prepare":
        return prepare()
    if cmd == "emit":
        step = int(sys.argv[2])
        bid = sys.argv[3] if len(sys.argv) > 3 else None
        return emit(step, bid)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
