import pandas as pd
import os

def clean_stock_data(input_path='data/raw/stocks_raw.csv'):
    df = pd.read_csv(input_path)
    
    # 1. Check for missing values
    print("Missing values:\n", df.isnull().sum())
    
    # 2. Drop duplicates
    df.drop_duplicates(inplace=True)
    
    # 3. Convert date column
    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.date
    
    # 4. Round prices to 2 decimal places
    for col in ['Open', 'High', 'Low', 'Close']:
        df[col] = df[col].round(2)
    
    # 5. Add useful columns
    df['Daily_Return_%'] = (
        (df['Close'] - df['Open']) / df['Open'] * 100
    ).round(2)
    
    df['Price_Range'] = (df['High'] - df['Low']).round(2)
    
    # 6. Save cleaned data
    os.makedirs('data/cleaned', exist_ok=True)
    df.to_csv('data/cleaned/stocks_clean.csv', index=False)
    print(f"Cleaned data saved: {len(df)} rows")
    return df

if __name__ == "__main__":
    clean_stock_data()