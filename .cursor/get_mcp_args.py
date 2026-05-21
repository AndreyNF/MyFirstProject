#!/usr/bin/env python3
"""Load chunk N args JSON to stdout for MCP relay."""
import json
import sys
from pathlib import Path

idx = int(sys.argv[1])
args = json.loads(Path(f'/workspace/.cursor/mcp_args_only_{idx:02d}.json').read_text(encoding='utf-8'))
print(json.dumps(args, ensure_ascii=False))
