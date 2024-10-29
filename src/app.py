import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from components.general.navbar import navbar

#external_scripts = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
#external_scripts = [{'src': 'https://cdn.tailwindcss.com'}]

app = Dash(__name__,
           title="PID",
           # external_scripts=[{'src': 'https://cdn.tailwindcss.com'}],
            meta_tags=[{"name": "viewport", "content": "width=device-width"}],
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
           use_pages=True,
           requests_pathname_prefix="/algoritmosgeneticos/",
           routes_pathname_prefix="/algoritmosgeneticos/"
            )

app._favicon = "/assets/icons/favicon.ico"

server = app.server

app.layout = html.Div([
    navbar(),
    html.Br(),
    dash.page_container
])

if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=80)
    app.run_server(debug=False, host="0.0.0.0", port=80)
