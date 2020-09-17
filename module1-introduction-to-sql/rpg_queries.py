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

# rpg_query = 'SELECT * FROM charactercreator_character;'
# rpg_data = cursor.execute(rpg_query).fetchall()
# print(rpg_data)

# result1 = cursor.execute(query1).fetchall()
# print(type(result1), result1)

'''
Question 1: How many total Characters are there?
'''

question1_query = '''
SELECT
	COUNT(character_id)
FROM
	charactercreator_character;
'''

result1 = cursor.execute(question1_query).fetchall()
print(f'There are {result1} total characters')

'''
Question 2: How many of each specific subclass?
'''

question2_query1 = '''
SELECT
	COUNT(charactercreator_mage.has_pet) AS MageCount
FROM
	charactercreator_mage;
'''

result2_1 = cursor.execute(question2_query1).fetchall()
print(f'There are {result2_1} mage characters')

question2_query2 = '''
SELECT
	COUNT(charactercreator_thief.is_sneaking) AS ThiefCount
FROM
	charactercreator_thief;
'''

results2_2 = cursor.execute(question2_query2).fetchall()
print(f'There are {results2_2} theif characters')

question2_query3 = '''
SELECT
	COUNT(character_ptr_id) AS ClericCount
FROM
	charactercreator_cleric;
'''

results2_3 = cursor.execute(question2_query3).fetchall()
print(f'There are {results2_3} cleric characters')

question2_query4 = '''
SELECT
	COUNT(character_ptr_id) AS FighterCount
FROM
	charactercreator_fighter;
'''

results2_4 = cursor.execute(question2_query4).fetchall()
print(f'There are {results2_4} fighter characters')

'''
Question 3: How many total Items?
'''

question3_query = '''
SELECT
	COUNT(item_id) AS TotalItems
FROM
	armory_item;
'''

results3 = cursor.execute(question3_query).fetchall()
print(f'There are {results3} items')

'''
Question 4: How many of the Items are weapons? How many are not?
'''

question4_query1 = '''
SELECT
	COUNT(item_ptr_id) AS TotalWeapons
FROM
	armory_weapon;
'''

results4_1 = cursor.execute(question4_query1).fetchall()
print(f'There are {results4_1} total weapons in Items')

question4_query2 = '''
SELECT
	COUNT(item_id) - 37 AS NonWeapons
FROM
	armory_item;
'''

results4_2 = cursor.execute(question4_query2).fetchall()
print(f'There are {results4_2} non weapons in Items')

'''
Question 5: How many Items does each character have? (Return first 20 rows)
'''

question5_query = '''
SELECT
	character_id,
	COUNT(character_id) AS TotalItems
FROM
	charactercreator_character_inventory
GROUP BY
	character_id
ORDER BY
	COUNT(character_id)
	DESC
LIMIT 20;
'''

results5 = cursor.execute(question5_query).fetchall()
print(results5)

'''
Question 6: How many Weapons does each character have? (Return first 20 rows)
'''

question6_query = '''
SELECT
	cci.character_id,
	COUNT(cci.character_id) AS TotalWeapons
FROM
	charactercreator_character_inventory AS cci
	JOIN armory_weapon AS aw ON cci.item_id = aw.item_ptr_id
GROUP BY
	cci.character_id
ORDER BY
	COUNT(cci.character_id)
	DESC
LIMIT 20;
'''

results6 = cursor.execute(question6_query).fetchall()
print(results6)

'''
Question 7: On average, how many Items does each Character have?
'''

question7_query = '''
SELECT
	ROUND(CAST(COUNT(character_id) AS Float) 
	/ COUNT(DISTINCT (character_id)), 2) AS AverageItem
FROM
	charactercreator_character_inventory;
'''

results7 = cursor.execute(question7_query).fetchall()
print(f'Characters have on average {results7} items')

'''
Questioin 8: On average, how many Weapons does each character have?
'''

question8_query = '''
SELECT
	ROUND (AVG(weapon_count), 2) AS AverageWeapon
FROM (
	SELECT
		c.character_id,
		COUNT(DISTINCT w.item_ptr_id) AS weapon_count
	FROM
		charactercreator_character c
	LEFT JOIN charactercreator_character_inventory inv 
	ON c.character_id = inv.character_id
	LEFT JOIN armory_weapon w 
	ON inv.item_id = w.item_ptr_id
GROUP BY
	c.character_id) subquery
'''

results8 = cursor.execute(question8_query).fetchall()
print(f'Characters have on average {results8} weapons')