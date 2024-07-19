# STATUS: IN DEVELOPMENT

# tickstock
Stock analysis.

# FEATURES:
1. Data download
    - Take user input about requested stock tickers [FEATURE ADDED]
    - Download data for all requested stock tickers for the requested time interval [FEATURE ADDED]
    - Load the data into a csv file [FEATURE ADDED]
    - Place the csv in a specific directory

2. Data analysis:
    - Provide descriptive statistics in a csv or xlsx file [FEATURE ADDED]
    - Calculate the moving average for of requested requested of 5, 10, 15, 30, 60, 90 or custom days. Place it in a file in a specific directory
    - Calculate bollinger band [FEATURE ADDED]
    - Transform the csv data into an xlsx or any other format data at user request
    - Allow user to change data
    - Provide a list of all stock tickers at user request [FEATURE ADDED]

3. Plotting
    - Plot stock prices for the chosen by the user stock with the price at trading day 'Close' or 'Open' 
    - Plot user chosen parameters: Date,Open,High,Low,Close,Adj Close,Volume
    - plot a bollinger band with moving average lines of 60 and 90 days
    - Allow the user to compare two plots of chosen stocks and parameters on one plot. Include basic descriptive statistics.

4. Plotting stock indicators:
   - Bollinger Bands [FEATURE ADDED]
   - Candlesatick pot [FEATURE ADDED]
   - MASD [FEATURE ADDED]
   - MA [FEATURE ADDED]
   - RSI [FEATURE ADDED]
   - Volume [FEATURE ADDED]

5. Allow all the features to be accessible for any data loaded externally (e.g. from an xlsx/csv file)

6. GUI
    - Develop a GUI for each of the features - ideas: TKinter, Grafna, Django.

APPLICATION STRUCTURE:
1. Develop the app in a modular way
2. Develop to make it an installable package (optional)
3. ...
