# Example: enums for order side and type
from enum import Enum

class OrderSide(Enum):
    BUY = 'BUY'
    SELL = 'SELL'
    HOLD = 'HOLD'

class OrderType(Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'