#!/bin/bash
# Zeus Server Monitor v2.0
# Smart monitoring (ignores noise)

ALERTS=""
DATE=$(date "+%Y-%m-%d %H:%M")

# 1. Gateway Status (Port Check)
if ! ss -tlnp | grep -q ":18789"; then
    ALERTS+="\n❌ Gateway: Port 18789 is CLOSED (Service Down)"
fi

# 2. Ollama Check
if ! curl -s --max-time 5 http://localhost:11434/api/tags > /dev/null; then
    ALERTS+="\n❌ Ollama: API not responding"
fi

# 3. Disk Space (Root)
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -gt 85 ]; then
    ALERTS+="\n❌ Disk: High usage (${DISK_USAGE}%)"
fi

# 4. RAM Check
RAM_AVAIL=$(free -m | awk '/^Mem:/ {print $7}')
if [ "$RAM_AVAIL" -lt 4000 ]; then
    ALERTS+="\n❌ RAM: Low memory (${RAM_AVAIL}MB)"
fi

# 5. GPU Check
if command -v nvidia-smi &> /dev/null; then
    GPU_TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)
    if [ "$GPU_TEMP" -gt 85 ]; then
        ALERTS+="\n❌ GPU: Overheating (${GPU_TEMP}°C)"
    fi
fi

# 6. Critical Logs (Filtered) - Only last hour
LOG_FILE="/tmp/openclaw/openclaw-$(date +%Y-%m-%d).log"
if [ -f "$LOG_FILE" ]; then
    # Conta apenas erros da última hora, ignorando ruído e erros antigos de sandbox
    ONE_HOUR_AGO=$(date -d '1 hour ago' "+%Y-%m-%dT%H:%M" 2>/dev/null || date -v-1H "+%Y-%m-%dT%H:%M" 2>/dev/null || echo "")
    if [ -n "$ONE_HOUR_AGO" ]; then
        CRITICAL_COUNT=$(grep "ERROR\|FATAL" "$LOG_FILE" | grep -A100000 "$ONE_HOUR_AGO" | grep -v "429\|403\|no TTY\|jq: error\|systemctl\|No such file\|command not found\|externally-managed-environment\|Sandbox workspace\|Path escapes sandbox" | wc -l)
        
        if [ "$CRITICAL_COUNT" -gt 3 ]; then
            ALERTS+="\n❌ Logs: $CRITICAL_COUNT CRITICAL errors in last hour"
        fi
    fi
fi

# Final Report
if [ -n "$ALERTS" ]; then
    echo -e "🚨 Monitor Zeus — $DATE$ALERTS"
else
    echo "NO_REPLY"
fi
