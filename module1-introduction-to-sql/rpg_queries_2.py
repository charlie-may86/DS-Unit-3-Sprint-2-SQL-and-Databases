import os
import json
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import psycopg2
import pandas as pd
import numpy as np
# from psycopg2.extensions import register_adapter, AsIs

# code to create the table
'''
CREATE TABLE titanic_table (
  id SERIAL PRIMARY KEY,
  survived INTEGER,
  pclass INTEGER,
  name  VARCHAR NOT NULL,
  sex VARCHAR NOT NULL,
  age FLOAT,
  sib_spouse_count INTEGER,
  parent_children_count INTEGER,
  fare FLOAT
);
'''
#code to avoid nan bugs - think
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME2")
DB_USER = os.getenv("DB_USER2")
DB_PASSWORD = os.getenv("DB_PASSWORD2")
DB_HOST = os.getenv("DB_HOST2")

# print(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

# exit()

df = pd.read_csv('titanic.csv')

# df = pd.read_csv('module1-introduction-to-sqltitanic.csv')

titanic_tuple = list(df.to_records(index=True))

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

insertion_query = "INSERT INTO titanic_table(id, survived, pclass, name, sex, age, sib_spouse_count, parent_children_count, fare) VALUES %s"
execute_values (cursor, insertion_query, titanic_tuple)
 

connection.commit()

cursor.close()
connection.close()