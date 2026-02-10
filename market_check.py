import json
import os
import sys
import subprocess

# File path
file_path = 'finance/last_prices.json'

# URLs
urls = {
    'BTC': 'https://api.coinbase.com/v2/prices/BTC-USD/spot',
    'ETH': 'https://api.coinbase.com/v2/prices/ETH-USD/spot',
    'KAS': 'https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=usd',
    'FLUX': 'https://api.binance.com/api/v3/ticker/price?symbol=FLUXUSDT'
}

def get_price(symbol, url):
    try:
        # Using curl to avoid python generic SSL/User-Agent issues in some envs
        result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
        data = json.loads(result.stdout)
        
        if 'coinbase' in url:
            return float(data['data']['amount'])
        elif 'binance' in url:
            return float(data['price'])
        elif 'coingecko' in url:
            return float(data['kaspa']['usd'])
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

def main():
    # Ensure directory exists
    os.makedirs('finance', exist_ok=True)

    # Load last prices
    last_prices = {}
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                last_prices = json.load(f)
        except:
            pass

    current_prices = {}
    alerts = []
    summary_lines = []

    print("Fetching prices...")
    for symbol, url in urls.items():
        price = get_price(symbol, url)
        if price is None:
            continue
            
        current_prices[symbol] = price
        
        old_price = last_prices.get(symbol)
        
        if old_price:
            diff = price - old_price
            pct_change = (diff / old_price) * 100
            
            direction = "📈" if pct_change > 0 else "📉"
            summary_lines.append(f"{symbol}: ${price:.4f} ({direction} {pct_change:+.2f}%)")
            
            if abs(pct_change) > 5.0:
                alerts.append(f"🚨 **{symbol}** moveu {pct_change:+.2f}% (Agora: ${price:.4f}, Antes: ${old_price:.4f})")
        else:
            summary_lines.append(f"{symbol}: ${price:.4f} (Novo)")

    # Save current prices
    with open(file_path, 'w') as f:
        json.dump(current_prices, f, indent=2)

    # Output for the agent to read
    print("\n--- REPORT ---")
    if alerts:
        print("\n".join(alerts))
        print("\nDetalles:")
    
    print("\n".join(summary_lines))
    
    if not alerts and summary_lines:
        print("\n✅ Estável (<5%)")

if __name__ == "__main__":
    main()
