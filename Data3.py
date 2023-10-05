import requests
from bs4 import BeautifulSoup

def scrape_exchange_symbols(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')
    symbols = []
    companies = []
    for row in rows[1:]:
        columns = row.find_all('td')
        symbol = columns[0].text.strip()
        company = columns[1].text.strip()
        symbols.append(symbol)
        companies.append(company)
    return symbols, companies

# Scrape NASDAQ symbols and company names
nasdaq_url = 'https://en.wikipedia.org/wiki/List_of_companies_listed_on_NASDAQ'
nasdaq_symbols, nasdaq_companies = scrape_exchange_symbols(nasdaq_url)

# Scrape NYSE symbols and company names
nyse_url = 'https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_New_York_Stock_Exchange'
nyse_symbols, nyse_companies = scrape_exchange_symbols(nyse_url)

# Print ticker symbols and company names
print("NASDAQ Tickers:")
for symbol, company in zip(nasdaq_symbols, nasdaq_companies):
    print(f"{symbol}: {company}")

print("\nNYSE Tickers:")
for symbol, company in zip(nyse_symbols, nyse_companies):
    print(f"{symbol}: {company}")
