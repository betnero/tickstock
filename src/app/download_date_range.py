# The script will download stock prices based on the entered ticker and date range accepted from the use.
# If start and end date are left empty all the available data for the stock will be downloaded.
# All data is placed in one database called local_stock_prices.db.
# Every downloaded ticker gets its own table within that database called by the ticker name. If for
# some reason you need to have several stock tickers in a single table enter the tickers separated with a space
# e.g. appl goog msft
# If the user mixes date formats e.g. 2000-01-01 and repeats the same request with 2000-1-1 the data will download to
# the database with two times introducing redundancy.


import sqlite3
import pandas as pd
import yfinance as yf
from datetime import datetime


def stock_downloader():

    # Print current date.
    print(datetime.today().strftime("\n%Y-%m-%d"))

    # Accept user input and transform it into lowercase letters. Lowercase will be used as part of the db name.
    tick = input("ENTER THE STOCK TICKER: ")
    ticker = str.lower(tick)

    # Accept date range from user.
    start = input("ENTER START DATE (YYYY-MM-DD). IF EMPTY EARLIEST POSSIBLE DATE: ")
    end = input("ENTER END DATE (YYYY-MM-DD). IF EMPTY IF TODAY: ")

    # If use does not enter anything use today's date.
    if not end:
        end = datetime.today().strftime("%Y-%m-%d")
    else:
        pass

    # If use does not enter anything use 1900-01-01 date which will in practice download the data starting from the
    # beginning.
    if not start:
        start = '1900-01-01'
    else:
        pass

    # Error handling.
    try:
        data = yf.download(ticker, start=start, end=end)  # Download data.

        if data.empty:  # If data is empty raise an exception.
            raise Exception("\nPLEASE CHECK IF THE TICKER SYMBOL EXISTS AND THE INTERNET CONNECTION IS WORKING.\n")

        # If data is downloaded print a message and 10 first lines.
        print("\nDATA DOWNLOADED\n")
        print(data.head())

        # Create a database and place data in the table with a ticker name in the db called stock_prices.db.
        conn = sqlite3.connect('local_stock_prices.db')
        data.to_sql(ticker, conn, if_exists="append", index=True)

        # Close connection.
        conn.close()
        print('\nFINISHED DOWNLOADING.')

    # Raise an exception if data is not downloadable.
    except Exception as err:
        print(f"\nERROR!: {err}")


stock_downloader()
