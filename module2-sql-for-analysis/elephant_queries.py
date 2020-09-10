import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", connection)
                            
cursor = connection.cursor()
print("CURSOR", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print(result)

# insertion_sql="""
# INSERT INTO test_table (name, data) VALUES
# ('A row name', null),
# ('Another row, with JSON', '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB);
# """
# cursor.execute(insertion_sql)

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }
insertion_query = "INSERT INTO test_table (name, data) VALUES %s"

# cursor.execute(insertion_query,
#     ('A rowwwww', 'null')
# )

# cursor.execute(insertion_query,
#     ('Another row, with JSONNNNN', json.dumps(my_dict))
# )

execute_values(cursor, insertion_query, [
    ('A rowwwww', 'null'),
    ('Another row, with JSONNNNN', json.dumps(my_dict)),
    ('Third row', "3")
])

connection.commit()

cursor.close()
connection.close()