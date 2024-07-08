import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go


def card_evolucion(evolucion_x, evolucion_y, promedio_y):

    figure = go.Figure()

    evolucion_y = [evolucion_y[i:i+4] for i in range(0, len(evolucion_y), 4)]
    evolucion_y = [max(i) for i in evolucion_y]
    evolucion_x = evolucion_x[::4]
    figure.add_trace(go.Scatter(x=evolucion_x, y=evolucion_y, mode='lines+markers'))
    #figure.add_bar(x=evolucion_x, y=evolucion_y)
    figure.update_layout(xaxis_title='Nro. de Población', yaxis_title='Utilidad', margin=dict(l=20, r=20, t=20, b=20))
    card = dbc.Card([
        dbc.CardHeader(html.Strong("Evolución del Individuo con Mayor Utilidad por Población")),
        dbc.CardBody([
            dcc.Graph(figure=figure)
        ])
    ])

    return card
