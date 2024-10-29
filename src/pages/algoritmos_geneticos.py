import dash
from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
from dash.dependencies import ALL
import random as rd

from components.algoritmos_geneticos.iteracion import iteracion
from components.algoritmos_geneticos.solucion import solucion
from components.algoritmos_geneticos.ag_inputs import alg_gen_input
from components.algoritmos_geneticos.ag_title import ag_title
from components.algoritmos_geneticos.modal_video import modal_video
from components.algoritmos_geneticos.modal_manual_ag import modal_manual_ag
from components.algoritmos_geneticos.toast_simulations import toast_simulations
from utils.alg_gen import AlgGenMochila, ErrorPoblacionConIndividuosRechazados

dash.register_page(__name__,
                   path="/simulador/",
                   title="Algoritmos Genéticos",
                   update_title="Algoritmos Genéticos",
                   name="Algoritmos Genéticos")

layout = dbc.Container([
    ag_title(),
    modal_video(),
    modal_manual_ag(),
    html.Br(),
    alg_gen_input(),
    html.Div(id="output_alg_gen"),
    dcc.Store(id='data_store'),
    toast_simulations(),
], style={'minWidth': '1200px', 'maxWidth': '1200px'})


# Mostrar modal video
@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_abrir_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return True


# Ocultar modal video
@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_cerrar_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def ocultar_modal(n_clicks):
    return False

# Mostrar modal manual
@callback(
    Output("modal_manual_ag", "is_open", allow_duplicate=True),
    Input("btn_abrir_modal_manual", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal_manual(n_clicks):
    return True


# Ocultar modal manual
@callback(
    Output("modal_manual_ag", "is_open", allow_duplicate=True),
    Input("btn_cerrar_modal_manual", "n_clicks"),
    prevent_initial_call=True
)
def ocultar_modal_manual(n_clicks):
    return False


# Generar bits aleatorios de tal forma que los individuos no superen el peso máximo de la mochila
@callback(
    Output({'type': 'form_individuos', 'index': ALL}, 'value'),
    Output('toast_simulations', 'children', allow_duplicate=True),
    Output('toast_simulations', 'is_open', allow_duplicate=True),
    Output('toast_simulations', 'icon', allow_duplicate=True),
    Input("btn_alg_gen_bits_random", 'n_clicks'),
    State({'type': 'form_objetos', 'index': ALL}, 'value'),
    State("in_peso_mochila", "value"),
    prevent_initial_call=True
)
def generar_bits(n_clicks, objetos, capacidad_mochila):

    try:

        while True:

            bits_individuos = [str(rd.choice([0, 1])) for _ in range(16)]

            bandera_peso = False

            for i in range(4):
                if sum([int(bits_individuos[0+4*i])*int(objetos[1]),
                        int(bits_individuos[1+4*i])*int(objetos[3]),
                        int(bits_individuos[2+4*i])*int(objetos[5]),
                        int(bits_individuos[3+4*i])*int(objetos[7])]) > capacidad_mochila:
                    bandera_peso = True

            if not bandera_peso:
                return bits_individuos, False, ''

    except Exception as e:

        mensaje = f'Debe ingresar los objetos y el peso máximo de la mochila para generar los bits.'
        icon = 'warning'

        return ['0' for _ in range(16)], mensaje, True, icon


# Limpiar datos
@callback(
    Output({'type': 'form_individuos', 'index': ALL}, 'value', allow_duplicate=True),
    Output({'type': 'form_objetos', 'index': ALL}, 'value', allow_duplicate=True),
    Output("in_probabilidad_cruce", "value", allow_duplicate=True),
    Output("in_probabilidad_mutacion", "value", allow_duplicate=True),
    Output("in_cantidad_iteraciones", "value", allow_duplicate=True),
    Output("in_peso_mochila", "value", allow_duplicate=True),
    Output('data_store', 'data', allow_duplicate=True),
    Output('output_alg_gen', 'children', allow_duplicate=True),
    Input("btn_alg_gen_limpiar", 'n_clicks'),
    prevent_initial_call=True
)
def limpiar_datos(n_clicks):
    data_objetos = [0 for _ in range(8)]
    data_individuos = ['0' for _ in range(16)]
    return data_individuos, data_objetos, None, None, None, None, {}, {}


# Añadir PopUp
# Deshabilitar boton mientras se ejecuta algoritmo
# @callback(
#     Output("btn_alg_gen_ejecutar", "children", allow_duplicate=True),
#     Output("btn_alg_gen_ejecutar", "disabled", allow_duplicate=True),
#     Input("btn_alg_gen_ejecutar", "n_clicks"),
#     prevent_initial_call=True
# )
# def cargar_boton(n_clicks):
#     contenido_boton = [dbc.Spinner(size="sm"), " Ejecutando..."]
#     return contenido_boton, True


# Ejecutar algoritmo y devolver resultados
@callback(
    Output("output_alg_gen", "children"),
    Output('data_store', 'data'),
    Output('toast_simulations', 'children', allow_duplicate=True),
    Output('toast_simulations', 'is_open', allow_duplicate=True),
    Output('toast_simulations', 'icon', allow_duplicate=True),
    Input("btn_alg_gen_ejecutar", "n_clicks"),
    State({'type': 'form_individuos', 'index': ALL}, 'value'),
    State("in_probabilidad_cruce", "value"),
    State("in_probabilidad_mutacion", "value"),
    State("in_cantidad_iteraciones", "value"),
    State({'type': 'form_objetos', 'index': ALL}, 'value'),
    State('in_peso_mochila', 'value'),
    prevent_initial_call=True,
    running=[
        (Output('btn_alg_gen_ejecutar', 'disabled'), True, False),
        (Output('btn_alg_gen_ejecutar', 'children'), ' Ejecutando...', ' Ejecutar simulador'),
    ]
)
def ejecutar_algoritmo(n_clicks, individuos, prob_cruce, prob_mutacion, cant_iteraciones, objetos, peso_mochila):

    resultado = {}
    data = {}
    mensaje = 'Simulación finalizada'
    icon = 'success'

    individuos = [int(i) for i in individuos]
    try:
        objetos = [{'Utilidad': int(objetos[i]), 'Peso': int(objetos[i+1])} for i in [0, 2, 4, 6]]

        if None in (prob_cruce, prob_mutacion) or prob_cruce < 0 or prob_cruce > 1 or prob_mutacion < 0 or prob_mutacion > 1:
            raise ValueError('Ocurrió un error al intentar ejecutar el algoritmo. '
                     'Las probabilidades de cruce y mutación deben estar entre 0 y 1.')

        if cant_iteraciones is None or cant_iteraciones < 1 or cant_iteraciones > 100:
            raise ValueError('Ocurrió un error al intentar ejecutar el algoritmo. '
                     'La cantidad de iteraciones debe estar entre 1 y 100.')

        if peso_mochila is None or peso_mochila < 1 or peso_mochila > 100:
            raise ValueError('Ocurrió un error al intentar ejecutar el algoritmo. '
                     'El peso máximo de la mochila debe estar entre 1 y 100.')

        for i in range(4):
            if 0 in (objetos[i]['Utilidad'], objetos[i]['Peso']):
                raise ValueError('Ocurrió un error al intentar ejecutar el algoritmo. '
                         'Los objetos deben tener valores de utilidad y peso mayores a 0.')

        utilidades, pesos, matriz_individuos = [], [], []

        for i in range(4):
            utilidades.append(objetos[i]['Utilidad'])
            pesos.append(objetos[i]['Peso'])
            matriz_individuos.append([individuos[0+4*i], individuos[1+4*i], individuos[2+4*i], individuos[3+4*i]])

        if pesos[0] > peso_mochila and pesos[1] > peso_mochila and pesos[2] > peso_mochila and pesos[3] > peso_mochila:
            raise ValueError('Ocurrió un error al intentar ejecutar el algoritmo. '
                             'Al menos uno de los objetos debe tener un peso menor al peso máximo de la mochila.')

        ag = AlgGenMochila(utilidades, pesos, peso_mochila, prob_cruce, prob_mutacion, matriz_individuos)
        ag.run(cant_iteraciones)
        data = ag.get_data()

        resultado = solucion(data)

    except ErrorPoblacionConIndividuosRechazados:
        for i in range(4):
            if sum([individuos[0+4*i]*pesos[0], individuos[1+4*i]*pesos[1], individuos[2+4*i]*pesos[2], individuos[3+4*i]*pesos[3]]) > peso_mochila:
                mensaje = (f'Ocurrió un error al intentar ejecutar el algoritmo. '
                         f'El individuo {i+1} no debe superar el peso máximo de la mochila.')
                icon = 'danger'
                break

    except TypeError:
        mensaje = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'Los objetos deben tener valores numéricos de utilidad y peso mayores a 0 y menores a 100.')
        icon = 'danger'

    except ValueError as e:
        mensaje = str(e)
        icon = 'danger'

    except Exception as e:
        mensaje = f'Ocurrió un error al intentar ejecutar el algoritmo: {e}'
        icon = 'danger'

    finally:
        return resultado, data, mensaje, True, icon


# Paginar iteraciones
@callback(
    Output('resultado_iteracion', 'children'),
    Input('paginacion_iteraciones', 'active_page'),
    State('data_store', 'data'),
    prevent_initial_call=True
)
def paginar_iteraciones(pagina, data):

    if not data:
        return {}

    utilidades = [data['Objetos'][i]['Utilidad'] for i in range(4)]
    pesos = [data['Objetos'][i]['Peso'] for i in range(4)]
    mochila = data['Mochila']['Capacidad']

    return iteracion(data['Poblaciones'], data['Cruces'], pagina-1, utilidades, pesos, mochila)

