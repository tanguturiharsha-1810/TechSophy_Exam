import pandas as pd

def load_and_clean_data(filepath):
    # Try to read with header, if fails, add header manually
    try:
        df = pd.read_csv(filepath)
        if list(df.columns)[:4] != ['Date', 'Description', 'Amount', 'Category']:
            raise Exception('Wrong header')
    except Exception:
        df = pd.read_csv(filepath, header=None, names=['Date', 'Description', 'Amount', 'Category'])

    # Parse dates, coerce errors
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Amount to numeric, coerce errors
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    # Drop rows with missing Date or Amount
    df.dropna(subset=['Date', 'Amount'], inplace=True)
    # Clean Category: strip, title, fill missing as 'Unknown'
    df['Category'] = df['Category'].astype(str).str.strip().str.title().replace({'Nan': 'Unknown', '': 'Unknown'})
    # Remove extra spaces
    df['Category'] = df['Category'].str.replace(r'\s+', ' ', regex=True)
    # Add Month
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    return df
