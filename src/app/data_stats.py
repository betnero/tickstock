import pandas as pd


def stats(csv_file):
    # Load the csv file with data_storage.
    df = pd.read_csv(csv_file)

    # Remove missing values.
    df.dropna(inplace=True)

    print('\n')

    # Basic information about data_storage (metadata).
    print('========================================')
    print('--------------- DATA INFO --------------')
    print('========================================')

    df.info(verbose=True)

    print('\n')

    # Example of how th data_storage is structured in the frame.
    print('========================================')
    print('--------- DATA STRUCTURE - 5 ROWS ------')
    print('========================================')

    print(df.tail())

    print('\n')

    # Statistics.
    print('========================================')
    print('------------ DATA STATISTICS -----------')
    print('========================================')

    with pd.option_context('display.max_columns', 40):
        print(df.describe(include='all'))


#stats('../app/aaplprices.csv')
