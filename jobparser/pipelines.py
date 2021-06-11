# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancy2021


    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        if item['sourse'] == 'superjob.ru':
            ready_salary = self.process_salary_sj(item['salary'])
            item['min_salary'] = ready_salary[0]
            item['max_salary'] = ready_salary[1]
            item['currency'] = ready_salary[-1]
        elif item['sourse'] == 'hh.ru':
            ready_salary = self.process_salary_hh(item['salary'])
            item['min_salary'] = ready_salary[1]
            item['max_salary'] = ready_salary[3]
            item['currency'] = ready_salary[-1]

        del item['salary']
        collection.insert_one(item)

        return item

    def process_salary_hh(self, salary):
        salary = salary[0].replace('\xa0', '').split(' ')
        # print(1)
        if 'от' in salary:
            if 'до' in salary:
                return salary
            else:
                salary.insert(2, None)
                salary.insert(2, None)
                return salary
        elif 'з/п' in salary:
            salary = [None,None,None,None,None]
            return salary
        elif 'до' in salary:
            salary.insert(0, None)
            salary.insert(0, None)
            return salary

    def process_salary_sj(self, salary):
        if 'По' in salary:
            salary = [None,None,None,None,None]
            return salary
        elif 'от' in salary:
            salary = salary[2].split('\xa0')
            currency = salary.pop()
            salary = float(''.join(salary))
            salary= [salary,currency]
            return salary
        elif '—' in salary:
            salary = [salary[0].replace('\xa0',''), salary[4].replace('\xa0',''), salary[6]]
            return salary
        elif 'до' in salary:
            salary = salary[2].split('\xa0')
            currency = salary.pop()
            salary = float(''.join(salary))
            salary = [salary, currency]
            salary.insert(0, None)
            return salary














