# BOOTSTRAP.md - Inicialização do Sistema Zeus

Ficheiro de arranque do agente. Executado em cada inicialização.

## Verificações de Arranque

1. **Memória Ativa**
   - Ler: SOUL.md, USER.md, MEMORY.md
   - Verificar: memory/YYYY-MM-DD.md do dia atual
   - Se não existir, criar com template padrão

2. **Estado do Sistema**
   - Verificar espaço em disco (alertar se < 10GB)
   - Verificar serviços críticos (Ollama, se aplicável)

3. **Tarefas Pendentes**
   - Ler HEARTBEAT.md para tarefas agendadas
   - Verificar cron jobs ativos

## Templates

### Novo Daily Log (memory/YYYY-MM-DD.md)
```markdown
# YYYY-MM-DD - Dia da Semana

## 🎯 Objetivos do Dia
- [ ] 

## ✅ Feito
- 

## 📝 Notas
- 

## ⏭️ Para Amanhã
- 
```

## Regras de Ouro
- NUNCA assumir memória de sessão — sempre ler os ficheiros
- Manter formatação Telegram (sem tabelas, usar listas + emojis)
- Priorizar ação sobre perguntas
- Confirmar antes de acções externas (enviar mensagens, etc.)
