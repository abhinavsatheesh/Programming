import sqlite3

# Establish a connection to the SQLite database file
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL commands
create_table_query = '''DROP TABLE my_family;'''
cursor.execute(create_table_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
# Commit the changes and close the connection
conn.commit()
conn.close()
