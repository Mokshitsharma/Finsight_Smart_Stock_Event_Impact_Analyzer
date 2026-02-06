import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (safe to call once)
nltk.download("vader_lexicon")


# ----------------------------------------
# Initialize Sentiment Analyzer
# ----------------------------------------
def get_sentiment_analyzer():
    """
    Initialize VADER sentiment analyzer
    """
    return SentimentIntensityAnalyzer()


# ----------------------------------------
# Analyze Event Sentiment
# ----------------------------------------
def analyze_event_sentiment(event_description: str):
    """
    Analyze sentiment of an event description
    """
    sia = get_sentiment_analyzer()
    scores = sia.polarity_scores(event_description)

    return {
        "positive": scores["pos"],
        "negative": scores["neg"],
        "neutral": scores["neu"],
        "compound": scores["compound"],
    }


# ----------------------------------------
# Add Sentiment to Events DataFrame
# ----------------------------------------
def add_sentiment_to_events(events_df: pd.DataFrame):
    """
    Add sentiment scores to market events
    """
    sentiments = events_df["description"].apply(analyze_event_sentiment)
    sentiment_df = pd.DataFrame(list(sentiments))

    return pd.concat([events_df.reset_index(drop=True), sentiment_df], axis=1)