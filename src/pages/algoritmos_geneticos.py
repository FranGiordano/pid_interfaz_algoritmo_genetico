import dash
from dash import html, callback, Input, Output, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_player
from src.components.algoritmos_geneticos.alg_gen_input import alg_gen_input
from src.components.algoritmos_geneticos.ag_title import ag_title
from src.components.algoritmos_geneticos.modal_video import modal_video

dash.register_page(__name__,
                   path="/algoritmosgeneticos/",
                   title="Algoritmos Genéticos",
                   update_title="Algoritmos Genéticos",
                   name="Algoritmos Genéticos")

layout = dbc.Container([
    html.Center(html.H1('Algoritmos Genéticos')),
    html.Center(html.Img(src="../assets/images/backpack.png", style={"width": "25%"})),
    ag_title(),
    modal_video(),
    html.Hr(),
    alg_gen_input()
])


@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_abrir_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return True


@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_cerrar_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return False
