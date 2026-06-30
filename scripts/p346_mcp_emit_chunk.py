#!/usr/bin/env python3
"""Print one chunk's MCP args as JSON for wordpress_content_blob_append."""
import json
import sys

i = int(sys.argv[1])
args = json.load(open(f"/tmp/p346_mcp_args_{i}.json"))
args["blob_id"] = "VaOvf9QTcc9n91BIotGCs2O"
print(json.dumps(args, ensure_ascii=False))
