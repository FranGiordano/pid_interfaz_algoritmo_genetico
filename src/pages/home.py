import dash
from dash import html, callback, Input, Output, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path="/",
                   title="PID",
                   update_title="PID",
                   name="PID")

layout = dbc.Container([
    html.H1(children='Introducción de la página', style={'textAlign': 'center'}),
], style={'minWidth': '1400px'})
