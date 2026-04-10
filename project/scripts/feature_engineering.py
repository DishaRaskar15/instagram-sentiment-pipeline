import pandas as pd

df = pd.read_csv('data/playstore_reviews_with_sentiment.csv')

def rating_category(r):
    if r >= 4:
        return "Good"
    elif r == 3:
        return "Average"
    else:
        return "Bad"

df['Rating Category'] = df['Rating'].apply(rating_category)


df['Review Length'] = df['Review'].apply(lambda x: len(str(x)))

df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.date

from textblob import TextBlob

df['Sentiment Score'] = df['Review'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

df.to_csv('data/final_reviews.csv', index=False)

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('data/reviews.db')

# Save data to database
df.to_sql('reviews', conn, if_exists='replace', index=False)

# Close connection
conn.close()

print("✅ Data saved to SQLite database!")
print("✅ Feature engineering completed!")
