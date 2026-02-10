# Search Fallback Strategy — Zeus 🌩️

**Data:** 2026-02-10  
**Problema:** Brave Search rate limit (429) afeta automações  
**Solução:** Fallback automático (Brave → Web_Fetch → Silent)

---

## 📋 Automações com Search

| Cron | Hora | Tipo | Status |
|------|------|------|--------|
| **Super Briefing** | 08:30 | News (AI/Crypto) | ✅ Fallback implementado |
| **IA Watch** | 18:00 | AI News | ✅ Fallback implementado |

---

## 🔄 Estratégia de Fallback

### Nível 1: Brave Search (Primário)
```
web_search(query) → 
  OK → Retorna resultados
  429 → Vai para Nível 2
  Outro erro → Vai para Nível 3
```

### Nível 2: Web_Fetch Direto (Sites-chave)
```
Tentaem sequência:
1. https://www.cnbc.com (Business/AI news)
2. https://www.technologyreview.com (MIT Tech Review)
3. https://newsletter.semianalysis.com (SemiAnalysis)
4. https://www.understandingai.org (Understanding AI)

Parse por keywords relevantes → Resume top 3
```

### Nível 3: Silent (NO_REPLY)
```
Se tudo falhar: Envia NO_REPLY (sem error)
Razão: Melhor ter silêncio que aviso de erro recorrente
```

---

## 🛠️ Implementação nos Crons

### Super Briefing (08:30)
```
1. web_search("AI Crypto news last 24 hours")
2. SE 429 → web_fetch(cnbc.com, technologyreview.com)
3. Combine com Coinbase API prices
4. Enviar Telegram com resultado ou "Sem news nova"
```

**Payload Atualizado:** ✅

### IA Watch (18:00)
```
1. web_search("AI LLM breakthroughs latest news")
2. SE 429 → web_fetch(CNBC, MIT, SemiAnalysis, UnderstandingAI)
3. Parse keywords: Claude, OpenAI, DeepSeek, Gemini, LLM
4. Resume top 3, envia '🤖 IA Diário' ou NO_REPLY
```

**Payload Atualizado:** ✅

---

## 📊 Benefícios

✅ **Zero downtime** — Brave falha não derruba automações  
✅ **Qualidade mantida** — Web_fetch retorna conteúdo real (não truncado)  
✅ **Simplicidade** — Sem código extra, apenas instruções ao agentTurn  
✅ **Escalável** — Funciona para futuras automações com search

---

## 🔧 Troubleshooting

### Web_fetch retorna error (403, timeout)
→ Tenta próximo site da lista
→ Se todos falharem, envia NO_REPLY

### Web_fetch retorna 200 mas conteúdo vazio
→ Site pode estar bloqueando scraping
→ Solução: Adicionar user-agent header ou usar RSS feeds

### Performance lenta
→ Web_fetch pode ser lento (2-5s por site)
→ Considerar cache de resultados (<24h)

---

## 📝 Próximos Passos

- [ ] Testar fallback amanhã às 08:30 (Super Briefing)
- [ ] Testar fallback amanhã às 18:00 (IA Watch)
- [ ] Se performance ruim, implementar cache
- [ ] Se web_fetch falhar consistentemente, adicionar RSS feeds
- [ ] Monitorar taxa de "NO_REPLY" (indica problemas)

---

**Última atualização:** 2026-02-10T21:06:20Z (Opus 4.6)
