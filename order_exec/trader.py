import logging
from utils.enums import OrderSide, OrderType

class Trader:
    """
    Trader is responsible for executing buy and sell orders using the provided exchange client.

    Attributes:
        exchange_client: The exchange client instance used to place orders.
        logger: Logger instance for logging order actions and errors.
    """
    def __init__(self, exchange_client):
        """
        Initializes the Trader with a given exchange client.

        Args:
            exchange_client: An exchange client instance that implements create_order().
        """
        self.exchange_client = exchange_client
        self.logger = logging.getLogger(__name__)

    # Price is optional for market orders, but required for limit orders.
    def buy(self, symbol, amount, price=None):
        """
        Places a buy order (market or limit) for the specified symbol and amount.

        Args:
            symbol (str): The trading pair symbol.
            amount (float): The amount to buy.
            price (float, optional): The price for a limit order. If None, places a market order.

        Returns:
            dict or None: The order details if successful, None otherwise.
        """
        if not self._validate_amount_price(amount, price, "buy"):
            return None
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
        """
        Places a sell order (market or limit) for the specified symbol and amount.

        Args:
            symbol (str): The trading pair symbol.
            amount (float): The amount to sell.
            price (float, optional): The price for a limit order. If None, places a market order.

        Returns:
            dict or None: The order details if successful, None otherwise.
        """
        if not self._validate_amount_price(amount, price, "sell"):
            return None
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
        
    def _validate_amount_price(self, amount, price, action_type):
        """
        Helper function to validate amount and price.

        Args:
            amount (float): The amount to trade.
            price (float or None): The price for a limit order.
            action_type (str): 'buy' or 'sell' for error messages.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            self.logger.error(f"Invalid {action_type} amount: {amount}")
            return False
        if price is not None and (not isinstance(price, (int, float)) or price <= 0):
            self.logger.error(f"Invalid {action_type} price: {price}")
            return False
        return True