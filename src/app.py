import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from components.general.navbar import navbar

#external_scripts = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
#external_scripts = [{'src': 'https://cdn.tailwindcss.com'}]

app = Dash(__name__,
           title="PID",
           # external_scripts=[{'src': 'https://cdn.tailwindcss.com'}],
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
           use_pages=True,
           )

app._favicon = "/assets/icons/favicon.ico"

server = app.server

app.layout = html.Div([
    navbar(),
    html.Br(),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)