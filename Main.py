from ingestion import load_and_clean_data
from Visualize import plot_category_spending, plot_monthly_trend
from Analysis import detect_anomalies, cluster_spending
from recommendation import generate_recommendation
from gemini_analysis import gemini_insights
import os
from dotenv import load_dotenv

# Load environment variables from .env if present
try:
    load_dotenv()
    api_key = os.getenv('api_key')
except Exception:
    api_key = None

# Load data
df = load_and_clean_data("data/messy_transactions_1200.csv")

# Analyze
df = detect_anomalies(df)
clustered = cluster_spending(df)

# Visualize
plot_category_spending(df)
plot_monthly_trend(df)

# Recommendations
insights = generate_recommendation(df)
print("\n===== Your Recommendations =====")
for tip in insights:
    print(tip)

# Gemini AI Insights (side by side)
if api_key:
    print("\n===== Gemini AI Suggestions =====")
    try:
        print(gemini_insights(df, api_key))
    except Exception as e:
        print(f"[Gemini Error] {e}")
else:
    print("\n[Gemini] No API key found. Skipping Gemini AI insights.")
