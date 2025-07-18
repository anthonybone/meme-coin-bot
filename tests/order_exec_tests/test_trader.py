import unittest
from unittest.mock import MagicMock, patch
from order_exec.trader import Trader

class DummyOrderSide:
    BUY = 'buy'
    SELL = 'sell'

class DummyOrderType:
    MARKET = 'market'
    LIMIT = 'limit'

class TestTrader(unittest.TestCase):
    def setUp(self):
        # Patch enums so we don't need the real ones
        patcher_side = patch('order_exec.trader.OrderSide', DummyOrderSide)
        patcher_type = patch('order_exec.trader.OrderType', DummyOrderType)
        self.addCleanup(patcher_side.stop)
        self.addCleanup(patcher_type.stop)
        patcher_side.start()
        patcher_type.start()
        # Mock exchange client
        self.mock_client = MagicMock()
        self.trader = Trader(self.mock_client)

    def test_buy_market_order_success(self):
        self.mock_client.create_order.return_value = {'id': 1, 'status': 'filled'}
        result = self.trader.buy('SHIB/USDT', 100)
        self.mock_client.create_order.assert_called_once_with(
            symbol='SHIB/USDT',
            order_type=DummyOrderType.MARKET,
            side=DummyOrderSide.BUY,
            amount=100,
            price=None
        )
        self.assertEqual(result, {'id': 1, 'status': 'filled'})

    def test_buy_limit_order_success(self):
        self.mock_client.create_order.return_value = {'id': 2, 'status': 'open'}
        result = self.trader.buy('SHIB/USDT', 50, price=0.00001)
        self.mock_client.create_order.assert_called_once_with(
            symbol='SHIB/USDT',
            order_type=DummyOrderType.LIMIT,
            side=DummyOrderSide.BUY,
            amount=50,
            price=0.00001
        )
        self.assertEqual(result, {'id': 2, 'status': 'open'})

    def test_buy_invalid_amount(self):
        result = self.trader.buy('SHIB/USDT', 0)
        self.assertIsNone(result)
        result = self.trader.buy('SHIB/USDT', -5)
        self.assertIsNone(result)
        result = self.trader.buy('SHIB/USDT', 'bad')
        self.assertIsNone(result)

    def test_buy_invalid_price(self):
        result = self.trader.buy('SHIB/USDT', 10, price=-1)
        self.assertIsNone(result)
        result = self.trader.buy('SHIB/USDT', 10, price='bad')
        self.assertIsNone(result)

    def test_buy_exception(self):
        self.mock_client.create_order.side_effect = Exception("API error")
        result = self.trader.buy('SHIB/USDT', 10)
        self.assertIsNone(result)

    def test_sell_market_order_success(self):
        self.mock_client.create_order.return_value = {'id': 3, 'status': 'filled'}
        result = self.trader.sell('SHIB/USDT', 100)
        self.mock_client.create_order.assert_called_once_with(
            symbol='SHIB/USDT',
            order_type=DummyOrderType.MARKET,
            side=DummyOrderSide.SELL,
            amount=100,
            price=None
        )
        self.assertEqual(result, {'id': 3, 'status': 'filled'})

    def test_sell_limit_order_success(self):
        self.mock_client.create_order.return_value = {'id': 4, 'status': 'open'}
        result = self.trader.sell('SHIB/USDT', 50, price=0.00002)
        self.mock_client.create_order.assert_called_once_with(
            symbol='SHIB/USDT',
            order_type=DummyOrderType.LIMIT,
            side=DummyOrderSide.SELL,
            amount=50,
            price=0.00002
        )
        self.assertEqual(result, {'id': 4, 'status': 'open'})

    def test_sell_invalid_amount(self):
        result = self.trader.sell('SHIB/USDT', 0)
        self.assertIsNone(result)
        result = self.trader.sell('SHIB/USDT', -5)
        self.assertIsNone(result)
        result = self.trader.sell('SHIB/USDT', 'bad')
        self.assertIsNone(result)

    def test_sell_invalid_price(self):
        result = self.trader.sell('SHIB/USDT', 10, price=-1)
        self.assertIsNone(result)
        result = self.trader.sell('SHIB/USDT', 10, price='bad')
        self.assertIsNone(result)

    def test_sell_exception(self):
        self.mock_client.create_order.side_effect = Exception("API error")
        result = self.trader.sell('SHIB/USDT', 10)
        self.assertIsNone(result)