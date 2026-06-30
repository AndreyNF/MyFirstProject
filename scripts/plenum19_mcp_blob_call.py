#!/usr/bin/env python3
"""Load blob append args and emit as JSON for mcp_call_tool (arguments only).

Usage:
  python3 plenum19_mcp_blob_call.py STEP [BLOB_ID]

Agent: mcp_call_tool Kovcheg wordpress_content_blob_append with json.loads(stdout)
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path("/workspace/scripts/publish_plenum19_mcp_step.py")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: plenum19_mcp_blob_call.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    cmd = ["python3", str(SCRIPT), str(step)]
    if step > 0:
        if len(sys.argv) < 3:
            print("blob_id required for step > 0", file=sys.stderr)
            return 2
        cmd.append(sys.argv[2])
    args = json.loads(subprocess.check_output(cmd, text=True))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
