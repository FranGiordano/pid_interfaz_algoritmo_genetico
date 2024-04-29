import dash_bootstrap_components as dbc
from dash import html


def card_solucion(ind_solucion):

    individuo = ind_solucion['Individuo']
    bits = ind_solucion['Bits']
    utilidad = ind_solucion['Utilidad']
    peso = ind_solucion['Peso']
    nro_poblacion = ind_solucion['NroPoblacion']

    card = dbc.Card([
        dbc.CardHeader(html.Strong("Solución del Algoritmo")),
        dbc.CardBody([
            html.P([f"El algoritmo propone al ", html.Strong(individuo),
                    f" de la ", html.Strong(f"Población {nro_poblacion}"), " como solución al problema de la mochila."]),
            html.Center(html.Img(src='../assets/images/dna.png', style={'width': '50%'})),
            html.P(f'Este individuo eligió los siguientes objetos: '),
            dbc.Checklist(
                options=[
                    {"label": "Objeto 1", "value": 1},
                    {"label": "Objeto 2", "value": 2},
                    {"label": "Objeto 3", "value": 3},
                    {"label": "Objeto 4", "value": 4},
                ],
                value=[i for i in range(1, 5) if bits[i-1] == 1]
            ),
            html.P(f'Con una utilidad total de {utilidad} y un peso total de {peso}.', className='mt-2')
        ])
    ], className='h-100')

    return card
