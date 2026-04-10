import pandas as pd
from textblob import TextBlob

# Load data
df = pd.read_csv('data/playstore_reviews.csv')

# Function to get sentiment
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df['Sentiment'] = df['Review'].apply(get_sentiment)

# Save updated data
df.to_csv('data/playstore_reviews_with_sentiment.csv', index=False)

print("✅ Sentiment analysis completed!")