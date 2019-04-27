from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

my_db = client.c4e

my_coll = my_db["river"]
river = my_coll.find()
list_name_river_in_Africa = []
list_name_river_in_S_America = []
for i in river:
    if "Africa" in i['continent']:
        list_name_river_in_Africa.append(i['name'])
    elif "S. America" in i['continent'] and i['length'] < 1000:
        list_name_river_in_S_America.append(i['name'])
print("River in Africa: ")
print(', '.join(list_name_river_in_Africa))
print("River in S.America with length < 1000 km: ")
print(', '.join(list_name_river_in_S_America))

