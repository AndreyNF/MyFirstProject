#!/usr/bin/env python3
"""Emit MCP arguments JSON for vs-uslovnyy sub-chunk step N (stdout only)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

READY = Path("/tmp")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs_uslovnyy_emit_mcp_args.py STEP", file=sys.stderr)
        return 2
    step = sys.argv[1]
    path = READY / f"mcp-ready-{step}.json"
    if not path.is_file():
        path = READY / f"vs-upload-{step}.json"
    print(path.read_text(encoding="utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
