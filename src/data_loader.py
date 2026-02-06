import os
import pandas as pd
import yfinance as yf
from datetime import datetime

# Paths
EVENTS_PATH = "data/events/market_events.csv"
CACHE_PATH = "data/cache/prices_cache.csv"


# -------------------------------
# Load Market Events
# -------------------------------
def load_market_events():
    """
    Load market events from CSV
    """
    if not os.path.exists(EVENTS_PATH):
        raise FileNotFoundError("market_events.csv not found")

    events_df = pd.read_csv(EVENTS_PATH, parse_dates=["event_date"])
    events_df.sort_values("event_date", inplace=True)
    return events_df


# -------------------------------
# Load Cached Prices
# -------------------------------
def load_price_cache():
    """
    Load cached stock price data
    """
    if not os.path.exists(CACHE_PATH):
        # Create empty cache if not exists
        df = pd.DataFrame(
            columns=["date", "ticker", "open", "high", "low", "close", "volume"]
        )
        df.to_csv(CACHE_PATH, index=False)

    cache_df = pd.read_csv(CACHE_PATH, parse_dates=["date"])
    return cache_df


# -------------------------------
# Save to Cache
# -------------------------------
def save_to_cache(new_data):
    """
    Append new stock data to cache
    """
    cache_df = load_price_cache()
    combined_df = pd.concat([cache_df, new_data])
    combined_df.drop_duplicates(subset=["date", "ticker"], inplace=True)
    combined_df.to_csv(CACHE_PATH, index=False)


# -------------------------------
# Fetch Stock Price Data
# -------------------------------
def fetch_stock_data(
    ticker: str,
    start_date: str,
    end_date: str
):
    """
    Fetch stock data using cache + yfinance fallback
    """
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    cache_df = load_price_cache()

    # Check cache
    cached_data = cache_df[
        (cache_df["ticker"] == ticker)
        & (cache_df["date"] >= start_date)
        & (cache_df["date"] <= end_date)
    ]

    expected_days = pd.date_range(start_date, end_date, freq="B")

    # If cache is incomplete → fetch from yfinance
    if len(cached_data) < len(expected_days):
        yf_data = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            progress=False
        )

        if yf_data.empty:
            return pd.DataFrame()

        yf_data.reset_index(inplace=True)
        yf_data.rename(
            columns={
                "Date": "date",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            },
            inplace=True,
        )

        yf_data["ticker"] = ticker
        yf_data = yf_data[
            ["date", "ticker", "open", "high", "low", "close", "volume"]
        ]

        save_to_cache(yf_data)
        return yf_data

    return cached_data.sort_values("date")


# -------------------------------
# Default Stock Universe
# -------------------------------
def get_default_stocks():
    """
    Initial stock universe (Top 5 Indian stocks)
    """
    return [
        "RELIANCE.NS",
        "TCS.NS",
        "INFY.NS",
        "HDFCBANK.NS",
        "ICICIBANK.NS",
    ]
import yfinance as yf
import pandas as pd
from functools import lru_cache


@lru_cache(maxsize=32)
def get_stock_prices(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Fetch historical stock prices
    """
    df = yf.download(
        ticker,
        period=period,
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    df.reset_index(inplace=True)
    return df
