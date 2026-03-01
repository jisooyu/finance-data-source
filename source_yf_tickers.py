import pandas as pd
import yfinance as yf

t = yf.Ticker("AAPL")

# Prices (pandas)
px = t.history(period="2y", auto_adjust=True)[["Close", "Volume"]]
print(px.tail())

# Fundamentals / financial statements (already DataFrames)
income = t.income_stmt          # annual income statement
balance = t.balance_sheet       # annual balance sheet
cashflow = t.cashflow           # annual cashflow statement

print(income.tail())
