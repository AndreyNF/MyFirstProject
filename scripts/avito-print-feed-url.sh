#!/usr/bin/env bash
# Print public URLs for Avito autoload feed (after git push).
set -euo pipefail
REPO="${AVITO_FEED_REPO:-AndreyNF/MyFirstProject}"
FILE="avito/autoload/legis24-new-ads.xml"
BRANCH="${1:-$(git branch --show-current 2>/dev/null || echo main)}"
echo "Feed URL (branch: $BRANCH):"
echo "https://raw.githubusercontent.com/${REPO}/${BRANCH}/${FILE}"
echo ""
echo "Stable (main):"
echo "https://raw.githubusercontent.com/${REPO}/main/${FILE}"
