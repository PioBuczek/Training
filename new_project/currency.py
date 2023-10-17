import requests

url = "http://api.nbp.pl/api/exchangerates/tables/A/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Bład", response.status_code())
