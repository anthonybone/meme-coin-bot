import random

class MockExchange:
    def fetch_ticker(self, symbol):
        # Simulate a price between 0.00001 and 0.00005 for SHIB/USDT
        price = round(random.uniform(0.00001, 0.00005), 8)
        return {'last': price}

    def create_order(self, symbol, type, side, amount, price=None):
        # Simulate order creation
        return {
            'id': random.randint(100000, 999999),
            'symbol': symbol,
            'type': type,
            'side': side,
            'amount': amount,
            'price': price or self.fetch_ticker(symbol)['last'],
            'status': 'mocked'
        }

exchange = MockExchange()

def get_price(symbol='SHIB/USDT'):
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        print(f"[ERROR] Fetching price failed: {e}")
        return None

def mock_trade(symbol='SHIB/USDT', type='limit', side='buy', amount=1000000):
    try:
        order = exchange.create_order(symbol, type, side, amount)
        print(f"Mock trade executed: {order}")
        return order
    except Exception as e:
        print(f"[ERROR] Mock trade failed: {e}")
        return None