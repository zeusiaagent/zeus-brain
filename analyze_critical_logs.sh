#!/bin/bash

# Script para análise profunda de logs em busca de erros CRITICAL
# Criado por Zeus em 2026-02-12

echo "Iniciando análise de logs para erros CRITICAL..."

# Procurar por 'CRITICAL' em todos os arquivos de log em /var/log
sudo find /var/log -type f -exec grep -i 'CRITICAL' {} + | sort | uniq -c | sort -nr | head -n 50 > /home/clopes/.openclaw/workspace/critical_logs_report.txt

echo "Análise concluída. Resultados guardados em /home/clopes/.openclaw/workspace/critical_logs_report.txt"

echo "Abrindo o relatório para visualização..."
cat /home/clopes/.openclaw/workspace/critical_logs_report.txt
