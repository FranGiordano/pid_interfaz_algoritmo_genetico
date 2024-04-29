import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go


def card_evolucion(evolucion_x, evolucion_y, promedio_y):

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=evolucion_x, y=evolucion_y, mode='markers', name='Individuos'))
    figure.add_trace(go.Scatter(x=list({x for x in evolucion_x}), y=promedio_y, mode='lines+markers', name='Promedio'))
    figure.update_layout(xaxis_title='Nro. de Población', yaxis_title='Utilidad', margin=dict(l=20, r=20, t=20, b=20),)

    card = dbc.Card([
        dbc.CardHeader(html.Strong("Evolución de la Utilidad de la Población")),
        dbc.CardBody([
            dcc.Graph(figure=figure)
        ])
    ])

    return card
