import pandas as pd


# ----------------------------------------
# Generate Return Insights
# ----------------------------------------
def generate_return_insights(impact_df: pd.DataFrame):
    """
    Convert event impact metrics into readable insights
    """
    insights = []

    for _, row in impact_df.iterrows():
        direction = (
            "increased"
            if row["return_change"] > 0
            else "decreased"
        )

        insight = (
            f"📈 {row['ticker']} average returns "
            f"{direction} after the event by "
            f"{abs(row['return_change']):.2%}."
        )

        insights.append(insight)

    return insights


# ----------------------------------------
# Generate Volatility Insights
# ----------------------------------------
def generate_volatility_insights(vol_df: pd.DataFrame):
    """
    Generate volatility-based insights
    """
    insights = []

    for _, row in vol_df.iterrows():
        change_type = (
            "higher"
            if row["volatility_change"] > 0
            else "lower"
        )

        insight = (
            f"⚠️ {row['ticker']} volatility became "
            f"{change_type} after the event."
        )

        insights.append(insight)

    return insights


# ----------------------------------------
# Generate Sentiment Insight
# ----------------------------------------
def generate_sentiment_insight(sentiment_df: pd.DataFrame):
    """
    Summarize sentiment impact
    """
    avg_sentiment = sentiment_df["compound"].mean()

    if avg_sentiment > 0.05:
        return "🟢 Overall event sentiment was positive."
    elif avg_sentiment < -0.05:
        return "🔴 Overall event sentiment was negative."
    else:
        return "🟡 Overall event sentiment was neutral."