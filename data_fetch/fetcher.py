from data_fetch.mock_exchange import MockExchange
import os
from dotenv import load_dotenv

load_dotenv() # loads env vars from .env

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
API_PASSPHRASE = os.getenv("API_PASSPHRASE")

class Fetcher:
    """
    Fetcher is responsible for retrieving market data from the provided exchange client.

    Attributes:
        exchange: An exchange client instance that implements fetch_ticker(symbol).
    """
    def __init__(self, exchange):
        """
        Initializes the Fetcher with a given exchange client.

        Args:
            exchange: An exchange client instance.
        """
        self.exchange = exchange

    def get_price(self, symbol='SHIB/USD'):
        """
        Fetches the latest price for the specified trading symbol.

        Args:
            symbol (str): The trading pair symbol (default: 'SHIB/USD').

        Returns:
            float: The latest price for the symbol, or None if fetching fails.
        """
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker['last']
        except Exception as e:
            print(f"[ERROR] Fetching price failed: {e}")
            return None
