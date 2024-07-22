# Original source: https://plotly.com/python/candlestick-charts/

import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('aaplprices.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df.Open,
                high=df.High,
                low=df.Low,
                close=df.Close,)])

fig.show()
