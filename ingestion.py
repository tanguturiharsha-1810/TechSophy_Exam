import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  
    df.dropna(subset=['Date', 'Amount'], inplace=True)
    df['Category'] = df['Category'].str.strip().str.title()
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    return df
