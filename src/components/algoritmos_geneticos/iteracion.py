import dash_bootstrap_components as dbc
from dash import html

from components.algoritmos_geneticos.card_cruce import card_cruce
from components.algoritmos_geneticos.tabla_poblacion import tabla_poblacion


def iteracion(poblaciones, cruces, nro_poblacion):

    cruces_iteracion = [cruce for cruce in cruces if cruce['nro_poblacion_padres'] == nro_poblacion]

    cards_cruces = [card_cruce(cruce) for cruce in cruces_iteracion]

    resultado = html.Div([

        tabla_poblacion(poblaciones[nro_poblacion-1]),

        html.Br(),



    ], id='resultado-iteracion')

    return resultado
