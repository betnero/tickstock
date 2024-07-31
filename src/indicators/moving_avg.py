import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# Calcualte and plot moving average.
def moving_average(window_size, csv_file):

    # Download data_storage and put it into a frame.
    data = pd.read_csv(csv_file)

    # Caluclate the moving average.
    moving_avg = data['Close'].rolling(window=window_size).mean()
    print(moving_avg)

    # Plot generation.
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Prices with a moving average")
    moving_avg.plot(label='Moving average {} days'.format(window_size))
    data.Close.plot(label='Close price')
    plt.legend()

    plt.show()


# moving_average(1000, '../../data_storage/aaplprices.csv')


# EMA - Exponential Moving Average

def ema(csv_file, period):
    from ta.trend import ema_indicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe.
    csv_file = pd.read_csv(csv_file).head(period)
    output_ema = ema_indicator(close=csv_file.Close, window=12, fillna=False)
    print(output_ema)

    # Plot generation.
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Prices with a moving average")
    output_ema.plot(label='Exponential Moving Average', color='orange', linewidth=0.8)
    csv_file.Close.plot(label='Close price', color='b', linewidth=0.6)

    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.legend(loc='upper left')
    plt.show()


# ema('../../data_storage/aaplprices.csv', 100)


# SMA - Simple Moving Average
def sma(csv_file, period):
    from ta.trend import sma_indicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe.
    csv_file = pd.read_csv(csv_file).head(period)
    output_sma = sma_indicator(close=csv_file.Close, window=12, fillna=False)
    print(output_sma)

    # Plot generation.
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Prices with a moving average")
    output_sma.plot(label='Exponential Moving Average', color='orange', linewidth=0.8)
    csv_file.Close.plot(label='Close price', color='b', linewidth=0.6)

    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.legend(loc='upper left')
    plt.show()


# sma('../../data_storage/aaplprices.csv', 100)


# WMA - Weighted Moving Average
def wma(csv_file, period):
    from ta.trend import wma_indicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe.
    csv_file = pd.read_csv(csv_file).head(period)
    output_wma = wma_indicator(close=csv_file.Close, window=12, fillna=False)
    print(output_wma)

    # Plot generation.
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Prices with a moving average")
    output_wma.plot(label='Weight Moving Average', color='orange', linewidth=0.8)
    csv_file.Close.plot(label='Close price', color='b', linewidth=0.6)

    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.legend(loc='upper left')
    plt.show()


# wma('../../data_storage/aaplprices.csv', 100)


# SMA, WMA and EMA on a single plot. Adjustable number of days for each of the moving averages. Possibility to
# select the input file with stock data_storage and the period for which the plot will be drawn.
def all_ma(csv_file, period, wmaperiod, smaperiod, emaperiod):
    from ta.trend import sma_indicator, ema_indicator, wma_indicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe.
    csv_file = pd.read_csv(csv_file).head(period)

    # Calculate and define output
    output_wma = wma_indicator(close=csv_file.Close, window=wmaperiod, fillna=False)
    output_sma = sma_indicator(close=csv_file.Close, window=smaperiod, fillna=False)
    output_ema = ema_indicator(close=csv_file.Close, window=emaperiod, fillna=False)

    # Plot generation.
    plt.figure(figsize=(16, 8))
    output_wma.plot(label='WMA({})'.format(wmaperiod), color='red', linewidth=0.8)
    output_sma.plot(label='SMA({})'.format(smaperiod), color='orange', linewidth=0.8)
    output_ema.plot(label='EMA({})'.format(emaperiod), color='green', linewidth=0.8)

    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.legend(loc='upper left')
    plt.title("Moving average SMA({}), WMA({}), EMA({})".format(smaperiod, wmaperiod, emaperiod))

    plt.show()


all_ma('../data_storage/aaplprices.csv', 100, 12, 12, 12)
