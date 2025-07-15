# BUY/SELL/HOLD

def basic_threshold_strategy(price, buy_threshold, sell_threshold):
    if price is None:
        return 'hold'
    if price < buy_threshold:
        return 'buy'
    elif price > sell_threshold:
        return 'sell'
    else:
        return 'hold'