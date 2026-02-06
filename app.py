import streamlit as st
import plotly.io as pio

from src.data_loader import get_stock_prices
from src.charts import price_chart, volatility_chart
from src.fundamentals import get_fundamentals_block
from src.event_analysis import load_market_events, get_relevant_events

# ---------------------------------------
# App Config
# ---------------------------------------
st.set_page_config(
    page_title="Smart Stock Event Impact Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

pio.templates.default = "plotly_dark"

# ---------------------------------------
# Dark Premium CSS
# ---------------------------------------
st.markdown(
    """
    <style>
    body { background-color: #0e1117; }

    .metric-card {
        background-color: #161b22;
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
    }

    .signal-buy { color: #00c853; font-weight: 700; }
    .signal-hold { color: #ffab00; font-weight: 700; }
    .signal-caution { color: #ff5252; font-weight: 700; }

    .event-card {
        background-color:#161b22;
        padding:14px;
        border-radius:12px;
        margin-bottom:12px;
        box-shadow:0 0 0 1px rgba(255,255,255,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------
# Header
# ---------------------------------------
st.markdown("# Smart Stock Event Impact Analyzer")
st.caption("### Where market events meet investor intelligence.")

# ---------------------------------------
# Stock Selector
# ---------------------------------------
stocks = {
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "Infosys": "INFY.NS",
}

selected_stock = st.radio(
    "",
    options=list(stocks.keys()),
    horizontal=True,
)

ticker = stocks[selected_stock]

# ---------------------------------------
# Fundamentals Section
# ---------------------------------------
fundamentals = get_fundamentals_block(ticker)

c1, c2, c3, c4 = st.columns([1, 1, 1, 1.2])

with c1:
    st.markdown(
        f"<div class='metric-card'><h4>PE</h4><h2>{fundamentals['metrics']['PE']}</h2></div>",
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"<div class='metric-card'><h4>EPS</h4><h2>{fundamentals['metrics']['EPS']}</h2></div>",
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"<div class='metric-card'><h4>ROE</h4><h2>{fundamentals['metrics']['ROE (%)']}%</h2></div>",
        unsafe_allow_html=True,
    )

with c4:
    signal = fundamentals["signal"]
    css_class = (
        "signal-buy" if "Buy" in signal else
        "signal-hold" if "Hold" in signal else
        "signal-caution"
    )

    st.markdown(
        f"""
        <div class='metric-card'>
            <h4>Signal</h4>
            <h2 class='{css_class}'>{signal}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# ---------------------------------------
# Charts Section
# ---------------------------------------
price_data = get_stock_prices(ticker)

ch1, ch2 = st.columns(2)

with ch1:
    st.plotly_chart(
        price_chart(price_data, selected_stock),
        use_container_width=True,
        config={"displayModeBar": False},
    )

with ch2:
    st.plotly_chart(
        volatility_chart(price_data, selected_stock),
        use_container_width=True,
        config={"displayModeBar": False},
    )

# ---------------------------------------
# Market Events Section
# ---------------------------------------
st.divider()
st.markdown("### 🗓️ Key Market Events & Impact")

events_df = load_market_events()
display_events = get_relevant_events(events_df, price_data)

if display_events.empty:
    st.caption("No major market events available.")
else:
    for _, row in display_events.iterrows():

        impact_badge = (
            "🟥 High" if row["impact"] == "High"
            else "🟨 Medium" if row["impact"] == "Medium"
            else "🟩 Low"
        )

        sentiment_badge = {
            "Bullish": "🟢 Bullish",
            "Bearish": "🔴 Bearish",
            "Neutral": "⚪ Neutral",
        }.get(row["sentiment"], "⚪ Neutral")

        st.markdown(
            f"""
            <div class="event-card">
                <strong>{row['event']}</strong><br>
                <small>
                    {row['date'].date()} • {impact_badge} • {row['event_type']}
                </small><br>
                <small><b>Sentiment:</b> {sentiment_badge}</small>
                <p style="margin-top:6px; font-size:13px; color:#c9d1d9;">
                    {row['description']}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
