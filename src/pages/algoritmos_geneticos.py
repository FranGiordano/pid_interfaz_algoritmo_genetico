import dash
from dash import html, callback, Input, Output, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__,
                   path="/algoritmosgeneticos/",
                   title="Algoritmos Genéticos",
                   update_title="Algoritmos Genéticos",
                   name="Algoritmos Genéticos")

layout = dbc.Container([
    html.H2(children='Algoritmos Genéticos: El Problema de la Mochila', style={'textAlign': 'center'}),
    html.Center(dash_player.DashPlayer(
        id="player",
        url="https://www.youtube.com/embed/86DaXndBVI4?si=0L_aEhS9GHdQBDB6",
        controls=True,
        width="80%",
        height="500px",
    )),
    html.Hr(),
    html.H2(children='Simulación', style={'textAlign': 'center'}),
])