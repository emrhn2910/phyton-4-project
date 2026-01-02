import re
import numpy as np
import pandas as pd

def remove_footnotes(x):
    return re.sub(r"\[[^\]]*\]", "", str(x)).strip()

def to_number(x):
    if pd.isna(x):
        return np.nan
    s = remove_footnotes(x)
    s = s.replace(",", "").replace("%", "").strip()
    s = re.sub(r"[^0-9.\-]", "", s)
    try:
        return float(s)
    except:
        return np.nan

def pick_best_numeric_column(df):
    best_col, best_ratio = None, -1
    for col in df.columns:
        ratio = df[col].apply(to_number).notna().mean()
        if ratio > best_ratio:
            best_ratio = ratio
            best_col = col
    return best_col

def build_clean_frame(df_raw):
    df = df_raw.copy()
    for c in df.columns:
        df[c] = df[c].apply(remove_footnotes)

    num_col = pick_best_numeric_column(df)
    df["value"] = df[num_col].apply(to_number)
    df["label"] = df[df.columns[0]].astype(str).str.strip()

    df = df.dropna(subset=["value"])
    df = df[df["label"] != ""]
    df = df[["label", "value"]].drop_duplicates().reset_index(drop=True)
    return df.sort_values("value", ascending=False).reset_index(drop=True)
