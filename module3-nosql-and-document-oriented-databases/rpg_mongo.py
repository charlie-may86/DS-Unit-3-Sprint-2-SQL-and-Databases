from pymongo import MongoClient
import os
from dotenv import load_dotenv
import os
import sqlite3
import json
import pandas as pd

# get the data in a format to added to mongoDB
DB_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "module1-introduction-to-sql", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

rpg_query = 'SELECT * FROM charactercreator_character;'
rpg_data = cursor.execute(rpg_query).fetchall()

columns = ['character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']

rpg_df = pd.DataFrame(rpg_data, columns=columns)
# print(rpg_df.head())

rpg_df.reset_index(inplace=True)
rpg_dict = rpg_df.to_dict('records')
print(rpg_dict)

# exit()
# print(rpg_data, type(rpg_data))

#convert to json

# rpg_json = json.dumps(rpg_data)
# print(rpg_json, type(rpg_json))
# rpg_dict = dict(rpg_data)
# print(rpg_dict, type(rpg_dict))

# exit()

# the code following the @ in the string below: cluster0.zqjps is the CLUSETER NAME

# client = pymongo.MongoClient("mongodb+srv://user323:<password>@cluster0.wbwyb.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.test

load_dotenv()

DB_USER = os.getenv("MONGO_USER2", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD2", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME2", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
print('-----------')
print('URI: ', connection_uri)


# run python in the terminal here to check if the above worked
# should return the URI
# exit()

client = MongoClient(connection_uri)
print('-----------')
print('CLIENT: ', type(client), client)
print('DATABASES: ', client.list_database_names())

# this break point allows you test the connection with client.list_database_names()
# if it works, things are good so far
# this is creating the connection between you and the MongoDB
# breakpoint()

db = client.rpg_database 
# "test_database" or whatever you want to call it "rpg_database" in this case
# this is creating the actual database, which is stored in the MongoDB cluster
# but it doesn't actually exist until data is inserted
print("----------------")
print("DB:", type(db), db)
print("COLLECTIONS:", db.list_collection_names())

collection = db.rpg_test
# this creates the table, or collection, which lives in the database 
# we will insert the rpg data into this collection

# need to fetch the data somehow. It exist somewhere.
# step 1: find it
# step 2: find a way to access it


collection.insert_many(rpg_dict)

print('DOCUMENTS COUNT:', collection.count_documents({}))