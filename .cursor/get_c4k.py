#!/usr/bin/env python3
"""Load chunk N args as JSON to stdout for MCP relay."""
import json
import sys
from pathlib import Path

idx = int(sys.argv[1])
p = Path(f'/workspace/.cursor/c4k_{idx:02d}.json')
print(p.read_text(encoding='utf-8'))
