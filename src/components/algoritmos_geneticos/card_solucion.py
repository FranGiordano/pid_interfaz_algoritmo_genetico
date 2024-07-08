import dash_bootstrap_components as dbc
from dash import html


def card_solucion(ind_solucion):

    individuo = ind_solucion['Individuo']
    bits = ind_solucion['Bits']
    utilidad = ind_solucion['Utilidad']
    peso = ind_solucion['Peso']
    nro_poblacion = ind_solucion['NroPoblacion']

    objetos_elegidos = dbc.Row([])
    for i in range(len(bits)):

        if bits[i] == 1:

            objeto = dbc.Col([

                html.Center([
                    html.Img(src=f'../assets/images/libro{i + 1}.png', style={'max-width': '50%'},
                             className='mx-auto mb-2'),
                    html.P(f"Objeto {i + 1}")
                ])

            ], className='col-2')

            objetos_elegidos.children.append(objeto)

        else:

            objeto = dbc.Col([

                html.Center([
                    html.Img(src=f'../assets/images/libro{i + 1}.png', style={'max-width': '50%', 'opacity': '0.25'},
                             className='mx-auto mb-2'),
                    html.P(f"")
                ])

            ], className='col-2')

            objetos_elegidos.children.append(objeto)

    card = dbc.Card([

        dbc.CardHeader(html.Strong("Mejor individuo del algoritmo")),

        dbc.CardBody([

            dbc.Row([

                dbc.Col([

                    html.Img(src='../assets/images/dna.png', style={'max-width': '100%'}, className='mx-auto mb-2'),

                ], className='col-2', align='center'),

                dbc.Col([

                    html.P([f"El algoritmo propone al ", html.Strong(individuo),
                            f" de la ", html.Strong(f"Población {nro_poblacion}"),
                            " como solución al problema de la mochila."]),

                    html.P(f'Este individuo eligió los siguientes objetos: '),

                    objetos_elegidos,

                    html.P([f'Con una ',
                            html.Strong(f'utilidad total de {utilidad}'),
                            ' y un ',
                            html.Strong(f'peso total de {peso}'),
                            '.'])

                ], className='col-10')

            ]),

        ])
    ])

    return card
