import json

# Current prices from APIs
data = {'BTC': 67313.64, 'ETH': 1968.735, 'KAS': 0.03207176, 'FLUX': 0.0704}

# Load last prices
with open('finance/last_prices.json', 'r') as f:
    last = json.load(f)

diff = {}
alert = False

print('Current Prices:', data)
print('Last Prices:', last)
print('---')

for asset in ['BTC', 'ETH', 'KAS', 'FLUX']:
    old = last[asset]
    new = data[asset]
    change = abs((new - old) / old * 100)
    diff[asset] = change
    print(f'{asset}: {change:.2f}%')
    if change > 5:
        alert = True
        print(f'ALERT: {asset} exceeded 5% change')

print('---')

if alert:
    print('NOTIFYING TELEGRAM')
else:
    print('No alerts')