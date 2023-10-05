import yfinance as yf

data = yf.download('SPCE', start='2023-01-01', end='2023-07-01')
print(data['Close'])
