# This is a file for functions representing stock indicators such as RSI, MACD, Bollinger bands and other.
def rsi(csv_file, period):
    # Importing all modules and libraries required.
    from ta.momentum import RSIIndicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe
    csv_file = pd.read_csv('aaplprices.csv')

    # Calculate the RSI
    output = RSIIndicator(close=csv_file.head(period).Close, window=14, fillna=False)
    print(output.rsi())

    # Set the labels for the axis.
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Relative Strength Index")

    # Plot RSI.
    output.rsi().plot(label='RSI')

    # Plot the buy and sell lines.
    plt.axhline(y=70, color='r', linestyle='--', label='Sell')
    plt.axhline(y=30, color='g', linestyle='--', label='Buy')

    # Plot legend location.
    plt.legend(loc='upper right')

    # Invert data on the x-axis.
    # gca - Get Current Axis. Revert xaxis to show data on xaxis from left (the oldest) to right (the newest)
    plt.gca().invert_xaxis()

    # Draw the plot grid.
    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)

    # Plot the final result
    plt.show()


# Calling the function.
rsi('aaplprices.csv', 300)
