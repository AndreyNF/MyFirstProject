
#!/bin/bash
# MCP upload must be done via mcp_call_tool in Cursor agent
# Chunks: /workspace/.cursor/payload4k/chunk-{0..20}.json
# 1. wordpress_content_blob_append chunk-0.json (reset=true)
# 2. wordpress_content_blob_append chunk-1..19.json (blob_id=...)
# 3. wordpress_content_blob_append chunk-20.json (blob_id=..., finalize=true)
# 4. wordpress_update_page_from_blob page_id=323 blob_id=... status=publish excerpt=... slug=...
echo "Use mcp_call_tool, not shell"
