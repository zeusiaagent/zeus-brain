# TOOLS.md - Local Setup

## Hardware
- **Server:** ia-zeus (Proxmox VM, Ubuntu 24.04, i7-11700F, 128GB RAM)
- **GPU:** RTX 3090 (24GB VRAM)
- **Ollama:** http://127.0.0.1:11434

## OpenClaw
- **Dashboard:** http://127.0.0.1:18789
- **Model Chain:** Primary=ollama/qwen3-coder:30b → Flash, Haiku, Kimi, Sonnet, Pro, Opus
- **Heartbeat:** ollama/qwen3-coder:30b (1h, 08:00-23:00)
