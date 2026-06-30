#!/usr/bin/env python3
"""Load blob append args from JSON file and print for mcp_call_tool."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1])
    args = json.loads(path.read_text(encoding="utf-8"))
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
