import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_spending(df):
    cat_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=cat_totals.index, y=cat_totals.values)
    plt.xticks(rotation=45)
    plt.title("Total Spending by Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

def plot_monthly_trend(df):
    monthly = df.groupby('Month')['Amount'].sum()
    plt.figure(figsize=(10, 4))
    monthly.plot(marker='o')
    plt.title("Monthly Spending Trend")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
