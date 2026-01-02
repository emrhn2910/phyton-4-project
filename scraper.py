import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from cleaning import to_number

def scrape_table(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, timeout=30)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    tables = soup.find_all("table")
    best_df = None
    best_score = -1

    for t in tables:
        try:
            df = pd.read_html(StringIO(str(t)))[0]
        except:
            continue

        if df.shape[0] < 10 or df.shape[1] < 2:
            continue

        numeric_like = sum(
            df[col].apply(to_number).notna().mean() >= 0.5
            for col in df.columns
        )

        score = df.shape[0] * df.shape[1] + numeric_like * 200
        if score > best_score:
            best_score = score
            best_df = df

    if best_df is None:
        raise RuntimeError("No suitable table found.")
    return best_df
