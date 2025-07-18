import unittest
from data_fetch.mock_exchange import MockExchange
from strategy.market_scanner import MarketScanner

class TestMarketScanner(unittest.TestCase):
    def setUp(self):
        self.exchange = MockExchange()
        self.scanner = MarketScanner(self.exchange)

    def test_get_all_tickers(self):
        tickers = self.scanner.get_all_tickers()
        print("[INFO] Meme coin tickers:", tickers)
        self.assertIsInstance(tickers, list)
        self.assertIn('SHIB/USDT', tickers)
        self.assertIn('DOGE/USDT', tickers)
        self.assertIn('PEPE/USDT', tickers)
        self.assertIn('FLOKI/USDT', tickers)
        self.assertIn('WIF/USDT', tickers)
        self.assertIn('MOON/USDT', tickers)
        self.assertIn('RUG/USDT', tickers)

    def test_get_all_tickers_not_empty(self):
        tickers = self.scanner.get_all_tickers()
        self.assertTrue(len(tickers) > 0)


    # Add more tests for your scanner logic as needed

if __name__ == '__main__':
    unittest.main()