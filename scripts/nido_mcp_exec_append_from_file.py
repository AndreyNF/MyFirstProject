#!/usr/bin/env python3
"""Load blob append args from JSON path; print MCP envelope for agent mcp_call_tool."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: nido_mcp_exec_append_from_file.py ARGS_JSON", file=sys.stderr)
        return 2
    args = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    envelope = {
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    print(json.dumps(envelope, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
