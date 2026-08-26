#!/usr/bin/env python3
"""Print MCP append args JSON for VPR chunk step (02-06)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

STEP = sys.argv[1]
path = Path(f"/workspace/.cursor/vpr-mcp-payload-{STEP}.json")
print(path.read_text(encoding="utf-8"))
