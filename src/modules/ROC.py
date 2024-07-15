def roc(csv_file, period):
    from ta.momentum import ROCIndicator
    import pandas as pd
    import matplotlib.pyplot as plt

    # Import the csv file into a dataframe.
    csv_file = pd.read_csv('../../data/aaplprices.csv').head(period)
    output_roc = ROCIndicator(close=csv_file.Close, window=12, fillna=False)
    print(output_roc.roc())

    # Plot the function and the 0 reference line.
    plt.figure(figsize=(16, 4))
    output_roc.roc().plot(label='ROC', color='navy', linewidth=0.6)
    plt.axhline(y=0, color='r', linestyle='--', linewidth=0.8)

    plt.fill_between(range(len(output_roc.roc())), output_roc.roc(), where=(output_roc.roc() <= 0), color='red',
                     alpha=0.5)
    plt.fill_between(range(len(output_roc.roc())), output_roc.roc(), where=(output_roc.roc() > 0), color='green',
                     alpha=0.5)

    # plt.gca().invert_xaxis()  # Reverting the axis.

    # Plot the grid.
    plt.grid(color='k', linestyle='-', linewidth=0.2, animated=True)
    plt.legend(loc='upper left')

    plt.show()


roc('../../data/aaplprices.csv', 30)
