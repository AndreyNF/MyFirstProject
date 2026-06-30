#!/usr/bin/env python3
"""Print wordpress_content_blob_append arguments JSON for one step (0-3)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STEP = int(sys.argv[1]) if len(sys.argv) > 1 else 0
BLOB_ID = sys.argv[2] if len(sys.argv) > 2 else None
path = Path(f"/workspace/.cursor/a11-mcp-step-{STEP}.json")
if not path.is_file():
    path = Path(f"/workspace/.cursor/a11-blob-call-{STEP}.json")
args = json.loads(path.read_text(encoding="utf-8"))
if STEP > 0 and BLOB_ID:
    args["blob_id"] = BLOB_ID
    args.pop("reset", None)
sys.stdout.write(json.dumps(args, ensure_ascii=False))
