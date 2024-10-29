import dash_bootstrap_components as dbc
import dash_player
from dash import html


def modal_manual_ag():

    modal = dbc.Modal([
        dbc.ModalHeader(html.Strong("Manual de usuario")),

        # leer pdf

        dbc.ModalBody([

            html.Iframe(src='/algoritmosgeneticos/assets/docs/manual.pdf', style={'width': '100%', 'height': '600px'})

        ]),

        dbc.ModalFooter(
            dbc.Button("Cerrar", id="btn_cerrar_modal_manual", className="ml-auto")
        )
    ], id="modal_manual_ag", size="xl")

    return modal

