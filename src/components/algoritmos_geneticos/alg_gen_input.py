import dash_bootstrap_components as dbc
from dash import dash_table, html
from src.components.algoritmos_geneticos.tabla_objetos import tabla_objetos
from src.components.algoritmos_geneticos.tabla_individuos import tabla_individuos


def alg_gen_input():
    input = (
        dbc.Card([
            dbc.CardHeader([
                dbc.Tabs([dbc.Tab(label="Parámetros del algoritmo", tab_id='tab_parametros')]),
            ]),
            dbc.CardBody([
                dbc.Row([

                    # Objetos
                    dbc.Col([
                        tabla_objetos()
                    ], className='col-3 border-right equal-height-col'),

                    # Individuos
                    dbc.Col([
                        tabla_individuos()
                    ], className='col-3 equal-height-col'),

                    # Inputs
                    dbc.Col([

                        # Peso maximo de la mochila y probabilidad de cruce
                        dbc.Row([
                            dbc.Col(
                                dbc.FormFloating([
                                    dbc.Input(id="in_peso_mochila", placeholder="Peso máximo de la Mochila",
                                              type="number", min=1, value=15, max=100, required=True, step=1),
                                    dbc.Label("Peso máximo de la Mochila")
                                ])
                            ),

                            dbc.Col(
                                dbc.FormFloating([
                                    dbc.Input(id="in_probabilidad_cruce", placeholder="Probabilidad de Cruce",
                                              type="number",
                                              min=0, value=0.98, required=True, max=1, step=0.01),
                                    dbc.Label("Probabilidad de Cruce")
                                ])
                            )
                        ]),

                        # Mutacion e iteraciones
                        dbc.Row([
                            dbc.Col(
                                dbc.FormFloating([
                                    dbc.Input(id="in_probabilidad_mutacion", placeholder="Probabilidad de Mutación",
                                              type="number",
                                              min=0, value=0.1, required=True, max=1, step=0.01),
                                    dbc.Label("Probabilidad de Mutación")
                                ], className='mt-2')
                            ),
                            dbc.Col(
                                dbc.FormFloating([
                                    dbc.Input(id="in_cantidad_iteraciones", placeholder="Cantidad de Iteraciones",
                                              type="number",
                                              min=1, value=5, required=True, max=15, step=1),
                                    dbc.Label("Cantidad de Iteraciones")
                                ], className='mt-2')
                            )
                        ]),

                        # Semilla
                        dbc.Row([
                            dbc.Col(
                                dbc.FormFloating([
                                    dbc.Input(id="in_semilla", placeholder="Semilla de Aleatoriedad",
                                              type="number",
                                              min=-1000, value=0, required=True, max=1000, step=1),
                                    dbc.Label("Semilla de Aleatoriedad")
                                ], className='mt-2')
                            ),
                            dbc.Col(
                            )
                        ]),

                        # Botones
                        html.Div([

                            dbc.Button("Generar bits aleatorios",
                                       id="btn_alg_gen_bits_random",
                                       color="primary",
                                       className='mx-3'
                                       ),

                            dbc.Button("Ejecutar algoritmo",
                                       id="btn_alg_gen_ejecutar",
                                       color="primary",
                                       className='')

                        ], className='d-flex justify-content-end mt-5'),

                    ], className='col-6')

                ])
            ])
        ])
    )

    return input
