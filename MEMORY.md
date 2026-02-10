# MEMORY.md - Sistema Zeus

**Modo:** 100% Local (Google Cloud desativado 2026-02-10)  
**Dados:** data/saude.json, data/investimentos.json, memory/

## 🎯 Automações Ativas
| Hora | Tarefa |
|------|--------|
| 04:00 | Manutenção (cleanup.sh) |
| 07:30 | BioMonitor (Oura → JSON) |
| 08:30 | Super Briefing (Crypto + Tech) |
| 18:00 | IA Watch (Tech monitoring) |
| 22:00 | Check-in (Diário + Protocolo) |
| Dom 20:00 | Resumo Semanal |
| 30min | Crypto Sentinel (BTC/ETH/FLUX) |
| 2h | Monitor Servidor |

## ⚙️ Model Chain (2026-02-10)
**Primary:** ollama/qwen3-coder:30b (Local, 0€)  
**Fallbacks:** Flash → Haiku → Kimi 128k → Sonnet → Pro → Opus

## 📋 Regras Críticas
- ❌ Sem tabelas markdown em Telegram (use listas + emojis)
- ❌ Sem passwords hardcoded (use tech/secrets/)
- ✅ Lê SOUL.md + USER.md + memory/YYYY-MM-DD.md sempre
