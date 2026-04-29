import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('../visuals', exist_ok=True)
df = pd.read_csv('data/cleaned/stocks_clean.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Chart 1: Stock Price Over Time
plt.figure(figsize=(14, 6))
for ticker in df['Ticker'].unique():
    subset = df[df['Ticker'] == ticker]
    plt.plot(subset['Date'], subset['Close'], label=ticker)

plt.title('Stock Closing Prices - Last 1 Year', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.tight_layout()
plt.savefig('../visuals/stock_prices_over_time.png')
plt.show()

# Chart 2: Average Daily Return by Stock
avg_return = df.groupby('Ticker')['Daily_Return_%'].mean().sort_values()
plt.figure(figsize=(10, 5))
avg_return.plot(kind='barh', color='steelblue')
plt.title('Average Daily Return % by Stock')
plt.xlabel('Return %')
plt.tight_layout()
plt.savefig('../visuals/avg_daily_return.png')
plt.show()

# Chart 3: Correlation Heatmap of Closing Prices
pivot = df.pivot_table(values='Close', index='Date', columns='Ticker')
plt.figure(figsize=(8, 6))
sns.heatmap(pivot.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Stock Prices')
plt.tight_layout()
plt.savefig('../visuals/correlation_heatmap.png')
plt.show()