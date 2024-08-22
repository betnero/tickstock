from downloader.data_downloader import StockDownloader
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# Cache location
cache_location = 'cache'
yf.set_tz_cache_location(cache_location)

# Download data for a stock within a specified date range
downloader = StockDownloader("aapl")
x = downloader.data_download(start=None, end=None)
# print(x.head())

downloader.data_to('datadb.sql')


# SQLAlchemy connectable
cnx = create_engine('sqlite:///datadb.sql.db').connect()

# table named 'contacts' will be returned as a dataframe.
df = pd.read_sql_table('datadb.sql', cnx)
print(df)
