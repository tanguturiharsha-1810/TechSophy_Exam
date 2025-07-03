def generate_recommendation(df):
    insights = []

    #Monthly overspend alert
    monthly_avg = df.groupby('Month')['Amount'].sum().Mean()
    latest_month = df['Month'].max()
    latest_spend = df[df['Month'] == latest_month]['Amount'].sum()
    if latest_spend > monthly_avg * 1.2:
        insights.append(f"⚠️ You spent ₹{latest_spend:.2f} in {latest_month}, which is 20% above your average monthly spend.")

    # Category overspend
    cat_avg = df.groupby('Category')['Amount'].mean()
    high_spend = cat_avg[cat_avg > cat_avg.mean() * 1.5]
    for cat in high_spend.index:
        insights.append(f"💰 High spending detected in '{cat}' category. Consider reducing your expenses there.")
    
    return insights