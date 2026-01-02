import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from baseline import analyze_clean_downloaded_data
from scraper import scrape_table
from cleaning import build_clean_frame
from analysis import compute_stats, add_anomaly_flags
from visualization import show_plots

def main():
    analyze_clean_downloaded_data()

    url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    raw = scrape_table(url)

    clean = build_clean_frame(raw)
    stats = compute_stats(clean["value"])

    print("\nSummary Statistics:")
    for k, v in stats.items():
        print(f"{k}: {v}")

    analyzed = add_anomaly_flags(clean)
    show_plots(analyzed)

if __name__ == "__main__":
    main()
