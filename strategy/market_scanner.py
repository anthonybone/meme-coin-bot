def get_all_trading_pairs(exchange):
    exchange.load_markets()
    return list(exchange.symbols)