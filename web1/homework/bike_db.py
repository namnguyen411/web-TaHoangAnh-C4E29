from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb+srv://admin:admin@c4e29-cluster-r1jps.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

bike_db = client.bikes_list

Bikes = bike_db["Bikes"]