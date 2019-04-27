from pymongo import MongoClient
from bson.objectid import ObjectId
import matplotlib.pyplot as plt
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

my_database = client.c4e
# Serious Excercise 1, 2:
my_coll = my_database["posts"]

my_mark = {
   "title" : "Track 7",
   "author": "HH",
   "content": '''You’re thinking to tell him bye, bye bye,
He gives you more I did you right, right right,
I mean I ain’t even got to try, I I,
Am never yours, but you’re mine, oh my, oh my,''' 
}

# my_coll.insert_one(my_mark)

# Serious Excercise 3:

my_db = client.c4e
my_coll = my_db["customers"]


customers = my_coll.find()
list_key = []
for i in customers:
   list_key.append(i['ref'])
names =['advertisements', 'organization', 'word of mount']

x = list_key.count('ads')/len(list_key) * 100
y = list_key.count('events')/len(list_key) * 100
z = list_key.count('wom')/len(list_key) * 100
values = [x, y, z]
plt.figure(1, figsize= (9, 3))
plt.ylabel("%")
plt.suptitle("event held by")
plt.plot(1,100)
plt.bar(names, values)
plt.show()