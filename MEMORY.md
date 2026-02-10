# MEMORY.md - Sistema Zeus (Carlos)

## 🧑 Sobre o Carlos
- **Timezone:** Europe/Lisbon
- **Nascido:** 12/06/1964 (61 anos)
- **Localização:** Aveiro, Portugal
- **Estilo:** Direto, eficaz, sem fluff

## 💻 Modelos Ativos (Fev 2026)

### Stack Principal
- **Primary (Qualidade):** anthropic/claude-haiku-4-5
- **Secondary (Rápido/Grátis):** google/gemini-3-flash-preview
- **Fallback Local:** ollama/qwen3-coder:30b

### Tarefas Automáticas
- **Rotinas Leves (Crons):** google-antigravity/gemini-3-pro-low
- **Tarefas Pesadas (Scholar):** ollama/qwen3-coder:30b

## 💻 Hardware
- **CPU:** i7-11700F
- **RAM:** 128GB
- **GPU:** RTX 3090 (24GB VRAM)
- **Disco:** 884GB (27% usado)
- **OS:** Ubuntu no Proxmox

## 📂 Dados & Integrações
- **Google Cloud:** ❌ DESATIVADO (Conta suspensa/falha OAuth)
- **Modo de Operação:** 100% Local
- **Armazenamento:**
  - `data/saude.json` (Biomarkers, Oura)
  - `data/investimentos.json` (Portfolio, Preços)
  - `memory/calendar.md` (Agenda)

## 📋 Regras Telegram (CRÍTICO)
- **NUNCA usar tabelas markdown** (|---|) — Telegram não renderiza
- Listas simples com emojis
- Formato limpo e direto

## 🔐 Security & Best Practices
- **NUNCA hardcoded passwords** em scripts (!!!)
- Chaves sensíveis (Oura, etc) em `tech/secrets/` (fora do git)

## 📅 Automações Configuradas

| Hora | Tarefa | Descrição |
|------|--------|-----------|
| 04:00 | Manutenção | cleanup.sh |
| 07:30 | BioMonitor | Dados saúde (Oura Local) |
| 08:30 | Super Briefing | Crypto + News (Local) |
| 18:00 | IA Watch | Monitoramento tech |
| 22:00 | Check-in | Diário (Local) |
| Domingo 20:00 | Resumo Semanal | Weekly report |
| A cada 30min | Sentinela Crypto | Alertas crypto (BTC, ETH, KAS, FLUX) |
| A cada 2h | Monitor Servidor | Health check |

---

**Última atualização:** 10 Fev 2026, 14:57 UTC
