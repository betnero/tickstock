# Source of the original code:
# https://technical-analysis-library-in-python.readthedocs.io/en/latest/index.html?highlight=bollinger#examples

def bollinger(csv_file, period):
    import pandas as pd
    from ta.volatility import BollingerBands
    import matplotlib.pyplot as plt

    # Import the data from a csv file into a dataframe.
    csv_file = pd.read_csv(csv_file).head(period)

    # Calculate the Bollinger Bands.
    indioutput_bolband = BollingerBands(close=csv_file.Close, window=20, window_dev=2)

    # Print the results.
    print(indioutput_bolband.bollinger_mavg())
    print(indioutput_bolband.bollinger_hband())
    print(indioutput_bolband.bollinger_lband())
    print(indioutput_bolband.bollinger_hband_indicator())
    print(indioutput_bolband.bollinger_lband_indicator())

    # Plot the results.
    plt.figure(figsize=(16, 4))
    indioutput_bolband.bollinger_hband().plot(label='HBAND', color='g', linewidth=0.6)
    indioutput_bolband.bollinger_lband().plot(label='LBAND', color='r', linewidth=0.6)
    indioutput_bolband.bollinger_mavg().plot(label='MA(20)', color='orange', linewidth=0.6)
    csv_file.Close.plot(label='CLOSE PRICE', color='navy', linewidth=0.8)

    # Plot the grid.
    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.legend(loc='upper left')

    plt.show()


bollinger('../app/aaplprices.csv', 500)
