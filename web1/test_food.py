from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-r1jps.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

test_db = client.foods_app

Foods = test_db["test-foods"]
