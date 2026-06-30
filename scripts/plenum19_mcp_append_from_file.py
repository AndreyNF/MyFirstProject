#!/usr/bin/env python3
"""Load wordpress_content_blob_append args from JSON file path; print for agent MCP call.

Usage:
  python3 plenum19_mcp_append_from_file.py /tmp/step.json

Stdout is exact JSON for mcp_call_tool arguments (parse with json.loads, do NOT edit).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: plenum19_mcp_append_from_file.py ARGS.json", file=sys.stderr)
        return 2
    args = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
