import pandas as pd
from pandas_datareader import data as web

# Stooq often uses tickers like "aapl.us"
df = web.DataReader("aapl.us", "stooq")   # returns OHLCV
df = df.sort_index()                      # stooq often comes newest->oldest
print(df.tail())
