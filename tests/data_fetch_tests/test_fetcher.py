import unittest
from unittest.mock import MagicMock
from data_fetch.fetcher import Fetcher

class TestFetcher(unittest.TestCase):
    def setUp(self):
        # Mock the exchange client
        self.mock_exchange = MagicMock()
        self.fetcher = Fetcher(self.mock_exchange)

    def test_get_price(self):
        self.mock_exchange.fetch_ticker.return_value = {'last': 0.00001}
        price = self.fetcher.get_price('SHIB/USDT')
        self.assertEqual(price, 0.00001)

    def test_multiple_prices(self):
        prices = {'DOGE/USDT': 0.1, 'SHIB/USDT': 0.00001, 'BTC/USDT': 30000}
        def fetch_ticker_side_effect(symbol):
            return {'last': prices[symbol]}
        self.mock_exchange.fetch_ticker.side_effect = fetch_ticker_side_effect

        for symbol, expected_price in prices.items():
            price = self.fetcher.get_price(symbol)
            self.assertEqual(price, expected_price)

if __name__ == "__main__":
    unittest.main()
