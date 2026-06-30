#!/bin/bash
# Prints chunk index for agent MCP loop (chunks 9-29)
BLOB=$(cat /workspace/.cursor/blob-id.txt)
for i in $(seq 9 29); do
  printf '%02d\n' "$i"
done
