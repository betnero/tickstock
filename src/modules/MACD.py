def macd(csv_file, period):
    from ta.trend import MACD
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe.
    csv_file = pd.read_csv(csv_file).head(period)

    # Defining MACD parameters and printing the result.
    output_macd = MACD(close=csv_file.Close, window_slow=26, window_fast=12, window_sign=9, fillna=False)
    print(output_macd.macd())
    print(csv_file.head(period))

    # Plotting the data.
    plt.figure(figsize=(16, 4)).subplots()
    output_macd.macd_signal().plot(label='Signal', color='r', alpha=0.4)  # MACD Signal == EMA(9)
    output_macd.macd_diff().plot.bar(label='MACDdiff (12,26)', color='g', alpha=0.4)  # EMA(12) - EMA(26)
    output_macd.macd().plot(label='MACD (12,26,9)', color='b', alpha=0.4)  # MACD Signal == EMA(12) -EMA(26)

    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)

    # csv_file.Close.plot()

    plt.title('MACD')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend(loc='upper left')
    #    plt.gca().invert_xaxis()  # Reverting the axis.
    plt.show()


# Calling the function.
macd('../app/aaplprices.csv', 100)
