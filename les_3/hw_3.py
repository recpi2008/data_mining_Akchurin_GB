import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import json
from pymongo import MongoClient

user_find = input('Введите вакансию:\n')

all_list= []

main_link_sj = "https://www.superjob.ru/"
params_sj = {"keywords":user_find,
        "geo%5Bt%5D%5B0%5D":"4"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

next_butten_sj = ''
n = 0
a = 0

while next_butten_sj != None:
    if next_butten_sj == '':
        response = requests.get(main_link_sj + "vacancy/search/", params=params_sj, headers=headers)
    else:
        response = requests.get(next_butten_sj, headers=headers)
    if response.ok:
        soup = bs(response.text, 'lxml')
        sj_vacancy_list = soup.findAll('div',{'class':'iJCa5 f-test-vacancy-item _1fma_ _2nteL'})

        for vacancy in sj_vacancy_list:
            vacancy_sj_data = {}
            try:
                vacancy_sj_name = vacancy.find("a", {'class':'icMQ_'}).getText()
            except:
                vacancy_sj_name = None
            try:
                vacancy_sj_link = main_link_sj + vacancy.find('a', {'class': 'icMQ_'}).attrs["href"]

            except:
                vacancy_sj_link = None
            try:
                vacancy_sj_company = vacancy.find('span',{'class':'f-test-text-vacancy-item-company-name'}).getText()
            except:
                vacancy_sj_company = None
            try:
                vacancy_sj_time = vacancy.find('span', {'class':"_1h3Zg e5P5i _2hCDz _2ZsgW"}).getText()
            except:
                vacancy_sj_time = None
            try:
                vacancy_sj_salary = vacancy.find("span", {'class': "_1OuF_ _1qw9T f-test-text-company-item-salary"}).getText()
                if '—' in vacancy_sj_salary:
                    sal = vacancy_sj_salary.replace('\xa0',' ').split()
                    if sal[0].isdigit() and sal[1].isdigit():
                        mim_sal = sal[0]+sal[1]
                        vacancy_sj_data['мин зарплата'] = float(mim_sal)
                    else:
                        vacancy_sj_data['мин зарплата'] = float(sal[0])
                    if sal[-3].isdigit() and sal[-2].isdigit():
                        max_sal = sal[-3]+sal[-2]
                        vacancy_sj_data['макс зарплата'] = float(max_sal)
                    else:
                        vacancy_sj_data['макс зарплата'] = float(sal[-3])
                    vacancy_sj_data['валюта'] = sal[-1]
                elif 'По' in vacancy_sj_salary:
                    vacancy_sj_data['зарплата'] = "По договоренности"
                    vacancy_sj_data['валюта'] = None
                elif 'от' in vacancy_sj_salary:
                    sal = vacancy_sj_salary.replace('\xa0', ' ').split()
                    if sal[1].isdigit() and sal[2].isdigit():
                        mim_sal = sal[1]+sal[2]
                        vacancy_sj_data['мин зарплата'] = float(mim_sal)
                    else:
                        vacancy_sj_data['мин зарплата'] = float(sal[1])
                    vacancy_sj_data['валюта'] = sal[-1]
                elif 'до' in vacancy_sj_salary:
                    sal = vacancy_sj_salary.replace('\xa0', ' ').split()
                    if sal[1].isdigit() and sal[2].isdigit():
                        max_sal = sal[1]+sal[2]
                        vacancy_sj_data['макс зарплата'] = float(max_sal)
                    else:
                        vacancy_sj_data['макс зарплата'] = float(sal[1])
                    vacancy_sj_data['валюта'] = sal[-1]
                else:
                    sal = vacancy_sj_salary.replace('\xa0', ' ').split()
                    if sal[0].isdigit() and sal[1].isdigit():
                        user_sal = sal[0]+sal[1]
                        vacancy_sj_data['макс зарплата'] = float(user_sal)
            except:
                vacancy_sj_data['зарплата'] = None


            a += 1
            vacancy_sj_data['номер'] = a
            vacancy_sj_data['вакансия'] = vacancy_sj_name
            vacancy_sj_data['ссылка на вакансию'] = vacancy_sj_link
            vacancy_sj_data['кампания'] = vacancy_sj_company
            vacancy_sj_data['время'] = vacancy_sj_time
            vacancy_sj_data['источник'] = main_link_sj

            all_list.append(vacancy_sj_data)

        try:
            next_butten_sj = main_link_sj + soup.find('a', attrs={'class': 'f-test-button-dalshe'}).attrs["href"]
        except Exception as e:
            next_butten_sj = None
        n += 1

# pprint(vacancy_sj)



main_link_hh = "https://hh.ru"
params_hh = {"area":"1",
          "fromSearchLine":"true",
          "st":"searchVacancy",
          "text":user_find,
          "page":"0"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

next_butten_hh = ''
n = 0


while next_butten_hh != None:
    if next_butten_hh == '':
        response = requests.get(main_link_hh + '/search/vacancy', params=params_hh, headers=headers)
    else:
        response = requests.get(next_butten_hh, headers=headers)
    if response.ok:
        soup = bs(response.text, "lxml")
        vacance_list_hh = soup.findAll('div', attrs={'class': 'vacancy-serp-item'})


        for vacance in vacance_list_hh:
            vacance_data_hh = {}
            vacance_name = vacance.find('a', {'class': 'bloko-link'}).getText()
            vacance_link = vacance.find('a', {'class': 'bloko-link'}).attrs["href"]
            try:
                vacance_salary = vacance.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).getText()
                vacance_salary = vacance_salary.replace('\u202f', '').split()
                if '–' in vacance_salary:
                    vacance_data_hh['мин зарплата'] = float(vacance_salary[0])
                    vacance_data_hh['макс зарплата'] = float(vacance_salary[2])
                    vacance_data_hh['валюта'] = vacance_salary[-1]
                elif 'от' in vacance_salary:
                    vacance_data_hh['мин зарплата'] = float(vacance_salary[1])
                    vacance_data_hh['валюта'] = vacance_salary[-1]
                elif 'до' in vacance_salary:
                    vacance_data_hh['макс зарплата'] = float(vacance_salary[1])
                    vacance_data_hh['валюта'] = vacance_salary[-1]
            except Exception as e:
                vacance_data_hh['зарплата'] = None


            a +=1
            vacance_data_hh['номер'] = a
            vacance_data_hh['вакансия'] = vacance_name
            vacance_data_hh['ссылка на вакансию'] = vacance_link
            vacance_data_hh['источник'] = main_link_hh

            all_list.append(vacance_data_hh)

        try:
            next_butten_hh = main_link_hh + soup.find('a', attrs={'data-qa':'pager-next'}).attrs["href"]
        except Exception as e:
            next_butten_hh = None

# pprint(vacances_hh)




# with open("les_hw_3.json", 'w', encoding="utf-8") as file:
#     json.dump(all_list, file, indent=2, ensure_ascii=False)

# подготовка
client = MongoClient('localhost', 27017)
db = client['basa_job']
jobs = db.jobs
jobs.insert_many(all_list)


# не получилась
# result = jobs.find({})
# jobs.update(result, all_list, upsert=True)
# result = jobs.find({})
# for job in result:






