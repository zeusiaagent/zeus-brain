const fs = require('fs');
const https = require('https');

const urls = {
    BTC: 'https://api.coinbase.com/v2/prices/BTC-USD/spot',
    ETH: 'https://api.coinbase.com/v2/prices/ETH-USD/spot',
    KAS: 'https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=usd',
    FLUX: 'https://api.binance.com/api/v3/ticker/price?symbol=FLUXUSDT'
};

const lastPricesFile = 'finance/last_prices.json';

function fetchUrl(url) {
    const options = {
        headers: { 'User-Agent': 'Mozilla/5.0 (Node.js script)' }
    };
    return new Promise((resolve, reject) => {
        https.get(url, options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    resolve(JSON.parse(data));
                } catch (e) {
                    reject(new Error(`Failed to parse JSON from ${url}: ${data.substring(0, 100)}`));
                }
            });
            res.on('error', reject);
        }).on('error', reject);
    });
}

async function run() {
    try {
        console.log('Fetching prices...');
        const [btc, eth, kas, flux] = await Promise.all([
            fetchUrl(urls.BTC),
            fetchUrl(urls.ETH),
            fetchUrl(urls.KAS),
            fetchUrl(urls.FLUX)
        ]);

        console.log('Prices fetched.');

        // Extract prices safely
        const prices = {};
        
        try { prices.BTC = parseFloat(btc.data.amount); } catch(e) { console.error('Error parsing BTC:', e); }
        try { prices.ETH = parseFloat(eth.data.amount); } catch(e) { console.error('Error parsing ETH:', e); }
        try { prices.KAS = parseFloat(kas.kaspa.usd); } catch(e) { console.error('Error parsing KAS:', JSON.stringify(kas)); }
        try { prices.FLUX = parseFloat(flux.price); } catch(e) { console.error('Error parsing FLUX:', e); }

        prices.timestamp = new Date().toISOString();

        let lastPrices = {};
        if (fs.existsSync(lastPricesFile)) {
            try {
                lastPrices = JSON.parse(fs.readFileSync(lastPricesFile, 'utf8'));
            } catch (e) {
                console.error('Error reading last prices file, starting fresh.');
            }
        }

        const alerts = [];
        const changes = {};

        for (const [coin, price] of Object.entries(prices)) {
            if (coin === 'timestamp') continue;
            
            if (isNaN(price)) {
                changes[coin] = 'ERR';
                continue;
            }

            const lastPrice = lastPrices[coin];
            if (lastPrice && !isNaN(lastPrice)) {
                const change = ((price - lastPrice) / lastPrice) * 100;
                changes[coin] = change.toFixed(2);
                if (Math.abs(change) > 5) {
                    alerts.push(`${coin}: ${change > 0 ? '+' : ''}${change.toFixed(2)}% ($${lastPrice} -> $${price})`);
                }
            } else {
                changes[coin] = 'INIT';
            }
        }

        fs.writeFileSync(lastPricesFile, JSON.stringify(prices, null, 2));

        if (alerts.length > 0) {
            console.log(`⚠️ **ALERTA VOLATILIDADE**\n${alerts.join('\n')}`);
        } else {
            console.log(`✅ Mercado Estável. Variações: BTC ${changes.BTC}%, ETH ${changes.ETH}%, KAS ${changes.KAS}%, FLUX ${changes.FLUX}%`);
        }

    } catch (error) {
        console.error('Critical Error:', error.message);
    }
}

run();