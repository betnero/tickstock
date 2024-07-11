import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def moving_average(window_size, csv_file):
    data = pd.read_csv(csv_file)
    moving_avg = data['Close'].rolling(window=window_size).mean()
    print(moving_avg)

    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Prices with a moving average")
    moving_avg.plot(label='Moving average {} days'.format(window_size))
    data.Close.plot(label='Close price')
    plt.legend()
    plt.show()


moving_average(1000, 'aaplprices.csv')