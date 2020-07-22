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

# Write your query
# query1 = "SELECT * FROM armory_weapon;"



#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

# result1 = cursor.execute(query1).fetchall()
# print(type(result1), result1)

'''
Question 1: How many total Characters are there?
'''

question1_query = 'SELECT COUNT(character_id) FROM charactercreator_character;'

result1 = cursor.execute(question1_query).fetchall()
print(f'There are {result1} total characters')

'''
Question 2: How many of each specific subclass?
'''

question2_query1 = 'SELECT COUNT(charactercreator_mage.has_pet) as MageCount FROM charactercreator_mage;'

result2_1 = cursor.execute(question2_query1).fetchall()
print(f'There are {result2_1} mage characters')

question2_query2 = 'SELECT COUNT(charactercreator_thief.is_sneaking) as ThiefCount FROM charactercreator_thief;'

results2_2 = cursor.execute(question2_query2).fetchall()
print(f'There are {results2_2} theif characters')

question2_query3 = 'SELECT COUNT(character_ptr_id) as ClericCount FROM charactercreator_cleric;'

results2_3 = cursor.execute(question2_query3).fetchall()
print(f'There are {results2_3} cleric characters')

question2_query4 = 'SELECT COUNT(character_ptr_id) as FighterCount FROM charactercreator_fighter;'

results2_4 = cursor.execute(question2_query4).fetchall()
print(f'There are {results2_4} fighter characters')

'''
Question 3: How many total Items?
'''

question3_query = 'SELECT COUNT(item_id) as TotalItems FROM armory_item;'

results3 = cursor.execute(question3_query).fetchall()
print(f'There are {results3} items')

'''
Question 4: How many of the Items are weapons? How many are not?
'''

question4_query1 = 'SELECT COUNT(item_ptr_id) as TotalWeapons FROM armory_weapon;'

results4_1 = cursor.execute(question4_query1).fetchall()
print(f'There are {results4_1} total weapons in Items')

question4_query2 = 'SELECT COUNT(item_id) - 37 as NonWeapons FROM armory_item;'

results4_2 = cursor.execute(question4_query2).fetchall()
print(f'There are {results4_2} non weapons in Items')

'''
Question 5: How many Items does each character have? (Return first 20 rows)
'''

question5_query = 'SELECT character_id, COUNT(character_id) as TotalItems from charactercreator_character_inventory GROUP BY character_id ORDER BY COUNT(character_id) DESC LIMIT 20;'

results5 = cursor.execute(question5_query).fetchall()
print(results5)