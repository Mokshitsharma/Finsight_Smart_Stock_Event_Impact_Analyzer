# 📈 Smart Stock Event Impact Analyzer
### 🚀 Overview

**The Smart Stock Event Impact Analyzer is a data-driven financial analytics application that quantifies how major market events (such as RBI policy decisions, Union Budget announcements, IPO approvals, and earnings) impact stock prices, volatility, and investor sentiment in the Indian equity market.**

The project follows an event-study approach, commonly used in quantitative finance, and presents insights through an interactive Streamlit dashboard.

### 🎯 Problem Statement

-> Stock prices often react sharply to macroeconomic and corporate events, but:

-> How significant is the reaction?

-> Is the impact short-term or persistent?

-> Does positive news sentiment always translate into positive returns?

-> Which events increase market risk (volatility) the most?

-> This project aims to systematically measure and visualize these effects.

### 🧠 Key Features

-> 📊 Event-based stock price analysis

-> 📈 Event-day return & pre/post event comparison

-> ⚡ Volatility spike detection

-> 🧠 News sentiment analysis (NLP)

-> 📝 Auto-generated, decision-oriented insights

-> 🎛️ Interactive Streamlit dashboard

### 📌 Scope (Version 1)

-> Market Focus: NIFTY-5 large-cap stocks

-> Reliance Industries

-> TCS

-> HDFC Bank

-> Infosys

-> ICICI Bank

-> Benchmark Index: NIFTY 50

### Event Types:

-> RBI Monetary Policy

-> Union Budget

-> IPO Approval

-> Quarterly Earnings

### 🏗️ Project Architecture
Smart-Stock-Event-Impact-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── events/
│   │   └── market_events.csv
│   └── cache/
│       └── prices_cache.csv
│
├── src/
│   ├── data_loader.py
│   ├── event_analysis.py
│   ├── volatility_analysis.py
│   ├── sentiment_analysis.py
│   ├── charts.py
│   └── insights.py
│
└── assets/
    └── screenshots/

### 🔄 Data Flow

User Input (Stock + Event)
        ↓
Market Data (yfinance)
        ↓
Event Window Extraction
        ↓
Returns & Volatility Analysis
        ↓
Sentiment Scoring (NLP)
        ↓
Visualization + Insights

### 🛠️ Tech Stack

-> **Programming Language**: Python

-> **Web Framework**: Streamlit

-> **Data Analysis**: Pandas, NumPy

-> **Market Data**: yfinance

-> **Visualization**: Matplotlib, Seaborn

-> **Statistics**: SciPy

-> **NLP (Sentiment)**: NLTK (VADER)

### ▶️ How to Run Locally
1️⃣ Clone the repository

git clone https://github.com/your-username/Smart-Stock-Event-Impact-Analyzer.git

cd Smart-Stock-Event-Impact-Analyzer

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py

### 🧪 Sample Insights Generated

“Positive market reaction despite negative news sentiment.”

“Significant volatility spike observed post event.”

“Negative immediate market reaction on event day.”

These insights help bridge the gap between raw analytics and decision-making.

### 📈 Future Enhancements (Planned)

Cumulative Abnormal Return (CAR) vs benchmark

Real-time news API integration

Sector-wise event impact analysis

Comparative analysis across multiple events

Deployment on Streamlit Cloud

### 👤 Author

Mokshit Sharma
B.Tech + M.Tech (Dual Degree) – AI & Data Science
📍 DAVV, Indore

### 🔗 GitHub: https://github.com/Mokshitsharma

### 🔗 LinkedIn: https://linkedin.com/in/mokshit-sharma-75b5ab305

### ⚠️ Disclaimer

This project is for educational and analytical purposes only.
It does not constitute financial or investment advice.

### ⭐ If you like this project, give it a ⭐ on GitHub — it helps a lot!
