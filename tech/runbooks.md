# Runbooks Técnicos

## Procedimento Browser Headless (Fiável)
Quando for necessário ler sites complexos (SPA/JS) que o `web_fetch` falha:

1.  **Iniciar:** `openclaw browser start profile="openclaw"`
2.  **Navegar:** `openclaw browser open targetUrl="..." profile="openclaw"`
3.  **Ler:** `openclaw browser snapshot format="aria" profile="openclaw"` (Para texto/estrutura)
4.  **Ver:** `openclaw browser screenshot profile="openclaw"` (Opcional)

*Nota: Não confiar na execução automática implícita. Ser explícito no START.*
