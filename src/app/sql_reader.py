# The script reads first 33 lines of the database

import sqlite3

conn = sqlite3.connect('../data_storage/stock_prices.db')
c = conn.cursor()

c.execute("SELECT * FROM stock_prices")
# rows = c.fetchall()  # Read all lines of the database
rows = c.fetchmany(33)  # Fetch 33 lines
for row in rows:
    print(row)

conn.close()
