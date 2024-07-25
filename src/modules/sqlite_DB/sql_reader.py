import sqlite3

conn = sqlite3.connect('stock_prices.db')
c = conn.cursor()

c.execute("SELECT * FROM stock_prices")
rows = c.fetchall()
# rows = c.fetchmany(33)  # Fetch 33 lines
for row in rows:
    print(row)

conn.close()
