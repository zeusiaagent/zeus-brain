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

# 6. Critical Logs (Filtered)
LOG_FILE="/tmp/openclaw/openclaw-$(date +%Y-%m-%d).log"
if [ -f "$LOG_FILE" ]; then
    # Conta apenas erros reais, ignorando ruído comum
    CRITICAL_COUNT=$(grep "ERROR\|FATAL" "$LOG_FILE" | grep -v "429" | grep -v "403" | grep -v "no TTY" | grep -v "jq: error" | grep -v "systemctl" | grep -v "No such file or directory" | grep -v "command not found" | grep -v "externally-managed-environment" | wc -l)
    
    if [ "$CRITICAL_COUNT" -gt 5 ]; then
        ALERTS+="\n❌ Logs: $CRITICAL_COUNT CRITICAL errors detected today"
    fi
fi

# Final Report
if [ -n "$ALERTS" ]; then
    echo -e "🚨 Monitor Zeus — $DATE$ALERTS"
else
    echo "NO_REPLY"
fi
