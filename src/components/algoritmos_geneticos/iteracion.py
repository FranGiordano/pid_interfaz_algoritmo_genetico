import dash_bootstrap_components as dbc
from dash import html

from components.algoritmos_geneticos.card_cruce import card_cruce
from components.algoritmos_geneticos.tabla_poblacion import tabla_poblacion


def iteracion(poblaciones, cruces, nro_iteracion):

    cruces_iteracion = [cruce for cruce in cruces if cruce['nro_poblacion_padres'] == nro_iteracion]

    cards_cruces = [card_cruce(cruce) for cruce in cruces_iteracion]

    tabs_cruces = []
    for i, card in enumerate(cards_cruces):
        tabs_cruces.append(dbc.Tab(card, label=f'Cruce {i+1}'))

    resultado = html.Div([

        html.Br(),

        html.Center(html.H4('Población de Padres')),

        tabla_poblacion(poblaciones[nro_iteracion - 1]),

        html.Br(),

        dbc.Tabs(tabs_cruces, className='mx-5'),

        html.Br(),

        html.Center(html.H4('Población de Hijos')),

        tabla_poblacion(poblaciones[nro_iteracion]),

    ], id='resultado-iteracion')

    return resultado
