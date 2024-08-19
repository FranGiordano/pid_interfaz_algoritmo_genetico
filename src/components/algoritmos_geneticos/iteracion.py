import dash_bootstrap_components as dbc
from dash import html, dcc

from components.algoritmos_geneticos.card_cruce import card_cruce
from components.algoritmos_geneticos.tabla_poblacion import tabla_poblacion


def iteracion(poblaciones, cruces, nro_iteracion, utilidades, pesos, mochila):

    cruces_iteracion = [cruce for cruce in cruces if cruce['nro_poblacion_padres'] == nro_iteracion]

    cards_cruces = [card_cruce(cruce) for cruce in cruces_iteracion]

    tabs_cruces = []
    for i, card in enumerate(cards_cruces):
        tabs_cruces.append(dbc.Tab(card, label=f'Cruce {i+1}'))

    resultado = html.Div([

        html.Br(),

        html.Center(dcc.Markdown(f'''
        Función Objetivo:
        $Z = {utilidades[0]}X_1 + {utilidades[1]}X_2 + {utilidades[2]}X_3 + {utilidades[3]}X_4$
        
        Función de Restricción:
        ${pesos[0]}X_1 + {pesos[1]}X_2 + {pesos[2]}X_3 + {pesos[3]}X_4 <= {mochila}$
        
        Función de Probabilidad:
        $P = \\frac{{\\text{{Utilidad del Individuo}}}}{{\\text{{Suma de las Utilidades}}}}$
        
        ''', mathjax=True, className='mx-5')),

        html.Br(),

        html.Center(html.H3('Población de Padres')),

        html.Div([
            tabla_poblacion(poblaciones[nro_iteracion])
            ], className='mx-5'),

        html.Br(),

        html.Center(html.H3('Cruces entre Padres')),

        dbc.Tabs(tabs_cruces, className='mx-5'),

        html.Br(),

        html.Center(html.H3('Población de Hijos')),

        html.Div([
            tabla_poblacion(poblaciones[nro_iteracion + 1]),
        ], className='mx-5'),

    ], id='resultado-iteracion')

    return resultado
