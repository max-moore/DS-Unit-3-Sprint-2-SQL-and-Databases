# Importing - and also instantiating my connection and cursor
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Queries for printing out info about database
numchar_query = '''SELECT * 
                   FROM charactercreator_character;'''

numclasschar_query = '''SELECT * 
                        FROM '''

numitem_query = '''SELECT * 
                   FROM charactercreator_character_inventory;'''

numweapon_query = '''SELECT item_id
                     FROM charactercreator_character_inventory
                     JOIN armory_weapon
                        ON item_id = item_ptr_id;'''

numiteminv_query = '''SELECT character_id, COUNT(*)
                      FROM charactercreator_character_inventory
                      GROUP BY 1;'''          
            
numweaponinv_query = '''SELECT character_id, COUNT(item_ptr_id)
                        FROM charactercreator_character_inventory
                        LEFT JOIN armory_weapon
                            ON item_id = item_ptr_id
                        GROUP BY 1;'''

avgiteminv_query = '''SELECT AVG(CAST(char_numitems AS REAL))
                      FROM(SELECT character_id, COUNT(*) AS char_numitems
                           FROM charactercreator_character_inventory
                           GROUP BY 1);''' 

avgweaponinv_query = '''SELECT AVG(CAST(char_numweapons AS REAL))
                        FROM(SELECT character_id, COUNT(item_ptr_id) AS char_numweapons
                             FROM charactercreator_character_inventory
                             LEFT JOIN armory_weapon
                                 ON item_id = item_ptr_id
                             GROUP BY 1);''' 

# Fetching and printing number of characters
curs.execute(numchar_query)
numchar_results = curs.fetchall()

print("Number of Characters:", len(numchar_results))

# Iterating through the subclass tables and printing the number of characters for each class
for classtable in ['charactercreator_cleric', 
              'charactercreator_fighter', 
              'charactercreator_mage',
              'charactercreator_thief', 
              'charactercreator_necromancer']:
    
    class_query = 'SELECT * FROM ' + classtable + ';'
    
    curs.execute(class_query)
    classchar_results = curs.fetchall()

    # Necromancer is a subclass of Mage which is why we end up with more total characters than the original 302
    print("Number of", classtable[17:].capitalize() + 's:', len(classchar_results))

# Fetching and printing number of items
curs.execute(numitem_query)
numitem_results = curs.fetchall()
print("Number of Items:", len(numitem_results))

# Fetching and printing number of weapons
curs.execute(numweapon_query)
numweapon_results = curs.fetchall()
print("Number of Weapons:", len(numweapon_results))

# Fetching and printing number of items in characters' inventories
curs.execute(numiteminv_query)
numiteminv_results = curs.fetchall()
print("First 20 Characters and Number of Items in Inventory:\n", numiteminv_results[:20])

# Fetching and printing number of weapons in characters' inventories
curs.execute(numweaponinv_query)
numweaponinv_results = curs.fetchall()
print("First 20 Characters and Number of Weapons in Inventory:\n", numweaponinv_results[:20])

# Fetching and printing average number of items in characters' inventories
curs.execute(avgiteminv_query)
avgiteminv_results = curs.fetchall()
print("Average Number of Items in Inventory:\n", avgiteminv_results)

# Fetching and printing average number of weapons in characters' inventories
curs.execute(avgweaponinv_query)
avgweaponinv_results = curs.fetchall()
print("Average Number of Weapons in Inventory:\n", avgweaponinv_results)