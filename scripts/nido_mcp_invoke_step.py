#!/usr/bin/env python3
"""Print MCP wordpress_content_blob_append arguments for NIDO step N (1-4)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

BLOB_DEFAULT = "1r7otKHJETOIwmvFpuZpdw"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: nido_mcp_invoke_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else BLOB_DEFAULT
    ready = Path(f"/workspace/.cursor/nido-mcp-step{step}-ready.json")
    if ready.is_file():
        args = json.loads(ready.read_text(encoding="utf-8"))
    else:
        out = subprocess.check_output(
            ["python3", "/workspace/scripts/nido_mcp_blob_step.py", str(step), blob_id],
            text=True,
        )
        args = json.loads(out)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
