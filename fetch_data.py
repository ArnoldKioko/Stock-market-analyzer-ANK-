import yfinance as yf
import pandas as pd
import os

# Stocks to track - feel free to change these
STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']

def fetch_stock_data(ticker, period='1y'):
    """Fetch 1 year of stock data for a given ticker."""
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df['Ticker'] = ticker
    df.reset_index(inplace=True)
    return df

def fetch_all_stocks():
    all_data = []
    for ticker in STOCKS:
        print(f"Fetching {ticker}...")
        df = fetch_stock_data(ticker)
        all_data.append(df)
    
    combined = pd.concat(all_data, ignore_index=True)
    
    # Save raw data
    os.makedirs('data/raw', exist_ok=True)
    combined.to_csv('data/raw/stocks_raw.csv', index=False)
    print(f"Saved {len(combined)} rows to data/raw/stocks_raw.csv")
    return combined

if __name__ == "__main__":
    fetch_all_stocks()