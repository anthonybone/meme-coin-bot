# bot.py

from data_fetch.fetcher import Fetcher
from strategy.basic_strategy import basic_threshold_strategy
from order_exec.trader import Trader
from data_fetch.mock_exchange import MockExchange
from utils.enums import OrderSide

exchange_client = MockExchange()
fetcher = Fetcher(exchange_client)
trader = Trader(exchange_client)


symbol = 'SHIB/USDT'
price = fetcher.get_price(symbol)
amount = 1000  # Example amount, adjust as needed

action = basic_threshold_strategy(price, buy_threshold=0.000008, sell_threshold=0.000012)
print(f"[DECISION] {symbol} price: {price}; {action.value}")

if action == OrderSide.BUY:
    # Here you would call the buy method from your Trader class
    trader.buy(symbol, amount)
    print(f"Placing buy order for {symbol} at {price} with amount {amount}")
elif action == OrderSide.SELL:
    # Here you would call the sell method from your Trader class
    trader.sell(symbol, amount)
    print(f"Placing sell order for {symbol} at {price} with amount {amount}")
else:
    print(f"Holding position for {symbol}")
