import yfinance as yf
import sqlite3

# DB connection
conn = sqlite3.connect('stock_prices.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS stock_prices
             (date DATE, ticker TEXT, open REAL, high REAL, low REAL, close REAL)''')

# Download the stock prices for AAPL
data = yf.download('AAPL', period='max')

# Get the stock prices from the dataframe
dates = [date.strftime('%Y-%m-%d') for date in data.index]
open_prices = data['Open'].tolist()
high_prices = data['High'].tolist()
low_prices = data['Low'].tolist()
close_prices = data['Close'].tolist()

# Upload data into the database
stock_prices = [(date, 'AAPL', open_price, high_price, low_price, close_price)
                for date, open_price, high_price, low_price, close_price in
                zip(dates, open_prices, high_prices, low_prices, close_prices)]
c.executemany('INSERT INTO stock_prices VALUES (?,?,?,?,?,?)', stock_prices)

conn.commit()
conn.close()
