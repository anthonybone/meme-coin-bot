import unittest
from strategy.basic_strategy import basic_threshold_strategy

class TestBasicStrategy(unittest.TestCase):
    def test_basic_threshold_strategy(self):
        test_cases = [
            (0.000007, 0.000008, 0.000012, 'buy'),
            (0.000009, 0.000008, 0.000012, 'hold'),
            (0.000013, 0.000008, 0.000012, 'sell')
        ]
        for price, buy_th, sell_th, expected in test_cases:
            result = basic_threshold_strategy(price, buy_th, sell_th)
            self.assertEqual(result, expected, f"Expected {expected}, got {result}")


    def test_buy_signal(self):
        price = 0.000007
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, 'buy')

    def test_sell_signal(self):
        price = 0.000013
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, 'sell')

    def test_hold_signal(self):
        price = 0.000010
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, 'hold')

    def test_none_price(self):
        price = None
        action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
        self.assertEqual(action, 'hold')  # Or whatever your function returns for None

if __name__ == '__main__':
    unittest.main()