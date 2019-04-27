from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb+srv://admin:admin@c4e29-cluster-r1jps.mongodb.net/test?retryWrites=true"

# Create connection
client = MongoClient(uri)

# 2. Get/ Create database
# first_db = client.tên database muốn đặt
first_db = client.first_database

# 3. Get/ Create collection
first_coll = first_db["first_collection"]

# 4. Create document

game_list = [{
    "game": "Pikachu",
    "description" : "Alawys lost money",
},
{
    "game" : "FO4",
    "description" : "football game"
}]
# 5. CREATE 
# 5.1 Create one

# first_coll.insert_one(first_document)

# 5.2 Create many

# first_coll.insert_many(game_list)

# 6. READ
# 6.1 Read all

# all_games = first_coll.find()
# Lazy loading

# for game in all_games:
    # print(game)

# 6.2 Read one
# pikachu_game = first_coll.find_one({'_id': ObjectId('5cc064ecfaf53eb322c7c302') })
# print(pikachu_game)

# # 7. UPDATE
# pikachu_game = first_coll.find_one({'_id': ObjectId('5cc05f3f397d25f2776ad101') })
# new_value = { "$set": { "game": "AUTO CHESS" } }
# first_coll.update_one(pikachu_game, new_value)
# print(pikachu_game)

# 8. DELETE
pikachu_game = first_coll.find_one({'_id': ObjectId('5cc05f3f397d25f2776ad101') })
if pikachu_game is not None:
    first_coll.delete_one(pikachu_game)
else:
    print("Not Found")