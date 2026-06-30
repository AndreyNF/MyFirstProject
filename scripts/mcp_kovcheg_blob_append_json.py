#!/usr/bin/env python3
"""Load wordpress_content_blob_append args from JSON and print for mcp_call_tool."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: mcp_kovcheg_blob_append_json.py ARGS_JSON", file=sys.stderr)
        return 2
    args = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing placeholder chunk")
    # stdout = arguments only (agent passes to mcp_call_tool)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
