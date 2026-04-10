from google_play_scraper import reviews
import pandas as pd

# Fetch reviews (example: Instagram app)
result, _ = reviews(
    'com.instagram.android',   # App ID
    lang='en',
    country='in',
    count=200
)

# Convert to DataFrame
df = pd.DataFrame(result)

# Select useful columns
df = df[['content', 'score', 'at']]

# Rename columns
df.rename(columns={
    'content': 'Review',
    'score': 'Rating',
    'at': 'Date'
}, inplace=True)

# Save to CSV
df.to_csv('data/playstore_reviews.csv', index=False)

print("✅ Data fetched and saved successfully!")