from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-r1jps.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

foods_db = client.foods_app

Foods = foods_db["foods"]



