from dash import html
import dash_bootstrap_components as dbc


def ag_title():
    titulo = html.Div([
        html.Img(src="../assets/images/backpack.png", style={"width": "15%"}, className='d-inline-block'),

        html.Div([
            html.H1(html.Strong('Algoritmos Genéticos')),
            html.H2('El Problema de la Mochila'),
            dbc.Button(
                "¿Cómo funciona?",
                id="btn_abrir_modal_video",
                color="secondary",
            ),
            dbc.Tooltip(
                "¿Qué es el problema de la mochila?",
                target="btn_abrir_modal_video",
                placement='right'
            )
        ], className='mx-2 p-2')
    ], className='d-flex justify-content-center')

    return titulo
