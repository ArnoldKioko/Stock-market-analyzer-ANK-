import pandas as pd
import sqlite3

def load_to_sqlite():
    df = pd.read_csv('data/cleaned/stocks_clean.csv')
    
    conn = sqlite3.connect('database/stocks.db')
    df.to_sql('stock_prices', conn, if_exists='replace', index=False)
    print("Data loaded into SQLite database!")
    conn.close()

if __name__ == "__main__":
    import os
    os.makedirs('database', exist_ok=True)
    load_to_sqlite()