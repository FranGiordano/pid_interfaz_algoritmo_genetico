import dash
from dash import html, callback, Input, Output, dcc, State
import dash_bootstrap_components as dbc
import random as rd
from src.components.algoritmos_geneticos.alg_gen_input import alg_gen_input
from src.components.algoritmos_geneticos.ag_title import ag_title
from src.components.algoritmos_geneticos.modal_video import modal_video
from utils.alg_gen import AlgGenMochila, ErrorPoblacionConIndividuosMuertos

dash.register_page(__name__,
                   path="/algoritmosgeneticos/",
                   title="Algoritmos Genéticos",
                   update_title="Algoritmos Genéticos",
                   name="Algoritmos Genéticos")

layout = dbc.Container([
    ag_title(),
    modal_video(),
    html.Br(),
    alg_gen_input(),
    html.Div(id="output_alg_gen")
])


# Mostrar modal
@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_abrir_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return True


# Ocultar modal
@callback(
    Output("modal_video", "is_open", allow_duplicate=True),
    Input("btn_cerrar_modal_video", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_modal(n_clicks):
    return False


# Generar bits aleatorios de tal forma que los individuos no superen el peso máximo de la mochila
@callback(
    Output("tabla_individuos", "rowData", allow_duplicate=True),
    Input("btn_alg_gen_bits_random", 'n_clicks'),
    State("tabla_individuos", "rowData"),
    State("tabla_objetos", "rowData"),
    State("in_peso_mochila", "value"),
    prevent_initial_call=True
)
def generar_bits(n_clicks, row_data_individuos, objetos, capacidad_mochila):

    pesos = [objetos[i]['Peso'] for i in range(4)]

    for row in row_data_individuos:
        row['1'], row['2'], row['3'], row['4'] = rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1)
        while sum([row['1']*pesos[0], row['2']*pesos[1], row['3']*pesos[2], row['4']*pesos[3]]) > capacidad_mochila:
            row['1'], row['2'], row['3'], row['4'] = rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1)

    return row_data_individuos


# Deshabilitar boton mientras se ejecuta algoritmo
@callback(
    Output("btn_alg_gen_ejecutar", "children", allow_duplicate=True),
    Output("btn_alg_gen_ejecutar", "disabled", allow_duplicate=True),
    Input("btn_alg_gen_ejecutar", "n_clicks"),
    prevent_initial_call=True
)
def cargar_boton(n_clicks):
    contenido_boton = [dbc.Spinner(size="sm"), " Ejecutando..."]
    return contenido_boton, True


# Ejecutar algoritmo y devolver resultados
@callback(
    Output("output_alg_gen", "children"),
    Output("btn_alg_gen_ejecutar", "children"),
    Output("btn_alg_gen_ejecutar", "disabled"),
    Output('alert_alg_gen', 'is_open'),
    Output('alert_alg_gen', 'children'),
    Input("btn_alg_gen_ejecutar", "n_clicks"),
    State("tabla_individuos", "rowData"),
    State("in_probabilidad_cruce", "value"),
    State("in_probabilidad_mutacion", "value"),
    State("in_cantidad_iteraciones", "value"),
    State("in_semilla", "value"),
    State('tabla_objetos', 'rowData'),
    State('in_peso_mochila', 'value'),
    prevent_initial_call=True
)
def ejecutar_algoritmo(n_clicks, individuos, prob_cruce, prob_mutacion, cant_iteraciones, semilla, objetos, peso_mochila):

    if None in (prob_cruce, prob_mutacion, cant_iteraciones, semilla, peso_mochila):
        error = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'Por favor revise que ningún parámetro esté vacío o incompleto.')
        return {}, "Ejecutar algoritmo", False, True, error

    if prob_cruce < 0 or prob_cruce > 1 or prob_mutacion < 0 or prob_mutacion > 1:
        error = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'Las probabilidades de cruce y mutación deben estar entre 0 y 1.')
        return {}, "Ejecutar algoritmo", False, True, error

    if cant_iteraciones < 1 or cant_iteraciones > 15:
        error = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'La cantidad de iteraciones debe estar entre 1 y 15.')
        return {}, "Ejecutar algoritmo", False, True, error

    if semilla < -1000 or semilla > 1000:
        error = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'La semilla de aleatoriedad debe estar entre -1000 y 1000.')
        return {}, "Ejecutar algoritmo", False, True, error

    if peso_mochila < 1 or peso_mochila > 100:
        error = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'El peso máximo de la mochila debe estar entre 1 y 100.')
        return {}, "Ejecutar algoritmo", False, True, error

    utilidades, pesos, matriz_individuos = [], [], []

    for i in range(4):
        utilidades.append(objetos[i]['Utilidad'])
        pesos.append(objetos[i]['Peso'])
        matriz_individuos.append([individuos[i]['1'], individuos[i]['2'], individuos[i]['3'], individuos[i]['4']])

    try:
        ag = AlgGenMochila(utilidades, pesos, peso_mochila, prob_cruce, prob_mutacion, matriz_individuos, semilla)
    except ZeroDivisionError:
        error = ('Ocurrió un error al intentar ejecutar el algoritmo. '
                 'Al menos un individuo debe tener un bit distinto de 0.')
        return {}, "Ejecutar algoritmo", False, True, error
    except ErrorPoblacionConIndividuosMuertos:
        error = ''
        for i in range(4):
            if sum([individuos[i]['1']*pesos[0], individuos[i]['2']*pesos[1], individuos[i]['3']*pesos[2], individuos[i]['4']*pesos[3]]) > peso_mochila:
                error = (f'Ocurrió un error al intentar ejecutar el algoritmo. '
                         f'El individuo {i+1} no debe superar el peso máximo de la mochila.')
                return {}, "Ejecutar algoritmo", False, True, error
        return {}, "Ejecutar algoritmo", False, True, error
    except Exception as e:
        error = f'Ocurrió un error al intentar ejecutar el algoritmo. {e}'
        return {}, "Ejecutar algoritmo", False, True, error

    ag.run(cant_iteraciones)
    data = ag.get_data()

    return 'Procesado', "Ejecutar algoritmo", False, False, ''
