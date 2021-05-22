# b65401f8fda8bd10b4ddc771be28156f

import requests
from pprint import pprint

main_link = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": 'moscow',
          "appid": "b65401f8fda8bd10b4ddc771be28156f"}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
           'Accept':'*/*'}
response = requests.get(main_link, params = params, headers = headers)
j_body = response.json()

pprint(j_body)
print(f"В городе {j_body.get('name')} температура {round(j_body.get('main').get('temp') - 273)}")

