import ccxt # (unified API wrapper for many exchanges)
import os
from dotenv import load_dotenv

load_dotenv() # loads env vars from .env

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
API_PASSPHRASE = os.getenv("API_PASSPHRASE")

exchange = ccxt.coinbase({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'password': API_PASSPHRASE,
    'enableRateLimit': True,
})

def get_price(symbol='SHIB/USDT'):
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        print(f"[ERROR] Fetching price failed: {e}")
        return None
