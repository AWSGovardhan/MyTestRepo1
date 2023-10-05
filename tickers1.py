from nasdaq_symbols import symbols as nasdaq_symbols
from nyse_symbols import symbols as nyse_symbols

# Fetch NASDAQ ticker symbols and company names
nasdaq_data = nasdaq_symbols.get()

# Fetch NYSE ticker symbols and company names
nyse_data = nyse_symbols.get()

# Extract ticker symbols and company names from the data
nasdaq_tickers = nasdaq_data['Symbol'].tolist()
nasdaq_companies = nasdaq_data['Security Name'].tolist()

nyse_tickers = nyse_data['Symbol'].tolist()
nyse_companies = nyse_data['Security Name'].tolist()

# Print ticker symbols and company names
print("NASDAQ Tickers:")
for ticker, company in zip(nasdaq_tickers, nasdaq_companies):
    print(f"{ticker}: {company}")

print("\nNYSE Tickers:")
for ticker, company in zip(nyse_tickers, nyse_companies):
    print(f"{ticker}: {company}")
