import plotly.graph_objects as go
import pandas as pd


# ---------------------------------------
# Price Chart
# ---------------------------------------
import plotly.graph_objects as go

def price_chart(df, stock_name):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Price",
            line=dict(width=2),
        )
    )

    fig.update_layout(
        title=f"{stock_name} Price Trend",
        height=420,
        margin=dict(l=10, r=10, t=40, b=10),
        xaxis_title="Date",
        yaxis_title="Price (₹)",
        hovermode="x unified",
    )

    return fig


# ---------------------------------------
# Volatility Chart
# ---------------------------------------
def volatility_chart(df: pd.DataFrame, stock_name: str):
    df = df.copy()
    df["Returns"] = df["Close"].pct_change()
    df["Volatility"] = df["Returns"].rolling(window=20).std() * 100

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Volatility"],
            mode="lines",
            name="Volatility",
            line=dict(width=2),
        )
    )

    fig.update_layout(
        title=f"{stock_name} Volatility (20D)",
        xaxis_title="Date",
        yaxis_title="Volatility %",
        height=420,
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False,
    )

    return fig