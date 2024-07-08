import dash_bootstrap_components as dbc
from dash import html

from components.algoritmos_geneticos.card_cruce import card_cruce
from components.algoritmos_geneticos.tabla_poblacion import tabla_poblacion


def iteracion(poblaciones, cruces, nro_iteracion):

    cruces_iteracion = [cruce for cruce in cruces if cruce['nro_poblacion_padres'] == nro_iteracion]

    cards_cruces = [card_cruce(cruce) for cruce in cruces_iteracion]

    tabs = dbc.Tabs([], className='mx-5')

    tab_poblacion_padre = dbc.Tab([dbc.Card([
        tabla_poblacion(poblaciones[nro_iteracion])
    ], className='mx-5 mt-3')], label='Población de Padres')

    tabs.children.append(tab_poblacion_padre)

    for i, card in enumerate(cards_cruces):
        tabs.children.append(dbc.Tab(card, label=f'Cruce {i+1}'))

    tab_poblacion_hijo = dbc.Tab([dbc.Card([
        tabla_poblacion(poblaciones[nro_iteracion+1])
    ], className='mx-5 mt-3')], label='Población de Hijos')

    tabs.children.append(tab_poblacion_hijo)

    resultado = html.Div([

        tabs

    ], id='resultado-iteracion')

    return resultado
