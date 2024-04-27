import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#external_scripts = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
external_scripts = [{'src': 'https://cdn.tailwindcss.com'}]

app = Dash(__name__,
           title="PID",
           meta_tags=[{"name": "viewport", "content": "width=device-width"}],
           external_scripts=external_scripts,
           # external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
           use_pages=True)

app._favicon = "/assets/icons/favicon.ico"

server = app.server

app.layout = html.Div([
    html.Br(),
    dash.page_container
], className='mx-auto bg-gray-900')

if __name__ == '__main__':
    app.run_server(debug=True)