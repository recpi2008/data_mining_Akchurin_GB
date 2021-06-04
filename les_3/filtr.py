from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['basa_job']
jobs_3 = db.jobs_3

# сортировка
result = jobs_3.find({'макс зарплата':{'$gt':50000}},{'вакансия':True, 'кампания': True,'ссылка на вакансию':True, 'макс зарплата':True, '_id':False}) # '$gt' значит > , '$lt' значит <, '$gte'

for user in result:
    pprint(user)
