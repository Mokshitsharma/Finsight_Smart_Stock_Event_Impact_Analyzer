import pandas as pd
import numpy as np


# ----------------------------------------
# Rolling Volatility
# ----------------------------------------
def calculate_rolling_volatility(
    price_df: pd.DataFrame,
    window: int = 5
):
    """
    Calculate rolling volatility using daily returns
    """
    df = price_df.copy()
    df["returns"] = df["close"].pct_change()
    df["rolling_volatility"] = (
        df["returns"]
        .rolling(window=window)
        .std()
    )
    return df


# ----------------------------------------
# Event-based Volatility Comparison
# ----------------------------------------
def event_volatility_analysis(
    price_df: pd.DataFrame,
    event_date: pd.Timestamp,
    window: int = 5
):
    """
    Compare volatility before and after an event
    """
    df = calculate_rolling_volatility(price_df, window)
    df["date"] = pd.to_datetime(df["date"])

    pre_event = df[
        (df["date"] < event_date)
        & (df["date"] >= event_date - pd.Timedelta(days=window))
    ]

    post_event = df[
        (df["date"] > event_date)
        & (df["date"] <= event_date + pd.Timedelta(days=window))
    ]

    if pre_event.empty or post_event.empty:
        return None

    return {
        "pre_event_volatility": pre_event["rolling_volatility"].mean(),
        "post_event_volatility": post_event["rolling_volatility"].mean(),
        "volatility_change": (
            post_event["rolling_volatility"].mean()
            - pre_event["rolling_volatility"].mean()
        ),
    }


# ----------------------------------------
# Multi-Stock Volatility Analysis
# ----------------------------------------
def analyze_volatility_for_stocks(
    stock_data: dict,
    event_date: pd.Timestamp,
    window: int = 5
):
    """
    Run volatility analysis for multiple stocks
    """
    results = []

    for ticker, df in stock_data.items():
        impact = event_volatility_analysis(df, event_date, window)

        if impact:
            impact["ticker"] = ticker
            results.append(impact)

    return pd.DataFrame(results)