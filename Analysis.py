from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import numpy as np

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly'] = model.fit_predict(df[['Amount']])
    return df

def cluster_spending(df, n_clusters=3):
    cat_grouped = df.groupby('Category')['Amount'].sum().reset_index()
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cat_grouped['Cluster'] = kmeans.fit_predict(cat_grouped[['Amount']])
    return cat_grouped
