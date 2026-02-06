import pandas as pd

def load_market_events():
    df = pd.read_csv("data/events/market_events.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


def classify_event_sentiment(row):
    event = row["event"].lower()
    etype = row["event_type"].lower()
    impact = row["impact"]

    if "war" in event or "crisis" in event:
        return "Bearish"

    if etype == "economic":
        return "Bearish" if impact == "High" else "Bullish"

    if etype == "political":
        return "Bearish" if impact == "High" else "Neutral"

    if etype == "monetary":
        return "Bullish" if "pause" in event or "cut" in event else "Bearish"

    if "budget" in event:
        return "Bullish"

    return "Neutral"


def get_relevant_events(events_df, price_df):
    events_df = events_df.copy()

    # --- SAFETY: ensure datetime index ---
    if not isinstance(price_df.index, pd.DatetimeIndex):
        price_df.index = pd.to_datetime(price_df.index)

    events_df["sentiment"] = events_df.apply(classify_event_sentiment, axis=1)
    events_df["impact_type"] = events_df["event_type"]
    events_df["notes"] = events_df["description"]

    start_date = price_df.index.min()
    end_date = price_df.index.max()

    linked_events = events_df[
        (events_df["date"] >= start_date) &
        (events_df["date"] <= end_date)
    ]

    # fallback: show all if none linked
    return linked_events if not linked_events.empty else events_df
