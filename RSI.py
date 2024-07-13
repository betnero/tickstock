def rsi(csv_file, period):
    from ta.momentum import RSIIndicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe
    csv_file = pd.read_csv(csv_file).head(period)
    output_rsi = RSIIndicator(close=csv_file.head(period).Close, window=14, fillna=False)
    print(output_rsi.rsi())
    # Plot RSI.
    output_rsi.rsi().plot(label='RSI')

    # Set the labels for the axis.
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Relative Strength Index")

    # Plot the buy and sell lines.
    plt.axhline(y=70, color='r', linestyle='--', label='Sell')
    plt.axhline(y=30, color='g', linestyle='--', label='Buy')

    # Plot legend location.
    plt.legend(loc='upper left')

    # Invert data on the x-axis.
    # gca - Get Current Axis. Revert xaxis to show data on xaxis from left (the oldest) to right (the newest)
    plt.gca().invert_xaxis()

    # Draw the plot with a grid.
    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.show()


# Calling the function.
rsi('aaplprices.csv', 50)
