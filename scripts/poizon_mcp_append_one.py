#!/usr/bin/env python3
"""Print wordpress_content_blob_append arguments for chunk index 1-13."""
import json
import sys

i = int(sys.argv[1])
print(json.dumps(json.load(open(f"/workspace/.cursor/poizon-mcp-args/{i:02d}.json")), ensure_ascii=False))
