from dash import html
import dash_bootstrap_components as dbc


def ag_title():
    titulo = html.Div([
        dbc.Row([
            dbc.Col([
                html.Img(src="../assets/images/backpack.png", style={"width": "100%"}),
            ], width=2, style={'display': 'flex', 'justify-content': 'center'} ),

            dbc.Col([
                html.H1('Algoritmos Genéticos'),
                html.H2('El Problema de la Mochila'),
                dbc.Button(
                    "¿Cómo funciona?",
                    id="btn_abrir_modal_video",
                    color="primary",
                ),
                dbc.Tooltip(
                    "¿Qué es el problema de la mochila?",
                    target="btn_abrir_modal_video",
                    placement='right'
                )
            ]),
        ], style={'display': 'flex', 'justify-content': 'center'} )
    ], className='mx-auto')

    return titulo
