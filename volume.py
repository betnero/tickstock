import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def volume(csv_file):
    # Import csv file as a frame.
    csv_file = pd.read_csv(csv_file)

    plt.figure(figsize=(16, 3))

    csv_file.Volume.plot.bar(label='Volume', color='darkgreen', width=0.15, alpha=1)

    # Plot the price line
    plt.grid(color='gray', linestyle='-', alpha=0.6, animated=True)

    # Plot description and legend.
    plt.title('Candlestick')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')

    plt.show()

# volume('aaplprices.csv')
