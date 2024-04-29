import dash_bootstrap_components as dbc
from dash import html


def navbar() -> dbc.Navbar:

    barra_navegacion = dbc.Navbar(
        dbc.Container([
            dbc.NavItem(
                dbc.Row(
                    [
                        html.Img(src="/assets/images/utn.png", height="50px")
                    ],
                    align="center",
                    className="g-0",
                )),
            dbc.NavItem(
                dbc.NavLink(html.Strong('Inicio'), href="/"),
                class_name="ms-auto px-3 text-primary"),
            dbc.NavItem(
                dbc.NavLink(html.Strong("Algoritmos Genéticos"), href="/algoritmosgeneticos/"),
                class_name="px-3 text-primary")
        ], style={'minWidth': '1400px'}), className='shadow-sm', style={'minWidth': '1400px'}
    )
    return barra_navegacion
