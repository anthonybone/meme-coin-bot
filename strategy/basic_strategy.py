# BUY/SELL/HOLD
from utils.enums import OrderSide

def basic_threshold_strategy(price, buy_threshold, sell_threshold):
    """
    Determines whether to buy, sell, or hold based on the current price and given thresholds.

    Args:
        price (float or None): The current price of the asset. If None, the function will return HOLD.
        buy_threshold (float): The price below which a BUY signal is triggered.
        sell_threshold (float): The price above which a SELL signal is triggered.

    Returns:
        OrderSide: BUY if price < buy_threshold, SELL if price > sell_threshold, otherwise HOLD.
    """
    if price is None:
        # If price data is unavailable, hold position to avoid making uninformed trades
        return OrderSide.HOLD
    if price < buy_threshold:
        return OrderSide.BUY
    elif price > sell_threshold:
        return OrderSide.SELL
    else:
        return OrderSide.HOLD