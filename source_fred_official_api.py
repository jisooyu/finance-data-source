import os
import pandas as pd
import requests
from pathlib import Path
from dotenv import load_dotenv

# 다른 디렉토리에서 실행할 경우를 대비. 이렇게 하면 .env를 찾는 데 문제가 없음
env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)
FRED_API_KEY = os.getenv("FRED_API_KEY")

def fred_api_series(series_id: str, start="2000-01-01") -> pd.Series:
    url = "https://api.stlouisfed.org/fred/series/observations"
    r = requests.get(
        url,
        params={
            "series_id": series_id,
            "api_key": FRED_API_KEY,
            "file_type": "json",
            "observation_start": start,
        },
        timeout=20,
    )
    r.raise_for_status()
    obs = r.json()["observations"]
    s = pd.Series(
        [x["value"] for x in obs],
        index=pd.to_datetime([x["date"] for x in obs]),
        name=series_id,
    )
    s = pd.to_numeric(s, errors="coerce")  # "." -> NaN, etc.
    return s

dgs10 = fred_api_series("DGS10")
print(dgs10.tail())
