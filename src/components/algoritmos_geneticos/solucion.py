import dash_bootstrap_components as dbc
from dash import html

from components.algoritmos_geneticos.card_evolucion import card_evolucion
from components.algoritmos_geneticos.iteracion import iteracion
from components.algoritmos_geneticos.card_solucion import card_solucion
from components.algoritmos_geneticos.tabla_poblacion import tabla_poblacion


def solucion(data):

    individuo_solucion = data['Solucion']

    evolucion_x, evolucion_y, promedio_y = [], [], []
    for i in data['Poblaciones']:
        suma = 0
        for j in i['individuos']:
            evolucion_x.append(i['nro_poblacion'])
            evolucion_y.append(j['Z'])
            suma += j['Z']
        promedio_y.append(suma/4)

    poblacion_final = data['Poblaciones'][-1]

    poblaciones = data['Poblaciones']
    cruces = data['Cruces']

    resultado = [

        html.Br(),

        dbc.Row([

            dbc.Col([
                card_solucion(individuo_solucion)
            ], className='col-4'),

            dbc.Col([
                card_evolucion(evolucion_x, evolucion_y, promedio_y)
            ], className='col-8')

        ]),

        html.Br(),

        dbc.Card([
            dbc.CardHeader(html.Strong("Población Final")),
            dbc.CardBody([
                tabla_poblacion(poblacion_final)
            ])
        ]),

        html.Br(),

        dbc.Card([
            dbc.CardHeader(html.Strong("Iteraciones")),
            dbc.CardBody([
                # iteracion(poblaciones, cruces, nro_poblacion)
            ])
        ]),

        html.Br()

    ]

    return resultado
