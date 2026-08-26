#!/usr/bin/env python3
"""Load NIDO blob append args for step N and print MCP envelope JSON to stdout."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

BLOB_ID = "1OF8HZflckhF6GgqfAQKQu"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: nido_kovcheg_mcp_run_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else BLOB_ID
    out = subprocess.check_output(
        ["python3", "/workspace/scripts/nido_mcp_call_append.py", str(step), blob_id],
        text=True,
    )
    args = json.loads(out)
    envelope = {
        "server": "Kovcheg",
        "toolName": "wordpress_content_blob_append",
        "arguments": args,
    }
    sys.stdout.write(json.dumps(envelope, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
