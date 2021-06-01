from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

# Кинопоиск
# https://www.kinopoisk.ru/popular/films/?quick_filters=serials&tab=all

main_link = "https://www.kinopoisk.ru"
params = {"quick_filters":"serials",
          'tab':"all"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
           }
response = requests.get(main_link + '/popular/films/', headers=headers, params=params)
if response.ok:
    soup = bs(response.text, 'html.parser')
    serial_list = soup.findAll('div', {'class':'desktop-rating-selection-film-item'})
    # print(len(serial_list))

    serials = []
    for serial in serial_list:
        serial_data = {}
        serial_name = serial.find('p')
        serial_link = main_link + serial_name.parent["href"]
        serial_name = serial_name.getText()
        serial_genre = serial.find('span', {'class': 'selection-film-item-meta__meta-additional-item'}).nextSibling.getText()
        serial_rating = serial.find('span', {'class': 'rating__value'}).getText()
        try:
            serial_rating = float(serial_rating)
        except Exception as e:
            serial_rating = None
        serial_data["name"] = serial_name
        serial_data["link"] = serial_link
        serial_data['genre'] = serial_genre
        serial_data["riting"] = serial_rating

        serials.append(serial_data)

pprint(serials)



