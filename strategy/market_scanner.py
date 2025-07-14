mock_tickers = [
    'SHIB/USDT',
    'DOGE/USDT',
    'PEPE/USDT',
    'FLOKI/USDT',
    'WIF/USDT',
    'MOON/USDT',  # totally fake, fun to mock
    'RUG/USDT',   # simulate a scam coin
]

class MarketScanner:
    def __init__(self, exchange):
        self.exchange = exchange

    def get_all_tickers(self):
        return mock_tickers  # TODO: replace with real exchange call