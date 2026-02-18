#!/bin/bash
# crypto_fetch.sh - Script fiável para obter preços crypto + Fear & Greed

echo "=== Crypto Fetch $(date -Iseconds) ==="

# BTC via Coinbase
echo "Fetching BTC..."
BTC_DATA=$(curl -s "https://api.coinbase.com/v2/prices/BTC-USD/spot" 2>/dev/null)
if echo "$BTC_DATA" | grep -q '"amount"'; then
    BTC_PRICE=$(echo "$BTC_DATA" | grep -oP '"amount":"\K[0-9.]+')
    echo "BTC: $BTC_PRICE"
else
    echo "BTC: ERROR"
fi

# ETH via Coinbase
echo "Fetching ETH..."
ETH_DATA=$(curl -s "https://api.coinbase.com/v2/prices/ETH-USD/spot" 2>/dev/null)
if echo "$ETH_DATA" | grep -q '"amount"'; then
    ETH_PRICE=$(echo "$ETH_DATA" | grep -oP '"amount":"\K[0-9.]+')
    echo "ETH: $ETH_PRICE"
else
    echo "ETH: ERROR"
fi

# KAS via CoinGecko
echo "Fetching KAS..."
KAS_DATA=$(curl -s "https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=usd" 2>/dev/null)
if echo "$KAS_DATA" | grep -q '"usd"'; then
    KAS_PRICE=$(echo "$KAS_DATA" | grep -oP '"usd":\K[0-9.]+')
    echo "KAS: $KAS_PRICE"
else
    echo "KAS: ERROR"
fi

# FLUX via Binance
echo "Fetching FLUX..."
FLUX_DATA=$(curl -s "https://api.binance.com/api/v3/ticker/price?symbol=FLUXUSDT" 2>/dev/null)
if echo "$FLUX_DATA" | grep -q '"price"'; then
    FLUX_PRICE=$(echo "$FLUX_DATA" | grep -oP '"price":"\K[0-9.]+')
    echo "FLUX: $FLUX_PRICE"
else
    echo "FLUX: ERROR"
fi

# Fear & Greed via alternative.me
echo "Fetching Fear & Greed..."
FNG_DATA=$(curl -s "https://api.alternative.me/fng/?limit=1" 2>/dev/null)
if echo "$FNG_DATA" | grep -q '"value"'; then
    FNG_VALUE=$(echo "$FNG_DATA" | sed -n 's/.*"value": "\([0-9]*\)".*/\1/p')
    FNG_CLASS=$(echo "$FNG_DATA" | sed -n 's/.*"value_classification": "\([^"]*\)".*/\1/p')
    echo "FNG: $FNG_VALUE ($FNG_CLASS)"
else
    echo "FNG: ERROR"
fi

# Guardar em JSON
OUTPUT="{\"timestamp\":\"$(date -Iseconds)\",\"btc\":\"${BTC_PRICE:-null}\",\"eth\":\"${ETH_PRICE:-null}\",\"kas\":\"${KAS_PRICE:-null}\",\"flux\":\"${FLUX_PRICE:-null}\",\"fng\":\"${FNG_VALUE:-null}\",\"fng_class\":\"${FNG_CLASS:-null}\"}"
echo "$OUTPUT" > ~/.openclaw/workspace/finance/current_prices.json
echo "Saved to finance/current_prices.json"
