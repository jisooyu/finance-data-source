import os
import pandas as pd
from fredapi import Fred
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

dgs10 = fred.get_series("DGS10", observation_start="2000-01-01")
dgs10 = pd.Series(dgs10, name="DGS10")
dgs10.index = pd.to_datetime(dgs10.index)

print(dgs10.tail())
