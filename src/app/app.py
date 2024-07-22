# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# Incorporate data
df = pd.read_csv('aaplprices.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    dmc.Title('Share price', color="blue", size="h3"),
    # html.Div(children='Data table'),
    html.Hr(),
    dcc.RadioItems(options=['Close', 'Open', 'High', 'Low', 'Volume'], value='Close', inline=True,
                   id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
]


# Callback adding more controls to the plot
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(df, x='Date', y=col_chosen)
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
