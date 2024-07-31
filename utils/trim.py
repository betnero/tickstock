# This script takes a full list of stock tickers (with their names) and transforms it into a single line with only
# tickers ready for use to download data_storage.

import csv

with open('../docs/company_names_with_tickers', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:

        if row:  # skip empty lines

            print(row[0].split(None)[0], end='\', \'')

# Launch with: python ./trim.py | tee output.txt
