# bot.py

from data_fetch.fetcher import get_price
from strategy.basic_strategy import basic_threshold_strategy

symbol = 'SHIB/USDT'
price = get_price(symbol)

action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
print(f"[DECISION] {symbol} price: {price}; {action.upper()}")
