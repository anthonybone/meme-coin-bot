import random

class MockExchange:
    """
    A mock exchange client for simulating price data and order creation.
    Useful for testing trading logic without connecting to a real exchange.
    """
    def fetch_ticker(self, symbol):
        """
        Simulates fetching the latest ticker price for a given symbol.

        Args:
            symbol (str): The trading pair symbol (e.g., 'SHIB/USD').

        Returns:
            dict: A dictionary with the latest price under the 'last' key.
        """
        price = round(random.uniform(0.00001, 0.00005), 8)
        return {'last': price}

    def create_order(self, symbol, order_type, side, amount, price=None):
        """
        Simulates creating an order on the exchange.

        Args:
            symbol (str): The trading pair symbol.
            order_type (str): The type of order (e.g., 'market', 'limit').
            side (str): The side of the order ('buy' or 'sell').
            amount (float): The amount to trade.
            price (float, optional): The price for the order. If not provided, uses the latest price.

        Returns:
            dict: A dictionary representing the mocked order details.
        """
        return {
            'id': random.randint(100000, 999999),
            'symbol': symbol,
            'type': order_type,
            'side': side,
            'amount': amount,
            'price': price or self.fetch_ticker(symbol)['last'],
            'status': 'mocked'
        }