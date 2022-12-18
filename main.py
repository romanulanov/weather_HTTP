import requests

cities = ["Лондон", "Шереметьево", "Череповец"]
url_params = {"nTFqM": '', "lang": "ru"}

for city in cities:
  response = requests.get('https://wttr.in/{}'.format(city), params=url_params)
  response.raise_for_status()
  print(response.text)
