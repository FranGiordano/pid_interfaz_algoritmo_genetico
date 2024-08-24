import dash_bootstrap_components as dbc
from dash import dash_table, html, dcc


def alg_gen_input():
    parametros = (
        dbc.Card([
            dbc.CardHeader([
                html.Strong("Parámetros del algoritmo")
            ]),
            dbc.CardBody([
                dbc.Row([

                    # Objetos
                    dbc.Col([

                        html.Span("Configuración de objetos", className='d-block text-center h5 mb-2'),

                        dbc.InputGroup([
                            dbc.InputGroupText("Objeto 1 - Utilidad", style={'width': '45%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'obj1'},
                                        type="number", min=1, max=100, required=True, step=1),
                            dbc.InputGroupText("Peso", style={'width': '20%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'peso1'},
                                        type="number", min=1, max=100, required=True, step=1),
                        ]),

                        dbc.InputGroup([
                            dbc.InputGroupText("Objeto 2 - Utilidad", style={'width': '45%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'obj2'},
                                        type="number", min=1, max=100, required=True, step=1),
                            dbc.InputGroupText("Peso", style={'width': '20%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'peso2'},
                                        type="number", min=1, max=100, required=True, step=1),
                        ], className='mt-2'),

                        dbc.InputGroup([
                            dbc.InputGroupText("Objeto 3 - Utilidad", style={'width': '45%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'obj3'},
                                        type="number", min=1, max=100, required=True, step=1),
                            dbc.InputGroupText("Peso", style={'width': '20%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'peso3'},
                                        type="number", min=1, max=100, required=True, step=1),
                        ], className='mt-2'),

                        dbc.InputGroup([
                            dbc.InputGroupText("Objeto 4 - Utilidad", style={'width': '45%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'obj4'},
                                        type="number", min=1, max=100, required=True, step=1),
                            dbc.InputGroupText("Peso", style={'width': '20%'}),
                            dbc.Input(id={'type': 'form_objetos', 'index': 'peso4'},
                                        type="number", min=1, max=100, required=True, step=1),
                        ], className='mt-2'),

                        # tabla_objetos()
                    ], className='col-4 border-right equal-height-col'),

                    # Individuos
                    dbc.Col([

                        html.Span("Configuración de bits de individuos", className='d-block text-center h5 mb-2'),

                        dbc.InputGroup([
                            dbc.InputGroupText("Individuo 1", style={'width': '35%'}),
                            dbc.Select(id={'type':'form_individuos', 'index':'ind11'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type':'form_individuos', 'index':'ind12'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind13'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind14'}, options=[0, 1], value='0', required=True),
                        ]),

                        dbc.InputGroup([
                            dbc.InputGroupText("Individuo 2", style={'width': '35%'}),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind21'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind22'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind23'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind24'}, options=[0, 1], value='0', required=True),
                        ], className='mt-2'),

                        dbc.InputGroup([
                            dbc.InputGroupText("Individuo 3", style={'width': '35%'}),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind31'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind32'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind33'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind34'}, options=[0, 1], value='0', required=True),
                        ], className='mt-2'),

                        dbc.InputGroup([
                            dbc.InputGroupText("Individuo 4", style={'width': '35%'}),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind41'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind42'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind43'}, options=[0, 1], value='0', required=True),
                            dbc.Select(id={'type': 'form_individuos', 'index': 'ind44'}, options=[0, 1], value='0', required=True),
                        ], className='mt-2'),

                    ], className='col-4 equal-height-col'),

                    # Inputs
                    dbc.Col([

                        html.Span("Configuración de simulación", className='d-block text-center h5 mb-2'),

                        # Peso maximo de la mochila
                        dbc.InputGroup([
                            dbc.InputGroupText("Peso máximo de la mochila", style={'width': '60%'}),
                            dbc.Input(id="in_peso_mochila", placeholder="1 ≤ x ≤ 100",
                                      type="number", min=1, max=100, required=True, step=1),
                        ]),

                        # Probabilidad de cruce
                        dbc.InputGroup([
                            dbc.InputGroupText("Probabilidad de cruce", style={'width': '60%'}),
                            dbc.Input(id="in_probabilidad_cruce", placeholder="0 ≤ x ≤ 1",
                                      type="number", min=0, required=True, max=1, step=0.01),
                        ], className='mt-2'),

                        # Probabilidad de mutacion
                        dbc.InputGroup([
                            dbc.InputGroupText("Probabilidad de mutación", style={'width': '60%'}),
                            dbc.Input(id="in_probabilidad_mutacion", placeholder="0 ≤ x ≤ 1",
                                      type="number", min=0, required=True, max=1, step=0.01),
                        ], className='mt-2'),

                        # Cantidad de Iteraciones
                        dbc.InputGroup([
                            dbc.InputGroupText("Cantidad de iteraciones", style={'width': '60%'}),
                            dbc.Input(id="in_cantidad_iteraciones", placeholder="1 ≤ x ≤ 100",
                                      type="number", min=1, required=True, max=100, step=1),
                        ], className='mt-2'),

                    ], className='col-4')

                ]),

                # Botones
                html.Div([

                    dbc.Button("Generar bits aleatorios",
                               id="btn_alg_gen_bits_random",
                               color="secondary",
                               className='w-35',
                               # disabled=True
                               ),

                    dbc.Button("Limpiar simulador",
                               id="btn_alg_gen_limpiar",
                               color="secondary",
                               className='w-35 mx-2'),

                    dbc.Button("Ejecutar simulador",
                               id="btn_alg_gen_ejecutar",
                               color="primary",
                               className='w-35')

                ], className='mt-2 d-grid d-md-flex justify-content-md-end'),

                dbc.Alert('', id='alert_alg_gen', dismissable=True, color='danger', is_open=False, className='mt-3')
            ])
        ])
    )

    return parametros
