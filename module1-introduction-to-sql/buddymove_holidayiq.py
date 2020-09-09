import pandas as pd 
import sqlite3

review = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

review.to_sql('review', conn, if_exists = 'replace')

query = '''SELECT COUNT(*)
           FROM review;'''

natureshopping_query = '''SELECT COUNT(*)
                          FROM review
                          WHERE Shopping >= 100
                            AND Nature >= 100;'''

# Fetching and printing number of items
curs.execute(query)
results = curs.fetchall()
print(results)

# Fectching and printing number of users with 100 reviews on nature and shopping
curs.execute(natureshopping_query)
natureshopping_results = curs.fetchall()
print(natureshopping_results)