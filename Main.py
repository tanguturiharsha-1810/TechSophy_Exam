from ingestion import load_and_clean_data
from Visualize import plot_category_spending, plot_monthly_trend
from Analysis import detect_anomalies, cluster_spending
from recommendation import generate_recommendation

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
for tip in insights:
    print(tip)
