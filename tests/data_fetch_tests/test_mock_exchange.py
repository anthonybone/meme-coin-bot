import unittest
from data_fetch.mock_exchange import MockExchange

class TestMockExchange(unittest.TestCase):
    def setUp(self):
        self.exchange = MockExchange()

    def test_fetch_ticker_returns_last(self):
        symbol = 'SHIB/USD'
        ticker = self.exchange.fetch_ticker(symbol)
        self.assertIn('last', ticker)
        self.assertIsInstance(ticker['last'], float)
        self.assertGreaterEqual(ticker['last'], 0.00001)
        self.assertLessEqual(ticker['last'], 0.00005)

    def test_create_order_market(self):
        order = self.exchange.create_order(
            symbol='SHIB/USD',
            order_type='market',
            side='buy',
            amount=100
        )
        self.assertIn('id', order)
        self.assertEqual(order['symbol'], 'SHIB/USD')
        self.assertEqual(order['type'], 'market')
        self.assertEqual(order['side'], 'buy')
        self.assertEqual(order['amount'], 100)
        self.assertIn('price', order)
        self.assertEqual(order['status'], 'mocked')

    def test_create_order_limit(self):
        order = self.exchange.create_order(
            symbol='DOGE/USDT',
            order_type='limit',
            side='sell',
            amount=50,
            price=0.00003
        )
        self.assertEqual(order['symbol'], 'DOGE/USDT')
        self.assertEqual(order['type'], 'limit')
        self.assertEqual(order['side'], 'sell')
        self.assertEqual(order['amount'], 50)
        self.assertEqual(order['price'], 0.00003)
        self.assertEqual(order['status'], 'mocked')

    def test_create_order_price_fallback(self):
        # If price is not given, should fallback to fetch_ticker
        order = self.exchange.create_order(
            symbol='BTC/USDT',
            order_type='market',
            side='buy',
            amount=1
        )
        self.assertIsInstance(order['price'], float)
        self.assertGreaterEqual(order['price'], 0.00001)
        self.assertLessEqual(order['price'], 0.00005)

if __name__ == "__main__":
    unittest.main()