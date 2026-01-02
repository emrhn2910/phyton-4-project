import matplotlib.pyplot as plt
import seaborn as sns

def show_plots(df, top_n=15):
    sns.set_theme()

    plt.hist(df["value"], bins=30)
    plt.title("Distribution")
    plt.show()

    sns.boxplot(x=df["value"])
    plt.title("Box Plot")
    plt.show()

    sns.histplot(df["value"], kde=True)
    plt.title("Histogram + KDE")
    plt.show()

    top = df.head(top_n).iloc[::-1]
    sns.barplot(data=top, x="value", y="label")
    plt.title(f"Top {top_n}")
    plt.show()

    tmp = df.reset_index()
    sns.scatterplot(data=tmp, x="index", y="value", hue="anomaly_final")
    plt.title("Anomaly Detection")
    plt.show()
