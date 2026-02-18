# MEMORY.md - Sistema Zeus

**Modo:** 100% Local (Google Cloud desativado 2026-02-10)  
**Dados:** data/saude.json, data/investimentos.json, memory/

## 🎯 Automações Ativas
| Hora | Tarefa |
|------|--------|
| 04:00 | Manutenção (cleanup.sh) |
| 08:30 | BioMonitor (Oura → JSON) |
| 09:00 | Super Briefing (Crypto + Tech) |
| 18:00 | IA Watch (Tech monitoring) |
| 22:00 | Check-in (Diário + Protocolo) |
| 23:00 | GitHub Backup (automático) |
| Dom 20:00 | Resumo Semanal |
| 60min | Crypto Sentinel (BTC/ETH/KAS/FLUX) |
| 2h | Monitor Servidor |

## 📝 Standard de Formatação 2025
**Referência:** `memory/skills/formatting-standard.md`  
**Aplica-se a:** Todos os relatórios agendados  
**Princípios:** Linguagem clara, frases curtas (máx 20 palavras), emojis estratégicos, negrito em valores, itálico em fontes

## ⚙️ Model Chain (2026-02-18)
**Primary:** moonshot/kimi-k2.5 (262K ctx, €0.6/€2.5)  
**Fallbacks:** ollama/qwen3-coder:30b → xai/grok-4-1-fast-reasoning  
**Aliases:** kimi, local, grok, glm, sonnet, haiku, opus

### Modelos Claude Disponíveis
• `sonnet` → Claude Sonnet 4.6 (Anthropic)  
• `haiku` → Claude Haiku 4.5 (Anthropic)  
• `opus` → Claude Opus 4.6 (Anthropic)

## 📋 Regras Críticas
- ❌ Sem tabelas markdown em Telegram (use listas + emojis)
- ❌ Sem passwords hardcoded (use tech/secrets/)
- ✅ Lê SOUL.md + USER.md + memory/YYYY-MM-DD.md sempre
