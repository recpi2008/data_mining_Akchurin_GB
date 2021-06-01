import json
from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

main_link = "https://hh.ru"
params = {"area":"1",
          "fromSearchLine":"true",
          "st":"searchVacancy",
          "text":"python",
          "page":"0"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

response = requests.get(main_link + '/search/vacancy', params=params, headers=headers)

if response.ok:
    soup = bs(response.text, "lxml")
    vacance_list = soup.findAll('div', attrs={'class':'vacancy-serp-item'})
    pprint(len(vacance_list))


    vacances = []
    for vacance in vacance_list:
        vacance_data = {}
        vacance_name = vacance.find('a', {'class':'bloko-link'}).getText()
        vacance_link = vacance.find('a', {'class':'bloko-link'}).attrs["href"]
        try:
            vacance_salary = vacance.find('span', {'data-qa':'vacancy-serp__vacancy-compensation'}).getText()
            vacance_salary = vacance_salary.replace('\u202f','').split()
            if '–' in vacance_salary:
                vacance_data['мин зарплата'] = vacance_salary[0]
                vacance_data['макс зарплата'] = vacance_salary[2]
                vacance_data['валюта'] = vacance_salary[-1]
            elif 'от' in vacance_salary:
                vacance_data['мин зарплата'] = vacance_salary[1]
                vacance_data['валюта'] = vacance_salary[-1]
            elif 'до' in vacance_salary:
                vacance_data['макс зарплата'] = vacance_salary[1]
                vacance_data['валюта'] = vacance_salary[-1]

        except Exception as e:
            vacance_data['зарплата'] = None


        site_link = main_link
        vacance_data['имя вакансии'] = vacance_name
        vacance_data['ссылка на вакансию'] = vacance_link
        vacance_data['источник'] = site_link

        vacances.append(vacance_data)
#
# pprint(vacances)
with open("les_hw_2_1.json", 'w', encoding="utf-8") as file:
    json.dump(vacances, file, indent=2, ensure_ascii=False)

