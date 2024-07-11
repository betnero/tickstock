
# Downloads price data for a stock ticker for a defined period of time.
def tick_fixed(period, *args):
    import pandas as pd
    import yfinance as yf
# Download the data for all requested stock tickers and place in a csv file.
    for arg in args:
        a = yf.download(arg, period=period)
        df = pd.DataFrame(a)
        df.to_csv(arg+"prices.csv")
# Inform the user about the stock ticker being added to the file.
    for arg in args:
        print("{} added to file.".format(arg.upper()))


# Function call example: 
# tick_fixed('max', 'msft', 'aapl', 'goog')
# First argument is the period. Periods available in pandas are as follows: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

# Download the data for all requested stock tickers, for a defined period of time and place in a csv file.
def tick_custom(start, end, *args):
    import pandas as pd
    import yfinance as yf

    for arg in args:
        a = yf.download(arg, start=start, end=end)
        df = pd.DataFrame(a)
        df.to_csv(arg+"prices.csv")

    for arg in args:
        print("{} added to file.".format(arg.upper()))

# Function call example: 
# EXAMPLE: tick_fixed('max', 'msft', 'aapl', 'goog')EXAMPLE: tick_custom('2020-01-01', '2020-12-31', 'msft', 'aapl', 'goog')
