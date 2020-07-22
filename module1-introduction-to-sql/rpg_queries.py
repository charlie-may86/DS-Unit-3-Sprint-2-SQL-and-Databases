import os
import sqlite3

# construct a path to wherever your database exists
# DB_FILEPATH = "module1-introduction-to-sql/rpg_db.sqlite3"
# DB_FILEPATH = os.path.join(module1-introduction-to-sql, "..", "rpg_db.sqlite3")
# This file path works because the db is in the root file (module1-introduction...)
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM armory_weapon;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print(type(result2), result2)