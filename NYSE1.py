import yfinance as yf

# Define the stock ticker symbol
ticker = 'SPCE'  # Example: Apple Inc. (AAPL)

# Fetch the stock data
data = yf.download(ticker, start='2023-06-01', end='2023-06-30')

# Print the fetched data
print(data.head())
print(data.tail())
