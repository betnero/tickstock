# This script takes a full list of stock tickers (with their names) and transforms it into a single line with only
# tickers ready for use as to download data.

import csv

with open('/../docs/stock_tickers', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:

        if row:  # skip empty lines

            print(row[0].split(None)[0], end='\', \'')