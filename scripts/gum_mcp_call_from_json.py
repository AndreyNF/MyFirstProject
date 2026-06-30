#!/usr/bin/env python3
"""Load MCP append args from JSON path; print as single JSON line for verification."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gum_mcp_call_from_json.py ARGS_JSON", file=sys.stderr)
        return 2
    args = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER")
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
