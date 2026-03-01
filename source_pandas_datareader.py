import pandas as pd
from pandas_datareader import data as pdr

def fetch_fred_datareader(series, start="2000-01-01", end="2026-02-26") -> pd.DataFrame:
    """
    Try pandas_datareader (fredgraph.csv). If blocked (Render), fall back to FRED API.
    """
    df = pdr.DataReader(series, "fred", start, end)
    return df


dgs10 = fetch_fred_datareader(["DGS3MO", "DGS2", "DGS10"]).ffill()
# dgs10 = fetch_fred_datareader("DGS3MO").ffill()
print(dgs10.tail(30))