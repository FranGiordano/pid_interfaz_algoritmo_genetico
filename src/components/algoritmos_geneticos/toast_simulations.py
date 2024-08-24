import dash_bootstrap_components as dbc
from dash import Input, Output, html


def toast_simulations():

    toast = dbc.Toast(
        "Simulación generada con éxito",
        id="toast_simulations",
        header="Simulación",
        is_open=False,
        dismissable=True,
        icon="success",
        # top: 66 positions the toast below the navbar
        style={"position": "fixed", "bottom": 66, "right": 10, "width": 350},
    )

    return toast
