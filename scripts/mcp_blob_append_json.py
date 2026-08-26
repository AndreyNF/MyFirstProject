#!/usr/bin/env python3
"""Load blob append args from JSON file path (argv[1]) and print as single-line JSON."""
from __future__ import annotations

import json
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: mcp_blob_append_json.py ARGS.json", file=sys.stderr)
        return 2
    args = json.loads(open(sys.argv[1], encoding="utf-8").read())
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
