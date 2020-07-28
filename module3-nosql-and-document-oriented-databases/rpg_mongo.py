from pymongo import MongoClient
import os
from dotenv import load_dotenv


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

