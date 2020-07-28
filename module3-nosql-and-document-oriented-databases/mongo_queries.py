from pymongo import MongoClient
import os
from dotenv import load_dotenv



# DB_URL = "mongodb+srv://user123:<password>@cluster0.0doa0.mongodb.net/<dbname>?retryWrites=true&w=majority"


# client = pymongo.MongoClient(DB_URL)
# db = client.test

# app/mongo_queries.py

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
# print("----------------")
# print("URI:", connection_uri)



client = MongoClient(connection_uri)
# print("----------------")
# print("CLIENT:", type(client), client)
# print("DATABASES:", client.list_database_names())


db = client.my_test_database # "test_database" or whatever you want to call it
# print("----------------")
# print("DB:", type(db), db)
# print("COLLECTIONS:", db.list_collection_names())

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
# print("----------------")
# print("COLLECTION:", type(collection), collection)

# print("DOCUMENTS COUNT:", collection.count_documents({}))


# print("----------------")
# print("COLLECTIONS:")
# print(db.list_collection_names())


print('PIKA COUNT:', collection.count_documents({'name': 'Pikachu'}))



for doc in collection.find({'level': {'$gt': 20}}):
    print(doc)

exit()

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))

# Insert many

bulbasaur = {
    'name': 'Bulbasaur',
    'type': 'grass', 
    'moves': ['leech seed', 'solar beam']
}

eevee = {
    'name': 'Eevee',
    'level': 40,
    'exp': 7500,
    'hp': 120
}

chansey = {
    'name': 'chansey',
    'egg group': 'fairy',
    'pokedex color': 'Pink'
}

jirachi = {
    'lvl': 100,
    'power': 'UNLIMITED',
    'favorite_item': 'Pokeflute'
}

team = [bulbasaur, eevee, chansey, jirachi]

breakpoint()

collection.insert_many(team)

print('DOCUMENTS COUNT:', collection.count_documents({}))