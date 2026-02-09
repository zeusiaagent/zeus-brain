#!/bin/bash
# Zeus Cleanup Script
# Executed daily at 04:00

echo "[$(date)] Starting Cleanup..."

# 1. Clean old sessions (>7 days)
find /home/clopes/.openclaw/agents/main/sessions/ -name "*.jsonl" -mtime +7 -print -delete >> /tmp/zeus_cleanup.log

# 2. Clean old daily memory (>30 days)
# Nota: Manter MEMORY.md principal! Apenas apagar datas antigas.
find /home/clopes/.openclaw/workspace/memory/ -name "20*.md" -mtime +30 -print -delete >> /tmp/zeus_cleanup.log

# 3. Clean temporary logs (>3 days)
find /tmp/ -name "openclaw*.log" -mtime +3 -print -delete >> /tmp/zeus_cleanup.log

echo "[$(date)] Cleanup Complete. Space freed." >> /tmp/zeus_cleanup.log
