# Meme Coin Bot

A simple trading bot for meme coins, designed for experimentation and learning.  
This bot uses a mock exchange and a basic threshold strategy to decide when to buy, sell, or hold a specified symbol.

## Features

- Fetches the latest price for a configured symbol (default: `SHIB/USD`)
- Makes buy/sell/hold decisions based on configurable price thresholds
- Simulates trades using a mock exchange (no real funds involved)
- Configurable trade amount via environment variable or CLI argument

## Usage

& C:/Python38/python.exe bot.py --amount {amount}

### Prerequisites

- Python 3.7+
- Install dependencies (if any):  
  ```sh
  pip install -r requirements.txt

