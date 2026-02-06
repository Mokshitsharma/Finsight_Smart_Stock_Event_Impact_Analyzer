import plotly.graph_objects as go
import pandas as pd

DARK_THEME = "plotly_dark"


# -------------------------------------------------
# Price Trend Chart
# -------------------------------------------------
def plot_price_trend(price_df: pd.DataFrame, ticker: str):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=price_df["date"],
            y=price_df["close"],
            mode="lines",
            name=ticker,
            line=dict(width=2),
        )
    )

    fig.update_layout(
        title=f"{ticker} Price Trend",
        template=DARK_THEME,
        height=280,
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis_title="Date",
        yaxis_title="Price",
        showlegend=False,
    )

    return fig


# -------------------------------------------------
# Pre vs Post Returns
# -------------------------------------------------
def plot_pre_post_returns(impact_df: pd.DataFrame):
    fig = go.Figure()

    fig.add_bar(
        x=impact_df["ticker"],
        y=impact_df["pre_event_avg_return"],
        name="Pre-Event",
    )

    fig.add_bar(
        x=impact_df["ticker"],
        y=impact_df["post_event_avg_return"],
        name="Post-Event",
    )

    fig.update_layout(
        title="Pre vs Post Event Returns",
        template=DARK_THEME,
        barmode="group",
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        yaxis_title="Average Return",
    )

    return fig


# -------------------------------------------------
# Volatility Change
# -------------------------------------------------
def plot_volatility_change(vol_df: pd.DataFrame):
    fig = go.Figure()

    fig.add_bar(
        x=vol_df["ticker"],
        y=vol_df["volatility_change"],
        marker_color="orange",
    )

    fig.update_layout(
        title="Volatility Change After Event",
        template=DARK_THEME,
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        yaxis_title="Volatility Change",
    )

    return fig


# -------------------------------------------------
# Event Sentiment
# -------------------------------------------------
def plot_event_sentiment(sentiment_df: pd.DataFrame):
    values = [
        sentiment_df["positive"].mean(),
        sentiment_df["negative"].mean(),
        sentiment_df["neutral"].mean(),
    ]

    fig = go.Figure(
        data=[
            go.Bar(
                x=["Positive", "Negative", "Neutral"],
                y=values,
            )
        ]
    )

    fig.update_layout(
        title="Event Sentiment",
        template=DARK_THEME,
        height=260,
        margin=dict(l=20, r=20, t=40, b=20),
        yaxis_title="Score",
    )

    return fig