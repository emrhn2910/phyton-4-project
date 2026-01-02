# GDP Data Analysis & Anomaly Detection System

A modern Python data analysis application that **scrapes real-world GDP data**, cleans messy datasets, performs **advanced statistical analysis**, detects **anomalies using data science methods**, and visualizes results with Matplotlib and Seaborn.

---

## 🚀 Features

### ✅ Dataset (Baseline + Real-World)

- Includes a **clean downloaded baseline dataset** for initial analysis  
- Scrapes **messy real-world GDP data** from Wikipedia  
- Converts unstructured and noisy values into clean numerical data  

### ✅ Web Scraping

- HTTP requests using **Requests**
- HTML parsing with **BeautifulSoup**
- Automatically scans all tables on the webpage
- Selects the most relevant GDP table dynamically
- Handles messy HTML content and footnotes

### ✅ Data Cleaning & Preprocessing

- Removes footnote references like `[1]`, `[n 2]`
- Converts strings with commas and symbols into numeric values
- Drops missing and invalid GDP entries
- Produces a clean dataset with:
  - `label` → country / territory
  - `value` → GDP value

### ✅ Advanced Statistical Analysis

- Basic statistics:
  - count, mean, min, max, standard deviation
- Advanced statistics:
  - quartiles (Q1, median, Q3)
  - interquartile range (IQR)

### ✅ Data Science: Anomaly Detection

Uses **three independent anomaly detection methods**:

- **IQR Rule**
- **Z-Score Analysis**
- **Isolation Forest (Machine Learning)**

A country is marked as an anomaly if **at least two methods agree**.

### ✅ Visualization

- **Matplotlib**
  - Histogram of GDP distribution
- **Seaborn**
  - Box & whisker plot
  - Histogram with KDE
  - Top-N GDP bar chart
  - Scatter plot highlighting anomalies

---

## 🏗️ Project Architecture Overviewproject/

├── project4.py        # Main Python script
       
└── README.md          # Project documentation

All scraping, cleaning, analysis, anomaly detection, and visualization steps are handled inside a single Python file.

---

## 📊 Anomaly Detection Logic

| Method            | Purpose                          |
|------------------|----------------------------------|
| IQR              | Quartile-based outlier detection |
| Z-Score          | Distance from mean               |
| Isolation Forest | ML-based anomaly detection       |

Final rule:
     
     Anomaly = True if (IQR + Z-Score + IsolationForest) ≥ 2


---

## 📦 Installation

pip install pandas numpy matplotlib seaborn requests beautifulsoup4 scikit-learn lxml


## ▶️ Run the Project

python project4.py


## 🌐 Analysis Workflow

•The program follows this workflow:

•Analyze a clean, downloaded baseline dataset

•Display baseline summary statistics

•Scrape GDP data from the web

•Parse and evaluate all HTML tables

•Automatically select the most relevant GDP table

•Clean and normalize messy or inconsistent values

•Compute statistical summaries

•Detect anomalies using multiple methods

•Visualize the results interactively


## 🖥️ Output

The program does not save any files by default

It displays the following outputs on the screen:

•Raw scraped data preview

•Cleaned dataset preview

•Summary statistics

•Number of detected anomalies

•Interactive plots and charts


## 🛠️ Technologies Used

  •Python 3.10+

  •Pandas

  •NumPy

  •Requests

  •BeautifulSoup (bs4)

  •lxml

  •Matplotlib

  •Seaborn

  •Scikit-learn (Isolation Forest)

  






