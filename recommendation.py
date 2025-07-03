def generate_recommendation(df):
    insights = []

    # Lowered threshold for more frequent alerts
    monthly_avg = df.groupby('Month')['Amount'].sum().mean()
    latest_month = df['Month'].max()
    latest_spend = df[df['Month'] == latest_month]['Amount'].sum()
    if latest_spend > monthly_avg * 1.05:
        insights.append(f"⚠️ You spent ₹{latest_spend:.2f} in {latest_month}, which is 5% above your average monthly spend.")

    # Category overspend (lowered threshold)
    cat_avg = df.groupby('Category')['Amount'].mean()
    high_spend = cat_avg[cat_avg > cat_avg.mean() * 1.1]
    for cat in high_spend.index:
        insights.append(f"💰 High spending detected in '{cat}' category. Consider reducing your expenses there.")

    # Top spending month
    month_totals = df.groupby('Month')['Amount'].sum()
    top_month = month_totals.idxmax()
    top_month_amt = month_totals.max()
    insights.append(f"📅 Your highest spending month was {top_month} with ₹{top_month_amt:.2f} spent.")

    # Top spending category
    cat_totals = df.groupby('Category')['Amount'].sum()
    top_cat = cat_totals.idxmax()
    top_cat_amt = cat_totals.max()
    insights.append(f"🏆 You spent the most on '{top_cat}' (₹{top_cat_amt:.2f}).")

    # Highlight unknown/missing categories
    unknown_count = (df['Category'] == 'Unknown').sum()
    if unknown_count > 0:
        insights.append(f"❓ {unknown_count} transactions have an unknown or missing category. Consider cleaning your data.")

    return insights
