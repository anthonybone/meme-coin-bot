import ccxt # (unified API wrapper for many exchanges)
from data_fetch.mock_exchange import MockExchange
import os
from dotenv import load_dotenv

load_dotenv() # loads env vars from .env

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
API_PASSPHRASE = os.getenv("API_PASSPHRASE")

class Fetcher:
    def __init__(self, exchange):
        self.exchange = exchange

    def get_price(self, symbol='SHIB/USDT'):
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker['last']
        except Exception as e:
            print(f"[ERROR] Fetching price failed: {e}")
