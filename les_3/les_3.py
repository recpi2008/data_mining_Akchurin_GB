from pymongo import MongoClient
from pprint import pprint

# подготовка
client = MongoClient('localhost', 27017)

db = client['basa_1']
# db2 = client['basa_2'] # можно работать с несколькими базами данных
users = db.users # название коллекции
books = db.books

# работа с базой
# users.insert_one({
#     "name":"Ivan",
#     'age':35,
#     "увлечения":["buhf","чтение",'ddd']})
# result = users.find({})
#
# for user in result:
#     pprint(user)

# users.insert_many([{
#     "name":"Nik",
#     "age":55,
#     "pet":['cat','dog']},
#     {"name":"Joe",
#     "age":25,
#     "pet":['fish','dog']}])

# result = users.find({}) #чтение
# for user in result:
#     pprint(user)

# поиск
# result = users.find({'name':'Ivan'},{'увлечения':True, '_id':False}) #чтение, '_id':False - если выключить показ id
# for user in result:
#     pprint(user)

# сортировка
# result = users.find({'age':{'$lt':35}},{'name':True, 'age':True, '_id':False}) # '$gt' значит > , '$lt' значит <, '$gte'
#
# for user in result:
#     pprint(user)

# сортировка вывода
# result = users.find({}).sort('age', -1) # если 'age', -1 то поубыванию
# result = users.find({}).limit(2)
# for user in result:
#     pprint(user)

# сортировка через "или"
# result = users.find({'$or':[{"name":'Ivan'},{'age':25}]})
# for user in result:
#     pprint(user)

# обновление и исправления данных
# users.update_one({'name':'Ivan'},{'$set':{'age':27}})
# result = users.find({})
# for user in result:
#     pprint(user)

# Обновление через словарь
# doc = {
#     'name':'Ivan El',
#     'age':'25'}
# users.update_one({'name':'Ivan'},{'$set':doc})
# result = users.find({})
# for user in result:
#     pprint(user)

# users.update_many({'name':'Ivan'},{'$set':doc})

# перезаписать данные
# doc = {
#     'name':'Ivan El',
#     'age':'25'}
# users.replace_one({'name':'Ivan El'},doc)
# result = users.find({})
# for user in result:
#     pprint(user)

# удаление
# users.delete_one({'name': 'Nik'})
# result = users.find({})
# for user in result:
#     pprint(user)
