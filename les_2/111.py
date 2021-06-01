# с готовыми условиями
from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

user_find = input('Введите вакансию:\n')

main_link = "https://hh.ru"
params = {"area":"1",
          "fromSearchLine":"true",
          "st":"searchVacancy",
          "text":user_find,
          "page":"0"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

next_butten = ''
n = 0
a = 0
vacances = []
while next_butten != None:
    if next_butten == '':
        response = requests.get(main_link + '/search/vacancy', params=params, headers=headers)
    else:
        response = requests.get(next_butten, headers=headers)
    if response.ok:
        soup = bs(response.text, "lxml")
        vacance_list = soup.findAll('div', attrs={'class': 'vacancy-serp-item'})


        for vacance in vacance_list:
            vacance_data = {}
            vacance_name = vacance.find('a', {'class': 'bloko-link'}).getText()
            vacance_link = vacance.find('a', {'class': 'bloko-link'}).attrs["href"]
            try:
                vacance_salary = vacance.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).getText()
            except Exception as e:
                vacance_salary = None
            site_link = main_link
            a +=1
            vacance_data['номер'] = a
            vacance_data['имя вакансии'] = vacance_name
            vacance_data['ссылка на вакансию'] = vacance_link
            vacance_data['зарплата'] = vacance_salary
            vacance_data['источник'] = site_link

            vacances.append(vacance_data)

        try:
            next_butten = main_link + soup.find('a', attrs={'data-qa':'pager-next'}).attrs["href"]
        except Exception as e:
            next_butten = None

        n +=1
pprint(vacances)
pprint(n)