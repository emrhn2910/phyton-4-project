import pandas as pd

def analyze_clean_downloaded_data():
    data = {
        "country": ["USA", "China", "Germany", "Japan", "India"],
        "gdp": [31821293, 20650754, 5328184, 4463634, 4226738]
    }
    df = pd.DataFrame(data)

    print("\n[BASELINE] Clean downloaded dataset analysis")
    print(df.to_string(index=False))
    print("Mean GDP:", df["gdp"].mean())
    print("Min GDP:", df["gdp"].min())
    print("Max GDP:", df["gdp"].max())
