import yfinance as yf  
import matplotlib.pyplot as plt
 
data = yf.download('BTC-USD','2021-01-01','2021-09-30')
# print(data.head())
# print(len(data))

# data = yf.download(['BTC-USD','AMD'],'2021-01-01','2021-09-30')
data["Close"].plot()
plt.show()