#!/bin/bash
# crypto_fetch.sh - Script fiável para obter preços crypto + Fear & Greed
# Formato: Standard Zeus 2025

DATA_HORA=$(date +%d/%m/%Y' às '%H:%M)

# BTC via Coinbase
BTC_DATA=$(curl -s "https://api.coinbase.com/v2/prices/BTC-USD/spot" 2>/dev/null)
if echo "$BTC_DATA" | grep -q '"amount"'; then
    BTC_PRICE=$(echo "$BTC_DATA" | grep -oP '"amount":"\K[0-9.]+')
    BTC_FMT=$(echo "$BTC_PRICE" | awk '{printf "%.0f", $1}' | sed 's/\B(?=(\d{3})+(?!\d))/./g')
else
    BTC_FMT="ERROR"
fi

# ETH via Coinbase
ETH_DATA=$(curl -s "https://api.coinbase.com/v2/prices/ETH-USD/spot" 2>/dev/null)
if echo "$ETH_DATA" | grep -q '"amount"'; then
    ETH_PRICE=$(echo "$ETH_DATA" | grep -oP '"amount":"\K[0-9.]+')
    ETH_FMT=$(echo "$ETH_PRICE" | awk '{printf "%.0f", $1}' | sed 's/\B(?=(\d{3})+(?!\d))/./g')
else
    ETH_FMT="ERROR"
fi

# KAS via CoinGecko
KAS_DATA=$(curl -s "https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=usd" 2>/dev/null)
if echo "$KAS_DATA" | grep -q '"usd"'; then
    KAS_PRICE=$(echo "$KAS_DATA" | grep -oP '"usd":\K[0-9.]+')
    KAS_FMT=$(echo "$KAS_PRICE" | awk '{printf "%.4f", $1}' | sed 's/\./,/')
else
    KAS_FMT="ERROR"
fi

# FLUX via Binance
FLUX_DATA=$(curl -s "https://api.binance.com/api/v3/ticker/price?symbol=FLUXUSDT" 2>/dev/null)
if echo "$FLUX_DATA" | grep -q '"price"'; then
    FLUX_PRICE=$(echo "$FLUX_DATA" | grep -oP '"price":"\K[0-9.]+')
    FLUX_FMT=$(echo "$FLUX_PRICE" | awk '{printf "%.4f", $1}' | sed 's/\./,/')
else
    FLUX_FMT="ERROR"
fi

# Fear & Greed via alternative.me
FNG_DATA=$(curl -s "https://api.alternative.me/fng/?limit=1" 2>/dev/null)
if echo "$FNG_DATA" | grep -q '"value"'; then
    FNG_VALUE=$(echo "$FNG_DATA" | sed -n 's/.*"value": "\([0-9]*\)".*/\1/p')
    FNG_CLASS=$(echo "$FNG_DATA" | sed -n 's/.*"value_classification": "\([^"]*\)".*/\1/p')
    
    # Emoji baseado no valor
    if [ "$FNG_VALUE" -le 20 ]; then FNG_EMOJI="😱"
    elif [ "$FNG_VALUE" -le 40 ]; then FNG_EMOJI="😰"
    elif [ "$FNG_VALUE" -le 60 ]; then FNG_EMOJI="😐"
    elif [ "$FNG_VALUE" -le 80 ]; then FNG_EMOJI="😊"
    else FNG_EMOJI="🤑"; fi
else
    FNG_VALUE="N/A"
    FNG_CLASS="N/A"
    FNG_EMOJI="⚠️"
fi

# Guardar em JSON (para uso interno)
OUTPUT="{\"timestamp\":\"$(date -Iseconds)\",\"btc\":\"${BTC_PRICE:-null}\",\"eth\":\"${ETH_PRICE:-null}\",\"kas\":\"${KAS_PRICE:-null}\",\"flux\":\"${FLUX_PRICE:-null}\",\"fng\":\"${FNG_VALUE:-null}\",\"fng_class\":\"${FNG_CLASS:-null}\"}"
echo "$OUTPUT" > ~/.openclaw/workspace/finance/current_prices.json

# Output formatado para Telegram
cat << EOF
🌅 *Crypto Morning Brief* — _$DATA_HORA_

💰 *Mercado:*
• BTC: *$BTC_FMT* USD
• ETH: *$ETH_FMT* USD
• KAS: *$KAS_FMT* USD
• FLUX: *$FLUX_FMT* USD

📊 *Fear & Greed:* $FNG_EMOJI *$FNG_VALUE*/100 — _$FNG_CLASS_

_Dados: Coinbase, CoinGecko, Binance, Alternative.me_
EOF
