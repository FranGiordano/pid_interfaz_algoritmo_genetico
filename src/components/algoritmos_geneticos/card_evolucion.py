import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go


def card_evolucion(evolucion_x, evolucion_y, promedio_y):

    figure = go.Figure()
    evolucion_x = evolucion_x[::4]
    figure.add_bar(x=evolucion_x, y=promedio_y)
    figure.update_layout(xaxis_title='Nro. de Población', yaxis_title='Utilidad Promedio', margin=dict(l=20, r=20, t=20, b=20))

    card = dbc.Card([
        dbc.CardHeader(html.Strong("Evolución de la Utilidad Promedio de la Población")),
        dbc.CardBody([
            dcc.Graph(figure=figure)
        ])
    ])

    return card
