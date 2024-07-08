from dash import html
import dash_bootstrap_components as dbc


def ag_title():
    titulo = html.Div([
        html.Img(src="../assets/images/backpack.png", style={"width": "15%"}, className='d-inline-block'),

        html.Div([
            html.H1(html.Strong('Algoritmos Genéticos')),
            html.H2('El Problema de la Mochila'),
            dbc.Button([
                html.I(className="bi bi-play"),
                " Video explicativo"
                ],
                id="btn_abrir_modal_video",
                color="danger",
            ),
            dbc.Button([
                html.I(className="bi bi-book"),
                " Manual del simulador"
            ],
                id="btn_abrir_modal_manual",
                color="secondary",
                className='mx-2'
            )
        ], className='mx-2 p-2')
    ], className='d-flex justify-content-center')

    return titulo
