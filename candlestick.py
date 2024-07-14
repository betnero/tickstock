
def candlestick(csv_file):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    # Import csv file as a frame.
    df = pd.read_csv(csv_file)

    # Define parameters for the candlestick plot.
    T = df.index
    O = df.Open
    H = df.High
    L = df.Low
    C = df.Close

    # Calculate and plot the candlestick pattern.
    plt.figure(figsize=(12, 4))
    color = ["green" if close_price > open_price else "red" for close_price, open_price in zip(C, O)]
    plt.bar(x=T, height=np.abs(O - C), bottom=np.min((O, C), axis=0), width=0.6, color=color)
    plt.bar(x=T, height=H - L, bottom=L, width=0.1, color=color)

    # Calculate and plot SMA for 30, 60, 90 days and day prices.
    window_size_30 = 30
    window_size_60 = 60
    window_size_90 = 90
    sma30 = df['Close'].rolling(window=window_size_30).mean()
    plt.plot(sma30, linewidth=0.6, label='SMA30')

    sma60 = df['Close'].rolling(window=window_size_60).mean()
    plt.plot(sma60, linewidth=0.6, label='SMA60')

    sma90 = df['Close'].rolling(window=window_size_90).mean()
    plt.plot(sma90, linewidth=0.6, label='SMA90')

    plt.plot(df.Close, color='purple', linewidth=0.6, label='Day price')

    # Plot the price line
    plt.grid(color='gray', linestyle='-', alpha=0.6, animated=True)

    # Plot description and legend.
    plt.title('Candlestick {}'.format(csv_file))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')

    plt.show()


# Call the function.
candlestick('aaplprices.csv')
