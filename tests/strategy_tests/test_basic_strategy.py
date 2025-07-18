import unittest
from strategy.basic_strategy import basic_threshold_strategy
from utils.enums import OrderSide

class TestBasicStrategy(unittest.TestCase):
    def test_basic_threshold_strategy(self):
        test_cases = [
            (0.000007, 0.000008, 0.000012, OrderSide.BUY),
            (0.000009, 0.000008, 0.000012, OrderSide.HOLD),
            (0.000013, 0.000008, 0.000012, OrderSide.SELL)
        ]
        for price, buy_th, sell_th, expected in test_cases:
            result = basic_threshold_strategy(price, buy_th, sell_th)
            self.assertEqual(result, expected, f"Expected {expected}, got {result}")


    def test_buy_signal(self):
        price = 0.000007
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, OrderSide.BUY)

    def test_sell_signal(self):
        price = 0.000013
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, OrderSide.SELL)

    def test_hold_signal(self):
        price = 0.000010
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, OrderSide.HOLD)

    def test_none_price(self):
        price = None
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, OrderSide.HOLD)  # Or whatever your function returns for None

if __name__ == '__main__':
    unittest.main()