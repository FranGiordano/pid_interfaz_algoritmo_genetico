import dash
from dash import html, callback, Input, Output, dcc, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_player
import random as rd
from src.components.algoritmos_geneticos.alg_gen_input import alg_gen_input
from src.components.algoritmos_geneticos.ag_title import ag_title
from src.components.algoritmos_geneticos.modal_video import modal_video

dash.register_page(__name__,
                   path="/algoritmosgeneticos/",
                   title="Algoritmos Genéticos",
                   update_title="Algoritmos Genéticos",
                   name="Algoritmos Genéticos")

layout = dbc.Container([
    ag_title(),
    modal_video(),
    html.Br(),
    alg_gen_input()
])


# Mostrar modal
@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_abrir_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return True


# Ocultar modal
@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_cerrar_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return False


# Generar bits aleatorios
@callback(
    Output("tabla_individuos", "rowData", allow_duplicate=True),
    Input("btn_alg_gen_bits_random", 'n_clicks'),
    State("tabla_individuos", "rowData"),
    prevent_initial_call=True
)
def generar_bits(n_clicks, row_data):

    for row in row_data:
        row['1'] = rd.randint(0, 1)
        row['2'] = rd.randint(0, 1)
        row['3'] = rd.randint(0, 1)
        row['4'] = rd.randint(0, 1)

    return row_data


# Deshabilitar boton ejecutar algoritmo
@callback(
    Output("btn_alg_gen_ejecutar", "children", allow_duplicate=True),
    Output("btn_alg_gen_ejecutar", "disabled", allow_duplicate=True),
    Input("btn_alg_gen_ejecutar", "n_clicks"),
    prevent_initial_call=True
)
def cargar_boton(n_clicks):
    contenido_boton = [dbc.Spinner(size="sm"), " Ejecutando..."]
    return contenido_boton, True


# Ejecutar algoritmo y devolver resultados
"""
@callback(
)
def cargar_boton():
    pass
"""