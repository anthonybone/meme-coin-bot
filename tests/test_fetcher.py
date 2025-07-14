from data_fetch.fetcher import get_price

def test_get_price(symbol='SHIB/USDT'):
    price = get_price(symbol)
    if price:
        print(f"[INFO] Current price of {symbol}: {price}")
    else:
        print(f"[WARN] Could not retrieve price for {symbol}")

# Add future test functions below
def test_multiple_prices():
    for symbol in ['DOGE/USDT', 'SHIB/USDT', 'BTC/USDT']:
        test_get_price(symbol)

# Run tests manually here (main block)
if __name__ == "__main__":
    test_get_price()         # Single test
    test_multiple_prices()   # Test several tickers
