# BUY/SELL/HOLD
from utils.enums import OrderSide

def basic_threshold_strategy(price, buy_threshold, sell_threshold):
    if price is None:
        return OrderSide.HOLD
    if price < buy_threshold:
        return OrderSide.BUY
    elif price > sell_threshold:
        return OrderSide.SELL
    else:
        return OrderSide.HOLD