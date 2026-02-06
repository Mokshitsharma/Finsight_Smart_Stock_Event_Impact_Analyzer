import yfinance as yf
import pandas as pd
from functools import lru_cache


# ---------------------------------------------
# Fetch fundamentals with caching
# ---------------------------------------------
@lru_cache(maxsize=32)
def fetch_fundamentals(ticker: str) -> dict:
    stock = yf.Ticker(ticker)
    info = stock.info

    fundamentals = {
        "PE": info.get("trailingPE"),
        "EPS": info.get("trailingEps"),
        "ROE": info.get("returnOnEquity"),
        "MarketCap": info.get("marketCap"),
        "DebtToEquity": info.get("debtToEquity"),
    }

    return fundamentals


# ---------------------------------------------
# Clean & format numbers
# ---------------------------------------------
def format_fundamentals(fundamentals: dict) -> dict:
    return {
        "PE": round(fundamentals["PE"], 2) if fundamentals["PE"] else "—",
        "EPS": round(fundamentals["EPS"], 2) if fundamentals["EPS"] else "—",
        "ROE (%)": round(fundamentals["ROE"] * 100, 2)
        if fundamentals["ROE"]
        else "—",
    }


# ---------------------------------------------
# Buy / Hold / Caution Logic
# ---------------------------------------------
def investment_signal(fundamentals: dict) -> str:
    pe = fundamentals.get("PE")
    roe = fundamentals.get("ROE")
    eps = fundamentals.get("EPS")

    if pe and roe and eps:
        if pe < 25 and roe > 0.15 and eps > 0:
            return "🟢 Buy"
        elif pe < 40 and roe > 0.10:
            return "🟡 Hold"
        else:
            return "🔴 Caution"

    return "⚪ Insufficient Data"


# ---------------------------------------------
# Bundle for UI
# ---------------------------------------------
def get_fundamentals_block(ticker: str) -> dict:
    raw = fetch_fundamentals(ticker)
    formatted = format_fundamentals(raw)
    signal = investment_signal(raw)

    return {
        "metrics": formatted,
        "signal": signal,
    }