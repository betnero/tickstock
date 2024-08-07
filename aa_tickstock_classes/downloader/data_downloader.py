import yfinance as yf
import sqlite3


class StockDownloader:

    def __init__(self, stock_ticker):
        self.stock_ticker = stock_ticker
        self.data = None

    def data_download(self, start, end):
        self.data = yf.download(self.stock_ticker, start, end)
        return self.data

    def data_to(self, file_name):

        # Split the file name to determine file format
        spl = file_name.split('.')[-1]

        # Choice of file formats
        if spl == 'csv':
            self.data.to_csv(file_name)
        elif spl == 'xlsx':
            self.data.to_excel(file_name)
        elif spl == 'json':
            self.data.to_json(file_name)
        elif spl == 'sql':
            conn = sqlite3.connect(file_name + '.db')
            self.data.to_sql(file_name, conn, if_exists="replace")
        elif spl == 'html':
            self.data.to_html(file_name)
        elif spl == 'md':
            self.data.to_markdown(file_name)
        else:
            self.data.to_html(file_name)


'''
TODO: 
pandas.DataFrame.to_orc
pandas.DataFrame.to_parquet
pandas.DataFrame.to_pickle
pandas.DataFrame.to_hdf
pandas.DataFrame.to_dict
pandas.DataFrame.to_feather
pandas.DataFrame.to_latex
pandas.DataFrame.to_stata
pandas.DataFrame.to_gbq
pandas.DataFrame.to_records
pandas.DataFrame.to_string
pandas.DataFrame.to_clipboard 
'''
