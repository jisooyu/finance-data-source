import pandas as pd
import yfinance as yf

df = yf.download(
    tickers=["AAPL", "MSFT"],
    start="2020-01-01",
    auto_adjust=True,
    group_by="ticker",
    progress=False,
)

# Example: build a close price dataframe
close = pd.DataFrame({
    "AAPL": df["AAPL"]["Close"],
    "MSFT": df["MSFT"]["Close"],
}).dropna(how="all")

print(close.tail())
