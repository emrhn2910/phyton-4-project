from sklearn.ensemble import IsolationForest

def compute_stats(x):
    return {
        "count": int(x.count()),
        "mean": x.mean(),
        "min": x.min(),
        "max": x.max(),
        "q1": x.quantile(0.25),
        "median": x.quantile(0.50),
        "q3": x.quantile(0.75),
        "iqr": x.quantile(0.75) - x.quantile(0.25)
    }

def add_anomaly_flags(df):
    x = df["value"]
    q1, q3 = x.quantile(0.25), x.quantile(0.75)
    iqr = q3 - q1

    df["anomaly_iqr"] = (x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)
    z = (x - x.mean()) / x.std()
    df["anomaly_z"] = z.abs() >= 3

    iso = IsolationForest(random_state=42)
    df["anomaly_iso"] = iso.fit_predict(df[["value"]]) == -1
    df["anomaly_final"] = (
        df[["anomaly_iqr", "anomaly_z", "anomaly_iso"]].sum(axis=1) >= 2
    )
    return df
