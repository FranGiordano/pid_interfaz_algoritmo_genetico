from dash import html
import dash_bootstrap_components as dbc


def ag_title():
    titulo = dbc.Row([
        dbc.Col(html.H2(children='Simulación del Problema de la Mochila'), width='auto'),
        dbc.Col([dbc.Button(
            id="btn_abrir_modal_video",
            color="primary",
            className='bi bi-question-circle rounded-circle',
            style={'justify-content': 'center', 'align-items': 'center'},
        ),
            dbc.Tooltip(
                "¿Qué es el problema de la mochila?",
                target="btn_abrir_modal_video",
                placement='right'
            )],
            width='auto')
    ], className='justify-content-center align-items-center')

    return titulo
