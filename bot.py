# bot.py
import argparse
import os
from data_fetch.fetcher import Fetcher
from strategy.basic_strategy import basic_threshold_strategy
from order_exec.trader import Trader
from data_fetch.mock_exchange import MockExchange
from utils.enums import OrderSide
import logging
from pythonjsonlogger import jsonlogger

# Remove any existing handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# File handler (JSON)
file_handler = logging.FileHandler('bot.log')
file_formatter = jsonlogger.JsonFormatter()
file_handler.setFormatter(file_formatter)

# Console handler (plain text)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)

logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])

def main():
    parser = argparse.ArgumentParser(description="Meme Coin Trading Bot")
    parser.add_argument("--amount", type=float, help="Trade amount (overrides TRADE_AMOUNT env variable)")
    args = parser.parse_args()

    # Use CLI arg if provided, else env variable, else default
    amount = args.amount if args.amount is not None else float(os.getenv(
        "TRADE_AMOUNT", 1000))
    
    # Initialize the mock exchange client and fetcher
    exchange_client = MockExchange()
    fetcher = Fetcher(exchange_client)
    trader = Trader(exchange_client)

    # Define the trading symbol and thresholds
    symbol = 'SHIB/USDT'
    buy_threshold = float(os.getenv("BUY_THRESHOLD", 0.000008))
    sell_threshold = float(os.getenv("SELL_THRESHOLD", 0.000012))

    # Fetch the current price of the symbol
    try:
        price = fetcher.get_price(symbol)
    except Exception as e:
        logging.error(f"Error fetching price for {symbol}: {e}")
        return

    # Determine the action based on the strategy
    action = basic_threshold_strategy(price, buy_threshold, sell_threshold)
    logging.info(f"[DECISION] {symbol} price: {price}; action: {action.value}")

    if action == OrderSide.BUY:
        trader.buy(symbol, amount)
        logging.info(f"Placing buy order for {symbol} at {price} with amount {amount}")
    elif action == OrderSide.SELL:
        trader.sell(symbol, amount)
        logging.info(f"Placing sell order for {symbol} at {price} with amount {amount}")
    else:
        logging.info(f"Holding position for {symbol}")

if __name__ == "__main__":
    main()