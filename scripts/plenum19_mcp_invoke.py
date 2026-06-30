#!/usr/bin/env python3
"""Load blob append args for step N; print JSON to stdout for mcp_call_tool."""
from __future__ import annotations

import json
import subprocess
import sys

BLOB_ID = "ph8o2J671wsrttRZq2W7Z"
SCRIPT = "/workspace/scripts/publish_plenum19_mcp_step.py"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: plenum19_mcp_invoke.py STEP", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    out = subprocess.check_output(
        ["python3", SCRIPT, str(step), BLOB_ID] if step > 0 else ["python3", SCRIPT, str(step)],
        text=True,
    )
    args = json.loads(out)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
