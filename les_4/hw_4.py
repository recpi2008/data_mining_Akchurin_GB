import requests
from lxml import html
from pprint import pprint
from pymongo import MongoClient

header = {"User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

main_url_lenta = "https://lenta.ru/"
response = requests.get(main_url_lenta, headers=header)

dom_lenta = html.fromstring(response.text)

items_lenta = dom_lenta.xpath('//div[contains(@class,"b-yellow-box__wrap")]//div[contains(@class,"item")]')

all_list = []
a = 0
for item in items_lenta:
    lenta_item = {}

    text_news = item.xpath(".//a/text()")[0].replace('\xa0',' ')
    lenta_item["text_news"] = text_news

    link_news = main_url_lenta + item.xpath(".//a/@href")[0]
    lenta_item["link_news"] = link_news

    response_data = requests.get(link_news, headers=header)
    dom_lenta_data = html.fromstring(response_data.text)
    data_lenta = dom_lenta_data.xpath('.//time[@class="g-date"]/text()')

    lenta_item["data_news"] = "".join(data_lenta)

    lenta_item["source_news"] = main_url_lenta

    a +=1
    all_list.append(lenta_item)

# pprint(lenta_list)
# pprint(a)

main_url_yandex = "https://yandex.ru/news"
response_yandex = requests.get(main_url_yandex, headers=header)
dom_yandex = html.fromstring(response_yandex.text)

items_yandex = dom_yandex.xpath('//div[@class="mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top"]//div[contains(@class,"mg-grid__col")]')
for item in items_yandex:
    yandex_item = {}

    name_yandex = item.xpath('.//h2[@class="mg-card__title"]/text()')[0].replace('\xa0',' ')
    link_yandex = item.xpath(".//a/@href")[0]
    source_yandex = item.xpath(".//a[@class='mg-card__source-link']/text()")
    time_yandex = item.xpath('.//span[@class="mg-card-source__time"]/text()')
    main_url_yandex = item.xpath(".//a[@class='mg-card__source-link']/text()")

    yandex_item["text_news"] = name_yandex
    yandex_item["link_news"] = link_yandex
    yandex_item["source_news"] = ''.join(source_yandex)
    yandex_item["data_news"] =  ''.join(time_yandex)


    all_list.append(yandex_item)

main_url_mail = "https://news.mail.ru/"
response = requests.get(main_url_mail, headers=header)

dom_mail = html.fromstring(response.text)
items_mail = dom_mail.xpath("//div[@class='block']")

for item in items_mail:

    link_mail = list(set(item.xpath('.//a/@href')))

for item_l in link_mail:
    response = requests.get(item_l, headers=header)
    dom_mail = html.fromstring(response.text)
    items_mail = dom_mail.xpath("//div[@class='block']")


    mail_item = {}
    mail_item["link_news"] = item_l

    for item in items_mail:

        name_mail = item.xpath('//h1/text()')
        source_mail = item.xpath("//a[@class='link color_gray breadcrumbs__link']//text()")
        time_mail = item.xpath("//span[@class='note__text breadcrumbs__text js-ago']//text()")

        mail_item["text_news"] = ''.join(name_mail)
        mail_item["source_news"] = ''.join(source_mail)
        mail_item["data_news"] = ''.join(time_mail)
        # pprint(1)


        all_list.append(mail_item)

# pprint(all_list)

client = MongoClient('localhost', 27017)
db = client['basa_news']
news = db.news
news.insert_many(all_list)



