import sqlite3 as sql

# Connecting to database - if database does not exist, this will create a new db with the name passed in
# For temporary databases (not saved when script/program ends) use the name ":memory:"
conn = sql.connect('firstSQLiteDB.db')

# Creating a cursor for the database
# Cursors will be used to do stuff to databases (i.e. add table, add field (?))
# Basically the thing to run SQL Commands to sqlite db
myCur = conn.cursor()

# Datatypes in SQLite
# 1. NULL
# 2. INTEGER - Whole Numbers (1, 2, 3, etc.)
# 3. REAL - Decimal Numbers (i.e. 1.234)
# 4. TEXT - String
# 5. BLOB - Custom Object (Think class objects. I.e. Image, sound data, etc)

# ==============================================================================
# # Creating a table (using cursor) - uncomment the block below to use
# ==============================================================================
# myCur.execute(
#     '''
#         CREATE TABLE customers(
#             first_name TEXT,
#             last_name TEXT,
#             email TEXT
#         )
#     '''
# )
# ==============================================================================

# ==============================================================================
# # Inserting fields/data into the table (using cursor) - uncomment the block below to use
# ==============================================================================
# myCur.execute(
#     '''
#         INSERT INTO customers VALUES(
#             "steve",
#             "",
#             "burgers@stevedonalds.com"
#         )
#     '''
# )
# ==============================================================================

# ==============================================================================
# # Inserting MULTIPLE fields/data into the table (using cursor) - uncomment the block below to use
# ==============================================================================
batchCustomers = [
    ('Doe', 'John', 'John@doe.com'),
    ('Steph', 'Kuewa', 'steph@kuewa.com'),
    ('Some', 'Guy', 'guy@some.com')
]
myCur.executemany('INSERT INTO customers VALUES(?, ?, ?)', batchCustomers) # Notice the placeholder uses "?"
# ==============================================================================

# To run the SQL command from cursor, use "commit" command. 
# We need to "commit" the database connection
conn.commit()

# Closing the communication
# When done with database query, it is best practice to close the connection.
conn.close()
