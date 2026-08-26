#!/usr/bin/env python3
"""Print wordpress_content_blob_append arguments JSON for step N to stdout."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_print_step_args.py STEP", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    path = Path(f"/tmp/obysk-mcp-step-{step:02d}.json")
    if not path.is_file():
        print(f"missing {path}; run obysk_prepare_all_steps.py first", file=sys.stderr)
        return 1
    args = json.loads(path.read_text(encoding="utf-8"))
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
