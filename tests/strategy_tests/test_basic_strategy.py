# tests/test_strategy.py

from strategy.basic_strategy import basic_threshold_strategy

def test_basic_threshold_strategy():
    test_cases = [
        (0.000007, 0.000008, 0.000012, 'buy'),
        (0.000009, 0.000008, 0.000012, 'hold'),
        (0.000013, 0.000008, 0.000012, 'sell')
    ]
    for price, buy_th, sell_th, expected in test_cases:
        result = basic_threshold_strategy(price, buy_th, sell_th)
        assert result == expected, f"Expected {expected}, got {result}"

    print("[PASS] basic_threshold_strategy works as expected.")

if __name__ == "__main__":
    test_basic_threshold_strategy()
