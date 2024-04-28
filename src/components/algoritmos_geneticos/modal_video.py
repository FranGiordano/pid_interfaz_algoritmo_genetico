import dash_bootstrap_components as dbc
import dash_player
from dash import html


def modal_video():

    modal = dbc.Modal([
        dbc.ModalHeader(html.Strong("¿Qué es el problema de la mochila?")),
        dbc.ModalBody([
            html.Center(dash_player.DashPlayer(
                id='video-presentacion',
                url='https://www.youtube.com/embed/86DaXndBVI4?si=0L_aEhS9GHdQBDB6',
                controls=True,
                playing=False,
                volume=1
            ))
        ]),
        dbc.ModalFooter(
            dbc.Button("Cerrar", id="btn_cerrar_modal_video", className="ml-auto")
        )
    ], id="modal_video", size="xl")

    return modal

