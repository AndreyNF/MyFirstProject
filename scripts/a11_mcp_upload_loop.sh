#!/bin/bash
# Print ready_N.json paths for agent MCP loop (3k chunks, 24 parts)
BLOB_ID="${1:-}"
for i in $(seq -w 1 23); do
  echo "/tmp/a11_sub/ready_${i}.json"
done
