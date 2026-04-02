# 📈 FinSight — Smart Stock Event Impact Analyzer

> **A dark, minimal fintech-style dashboard that connects market events with stock behavior — designed from an investor-first perspective.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?style=flat-square&logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Dark-636efa?style=flat-square&logo=plotly)
![NLTK](https://img.shields.io/badge/NLTK-VADER-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

---

## 📌 Problem Statement

Stock prices react sharply to macroeconomic and corporate events — but most retail investors have no systematic way to measure these reactions. Key unanswered questions include:

- How significant is the price reaction to a specific event (RBI rate cut, Budget, Earnings)?
- Is the impact short-term or does it persist over days?
- Does positive news sentiment always translate into positive returns?
- Which event types cause the highest volatility spikes?
- How do fundamentals (PE, EPS, ROE) relate to event-driven movements?

Without a structured framework, investors rely on noise and opinions instead of data. FinSight solves this.

---

## 💡 My Solution

FinSight applies the **event-study methodology** — a standard quantitative finance technique used by institutional analysts — to Indian equity markets, packaged as an interactive Streamlit dashboard.

For each of 4 major Nifty large-cap stocks, the system:
- Fetches live OHLCV price data via yfinance
- Loads a curated market events dataset (RBI, Budget, IPO, Earnings)
- Computes event-day returns and volatility spikes around each event window
- Scores news sentiment using NLTK VADER
- Generates a fundamental signal (BUY / HOLD / CAUTION) based on PE, EPS, ROE
- Renders all insights in a premium dark Plotly dashboard with event cards

The result is a clear, data-driven view of how each major market event impacted each stock — with sentiment, impact severity, and price behavior all in one place.

---

## 📊 Metrics

| Metric | Description |
|---|---|
| **Event-Day Return (%)** | Percentage price change on the event date vs prior close |
| **Pre-Event Window Return** | Average return in the 5 trading days before the event |
| **Post-Event Window Return** | Average return in the 5 trading days after the event |
| **Volatility Spike** | Rolling standard deviation of returns around event window |
| **Sentiment Score** | VADER compound score (−1 to +1) on event description text |
| **Impact Classification** | High / Medium / Low based on price move magnitude |
| **Fundamental Signal** | BUY / HOLD / CAUTION derived from PE, EPS, ROE thresholds |

---

## 🛠️ Skills & Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Web UI | Streamlit (dark theme, custom CSS) |
| Visualization | Plotly (dark theme), Matplotlib, Seaborn |
| Market Data | yfinance (live OHLCV + fundamentals) |
| NLP / Sentiment | NLTK VADER (event description sentiment scoring) |
| Statistics | SciPy (return analysis, volatility computation) |
| Data Processing | Pandas, NumPy |
| Event Data | Custom CSV (`market_events.csv`) with curated event metadata |
| Caching | Local CSV cache (`prices_cache.csv`) for faster reruns |

---

## 📂 Dataset Details

### Market Price Data
| Field | Details |
|---|---|
| Source | Yahoo Finance via yfinance |
| Stocks | Reliance (RELIANCE.NS), TCS (TCS.NS), HDFC Bank (HDFCBANK.NS), Infosys (INFY.NS) |
| Benchmark | NIFTY 50 Index |
| Frequency | Daily OHLCV |

### Market Events Dataset (`data/events/market_events.csv`)
| Field | Details |
|---|---|
| Event Types | RBI Monetary Policy, Union Budget, IPO Approval, Quarterly Earnings |
| Fields | event, date, event_type, impact (High/Medium/Low), sentiment (Bullish/Bearish/Neutral), description |
| Scope | Curated manually for accuracy and relevance |

### Fundamentals (Live via yfinance)
| Metric | Description |
|---|---|
| PE Ratio | Price-to-Earnings |
| EPS | Earnings Per Share |
| ROE (%) | Return on Equity |

---

## 🗂️ Folder Structure

```
Finsight_Smart_Stock_Event_Impact_Analyzer/
├── app.py                        # Main Streamlit app (183 lines)
├── requirements.txt              # Python dependencies
├── README.md
│
├── data/
│   ├── events/
│   │   └── market_events.csv     # Curated market event dataset
│   └── cache/
│       └── prices_cache.csv      # Local price data cache
│
└── src/
    ├── data_loader.py            # yfinance price fetcher + cache handler
    ├── event_analysis.py         # Event window extraction + matching logic
    ├── volatility_analysis.py    # Rolling volatility + spike detection
    ├── sentiment_analysis.py     # NLTK VADER sentiment scorer
    ├── charts.py                 # Plotly price chart + volatility chart builders
    ├── fundamentals.py           # PE/EPS/ROE fetcher + BUY/HOLD/CAUTION signal
    └── insights.py               # Auto-generated insight text per event
```

---

## ⚙️ System Architecture

```
Step 1 → User selects a stock (Reliance / TCS / HDFC Bank / Infosys) via Streamlit radio
Step 2 → data_loader.py fetches live OHLCV from Yahoo Finance (cached locally as CSV)
Step 3 → fundamentals.py pulls PE, EPS, ROE → computes BUY / HOLD / CAUTION signal
Step 4 → charts.py renders Plotly dark-theme price chart + rolling volatility chart
Step 5 → event_analysis.py loads market_events.csv → filters events relevant to selected stock
Step 6 → For each event: computes event-day return, pre/post window returns, volatility spike
Step 7 → sentiment_analysis.py runs NLTK VADER on event description → Bullish/Bearish/Neutral
Step 8 → insights.py generates auto-text: "Positive market reaction despite negative sentiment"
Step 9 → Streamlit renders event cards: event name, date, impact badge, sentiment badge, description
Step 10 → User reads full picture: fundamentals + price trend + volatility + event history
```

---

## 🔍 Why This Tech Stack?

| Choice | Reason |
|---|---|
| **Streamlit** | Rapid prototyping of data apps without frontend code; perfect for fintech dashboards |
| **Plotly (dark theme)** | Interactive, visually premium charts — far superior to Matplotlib for investor-facing UIs |
| **NLTK VADER** | Rule-based sentiment scorer that works well on short financial text without model training |
| **yfinance** | Free, reliable access to NSE/BSE stock data and fundamentals |
| **SciPy** | Statistical functions for return distribution analysis and volatility metrics |
| **Custom CSV events** | Full control over event quality and relevance — avoids noisy API-based event data |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
git clone https://github.com/Mokshitsharma/Finsight_Smart_Stock_Event_Impact_Analyzer.git
cd Finsight_Smart_Stock_Event_Impact_Analyzer
pip install -r requirements.txt
```

### Run
```bash
streamlit run app.py
```

Open browser at **http://localhost:8501**

### Usage
1. Select a stock from the top radio selector
2. View live fundamentals (PE, EPS, ROE, Signal) in metric cards
3. Analyze price trend and rolling volatility in the dual Plotly charts
4. Scroll down to read event cards — each showing date, impact, sentiment, and description

---

## 🔮 Future Improvements

1. **Cumulative Abnormal Return (CAR)** — compare stock return vs NIFTY 50 benchmark return around each event window to isolate true event-driven alpha
2. **Real-time news API** — replace manual CSV events with live NewsAPI / Google News RSS for auto event detection
3. **Expand stock universe** — cover all 50 Nifty stocks with sector-wise event impact grouping
4. **Multi-event comparison** — overlay multiple events on a single chart to compare impact magnitudes side-by-side
5. **Streamlit Cloud deployment** — make the dashboard publicly accessible with a shareable URL
6. **Statistical significance testing** — t-tests on event-window returns to confirm significance vs random noise

---

## ⚠️ Disclaimer

FinSight is built for **educational and analytical purposes only**. It does not constitute financial or investment advice. Always consult a SEBI-registered financial advisor before making investment decisions.

---

## 👤 Author

**Mokshit Sharma**
B.Tech + M.Tech (Dual Degree) — AI & Data Science | DAVV, Indore
📧 sharman48520@gmail.com | 🌐 [mokshitsharma27.vercel.app](https://mokshitsharma27.vercel.app)
🔗 [LinkedIn](https://linkedin.com/in/mokshit-sharma-75b5ab305) | 💻 [GitHub](https://github.com/Mokshitsharma)

---

⭐ Star this repo if you find it useful!
