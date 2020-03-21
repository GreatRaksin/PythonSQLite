import sqlite3 as db

# Making a DB connection
start = db.connect('DB_Sqlite.sqlite')

# Making requests and getting answers (results)
cursor = start.cursor()

# CODING STARTS HERE
# CODING ENDS HERE

# Closing DB connection
start.close()