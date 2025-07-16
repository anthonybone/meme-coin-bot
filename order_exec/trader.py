import logging
from utils.enums import OrderSide, OrderType

class Trader:
    def __init__(self, exchange_client):
        self.exchange_client = exchange_client
        self.logger = logging.getLogger(__name__)

    # Price is optional for market orders, but required for limit orders.
    def buy(self, symbol, amount, price=None):
        try:
            # Example: Place a market or limit buy order
            order = self.exchange_client.create_order(
                symbol=symbol,
                order_type=OrderType.LIMIT if price else OrderType.MARKET,
                side=OrderSide.BUY,
                amount=amount,
                price=price
            )
            self.logger.info(f"Buy order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Buy order failed: {e}")
            return None

    def sell(self, symbol, amount, price=None):
        try:
            # Example: Place a market or limit sell order
            order = self.exchange_client.create_order(
                symbol=symbol,
                order_type=OrderType.LIMIT if price else OrderType.MARKET,
                side=OrderSide.SELL,
                amount=amount,
                price=price
            )
            self.logger.info(f"Sell order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Sell order failed: {e}")
            return None