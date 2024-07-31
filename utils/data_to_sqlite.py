# The script downloads ALL stock data_storage available via yfinance library, for the maximum period available and puts it in
# a sqlite DB.

import yfinance as yf
import sqlite3
import re

with open('tickers_cleaned.txt', 'r') as f:
    for match in re.findall(r"'(.*?)'", f.read()):

        # DB connection
        conn = sqlite3.connect('stock_prices.db')
        c = conn.cursor()

        # Create a table
        c.execute('''CREATE TABLE IF NOT EXISTS stock_prices
                     (date DATE, ticker TEXT, open REAL, high REAL, low REAL, close REAL, adj REAL, volume REAL)''')

        # Download the stock prices for 'match'
        data = yf.download(match, period='max')

        # Get the stock prices from the dataframe
        dates = [date.strftime('%Y-%m-%d') for date in data.index]
        open_prices = data['Open'].tolist()
        high_prices = data['High'].tolist()
        low_prices = data['Low'].tolist()
        close_prices = data['Close'].tolist()
        adj_prices = data['Adj Close'].tolist()
        volume_prices = data['Volume'].tolist()

        # Upload data_storage into the database
        stock_prices = [(date, match, open_price, high_price, low_price, close_price, adj_price, volume_price )
                        for date, open_price, high_price, low_price, close_price, adj_price, volume_price in
                        zip(dates, open_prices, high_prices, low_prices, close_prices, adj_prices, volume_prices)]
        c.executemany('INSERT INTO stock_prices VALUES (?,?,?,?,?,?,?,?)', stock_prices)

        conn.commit()
        conn.close()
# Data categories: Date,Open,High,Low,Close,Adj Close,Volume
