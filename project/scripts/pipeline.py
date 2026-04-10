import os

print("🚀 Starting Data Pipeline...")

# Step 1: Fetch Data
print("📥 Fetching data...")
os.system("python scripts/google-play.py")

# Step 2: Sentiment Analysis
print("🧠 Running sentiment analysis...")
os.system("python scripts/sentiment.py")

# Step 3: Feature Engineering
print("⚙️ Applying feature engineering...")
os.system("python scripts/feature_engineering.py")

print("✅ Pipeline completed successfully!")