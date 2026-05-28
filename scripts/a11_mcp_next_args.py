#!/usr/bin/env python3
"""Print arguments JSON for blob step N. Usage: a11_mcp_next_args.py <step> [blob_id]"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from a11_blob_mcp_steps import build_steps  # noqa: E402


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: a11_mcp_next_args.py <step> [blob_id]", file=sys.stderr)
        return 2
    idx = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    steps = build_steps()
    if idx < 0 or idx >= len(steps):
        return 1
    st = steps[idx]
    args: dict = {"chunk": st["chunk"]}
    if idx == 0:
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
    if idx == len(steps) - 1:
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
