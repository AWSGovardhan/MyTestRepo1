import requests
url = 'https://sandbox.seamlesschex.com/v1/paymentlink/list?limit=15&page=1&sort=date&direction=DESC'
headers = {
  'Content-Type': 'application/json',
  'Authorization': '{{}}'
}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
print(response.text)