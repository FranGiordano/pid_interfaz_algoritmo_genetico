import dash_bootstrap_components as dbc
from dash import html


def card_cruce(cruce):

    nro_poblacion_padres = cruce['nro_poblacion_padres']
    nro_cruce = cruce['nro_cruce']
    probabilidad_cruce = cruce['probabilidad_cruce']
    probabilidad_mutacion = cruce['probabilidad_mutacion']
    prob_cruce = cruce['prob_cruce']
    punto_corte = cruce['punto_corte']
    cruzo = cruce['cruzo']
    prob_ind_1 = cruce['prob_ind_1']
    prob_ind_2 = cruce['prob_ind_2']
    bits_individuo_padre1 = cruce['bits_individuo_padre1']
    bits_individuo_padre2 = cruce['bits_individuo_padre2']
    nro_ind_padre1 = cruce['nro_ind_padre1']
    nro_ind_padre2 = cruce['nro_ind_padre2']
    punto_corte = cruce['punto_corte']
    bits_padre_1_izq = cruce['bits_padre_1_izq']
    bits_padre_1_der = cruce['bits_padre_1_der']
    bits_padre_2_izq = cruce['bits_padre_2_izq']
    bits_padre_2_der = cruce['bits_padre_2_der']
    probabilidad_mutaciones_1 = cruce['probabilidad_mutaciones_1']
    probabilidad_mutaciones_2 = cruce['probabilidad_mutaciones_2']
    bits_individuo_hijo1 = cruce['bits_individuo_hijo1']
    bits_individuo_hijo2 = cruce['bits_individuo_hijo2']
    peso_hijo1 = cruce['peso_hijo1']
    peso_hijo2 = cruce['peso_hijo2']
    hijo1_aceptado = cruce['hijo1_aceptado']
    hijo2_aceptado = cruce['hijo2_aceptado']
    nro_hijo1 = cruce['nro_hijo1']
    nro_hijo2 = cruce['nro_hijo2']

    div_hijo1 = []
    div_hijo2 = []
    if cruzo:

        input_group_cruce1 = [
            dbc.InputGroupText("Bits Cruce 1")
        ]
        if bits_padre_1_izq is not None:
            for i in bits_padre_1_izq:
                input_group_cruce1.append(dbc.Input(readonly=True, value=i, className='p-2'))
            for i in bits_padre_2_der:
                input_group_cruce1.append(dbc.Input(readonly=True, value=i, className='p-2'))

        input_group_cruce2 = [
            dbc.InputGroupText("Bits Cruce 2")
        ]
        for i in bits_padre_2_izq:
            input_group_cruce2.append(dbc.Input(readonly=True, value=i, className='p-2'))
        for i in bits_padre_1_der:
            input_group_cruce2.append(dbc.Input(readonly=True, value=i, className='p-2'))

        div_hijo1 = [

            dbc.InputGroup([
                dbc.InputGroupText("Punto de Corte"),
                dbc.Input(readonly=True, value=round(punto_corte, 2), className='p-2 text-primary')
            ], className="p-2"),

            dbc.InputGroup(input_group_cruce1, className="p-2"),

            dbc.InputGroup([
            ], className="mr-auto p-2")

        ]

        div_hijo2 = [

            dbc.InputGroup([
                dbc.InputGroupText("Entre gen"),
                dbc.Input(readonly=True, value=(1 if punto_corte < 0.33 else 2 if punto_corte < 0.66 else 3), className='p-2'),
                dbc.InputGroupText("y gen"),
                dbc.Input(readonly=True, value=(2 if punto_corte < 0.33 else 3 if punto_corte < 0.66 else 4), className='p-2'),
            ], className="p-2"),

            dbc.InputGroup(input_group_cruce2, className="p-2"),

            dbc.InputGroup([
            ], className="mr-auto p-2")

        ]

    card = dbc.Card(dbc.CardBody([

        html.Br(),

        html.Center(html.H4('Elección de Padres')),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText("Probabilidad padre 1"),
                dbc.Input(readonly=True, value=round(prob_ind_1, 2), className='p-2 text-primary')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("Individuo elegido"),
                dbc.Input(readonly=True, value=nro_ind_padre1, className='p-2')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("Bits"),
                dbc.Input(readonly=True, value=bits_individuo_padre1[0], className='p-2'),
                dbc.Input(readonly=True, value=bits_individuo_padre1[1], className='p-2'),
                dbc.Input(readonly=True, value=bits_individuo_padre1[2], className='p-2'),
                dbc.Input(readonly=True, value=bits_individuo_padre1[3], className='p-2')
            ], className="mr-auto p-2"),

        ], className='d-flex'),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText("Probabilidad padre 2"),
                dbc.Input(readonly=True, value=round(prob_ind_2, 2), className='p-2 text-primary')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("Individuo elegido"),
                dbc.Input(readonly=True, value=nro_ind_padre2, className='p-2')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("Bits"),
                dbc.Input(readonly=True, value=bits_individuo_padre2[0], className='p-2'),
                dbc.Input(readonly=True, value=bits_individuo_padre2[1], className='p-2'),
                dbc.Input(readonly=True, value=bits_individuo_padre2[2], className='p-2'),
                dbc.Input(readonly=True, value=bits_individuo_padre2[3], className='p-2')
            ], className="mr-auto p-2"),

        ], className='d-flex'),

        html.Br(),

        html.Center(html.H4('Cruzamiento')),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText("Probabilidad de Cruce"),
                dbc.Input(readonly=True, value=round(prob_cruce, 2), className='p-2 text-primary'),
                dbc.InputGroupText('<'),
                dbc.Input(readonly=True, value=round(probabilidad_cruce, 2), className='p-2')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("¿Cruzan?"),
                dbc.Input(readonly=True, value=('SI' if cruzo else 'NO'), className='p-2')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
            ], className="mr-auto p-2")

        ], className='d-flex'),

        html.Div(div_hijo1, className='d-flex', hidden=(not cruzo)),

        html.Div(div_hijo2, className='d-flex', hidden=(not cruzo)),

        html.Br(),
        html.Center(html.H4('Mutación')),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText("Prob Mutación Hijo 1"),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_1[0], 2),
                          className='p-2 text-primary'),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_1[1], 2),
                          className='p-2 text-primary'),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_1[2], 2),
                          className='p-2 text-primary'),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_1[3], 2),
                          className='p-2 text-primary'),
                dbc.InputGroupText('<'),
                dbc.Input(readonly=True, value=round(probabilidad_mutacion, 2), className='p-2')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("Bits Hijo 1"),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[0],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_1[0] < probabilidad_mutacion else ""}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[1],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_1[1] < probabilidad_mutacion else ""}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[2],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_1[2] < probabilidad_mutacion else ""}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[3],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_1[3] < probabilidad_mutacion else ""}'),
                dbc.InputGroupText('Peso'),
                dbc.Input(readonly=True, value=peso_hijo1, className=f'p-2 {"text-success" if hijo1_aceptado else "text-danger"}')
            ], className="mr-auto p-2"),

        ], className='d-flex'),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText("Prob Mutación Hijo 2"),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_2[0], 2),
                          className='p-2 text-primary'),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_2[1], 2),
                          className='p-2 text-primary'),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_2[2], 2),
                          className='p-2 text-primary'),
                dbc.Input(readonly=True, value=round(probabilidad_mutaciones_2[3], 2),
                          className='p-2 text-primary'),
                dbc.InputGroupText('<'),
                dbc.Input(readonly=True, value=round(probabilidad_mutacion, 2),
                          className='p-2')
            ], className="mr-auto p-2"),

            dbc.InputGroup([
                dbc.InputGroupText("Bits Hijo 2"),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[0],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_2[0] < probabilidad_mutacion else ""}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[1],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_2[1] < probabilidad_mutacion else ""}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[2],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_2[2] < probabilidad_mutacion else ""}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[3],
                          className=f'p-2 {'text-danger' if probabilidad_mutaciones_2[3] < probabilidad_mutacion else ""}'),
                dbc.InputGroupText('Peso'),
                dbc.Input(readonly=True, value=peso_hijo2,
                          className=f'p-2 {"text-success" if hijo2_aceptado else "text-danger"}')
            ], className="mr-auto p-2"),

        ], className='d-flex'),

        html.Br(),
        html.Center(html.H4('Hijos Resultantes')),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText('Hijo'),
                dbc.Input(readonly=True, value=f"{'-' if nro_hijo1 is None else nro_hijo1}",
                          className=f'p-2 {"text-danger" if not hijo1_aceptado else "text-success"}'),
            ], className="p-2"),

            dbc.InputGroup([
                dbc.InputGroupText('Estado'),
                dbc.Input(readonly=True, value=f"{'Aceptado' if hijo1_aceptado else 'Rechazado'}",
                          className=f'p-2 {"text-danger" if not hijo1_aceptado else "text-success"}'),
            ], className="p-2"),

            dbc.InputGroup([
                dbc.InputGroupText('Bits'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[0],
                          className=f'p-2 {"text-danger" if not hijo1_aceptado else "text-success"}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[1],
                          className=f'p-2 {"text-danger" if not hijo1_aceptado else "text-success"}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[2],
                          className=f'p-2 {"text-danger" if not hijo1_aceptado else "text-success"}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo1[3],
                          className=f'p-2 {"text-danger" if not hijo1_aceptado else "text-success"}')
            ], className="p-2")

        ], className='d-flex'),

        html.Div([

            dbc.InputGroup([
                dbc.InputGroupText('Hijo'),
                dbc.Input(readonly=True, value=f"{'-' if nro_hijo2 is None else nro_hijo2}",
                          className=f'p-2 {"text-danger" if not hijo2_aceptado else "text-success"}'),
            ], className="p-2"),

            dbc.InputGroup([
                dbc.InputGroupText('Estado'),
                dbc.Input(readonly=True, value=f"{'Aceptado' if hijo2_aceptado else 'Rechazado'}",
                          className=f'p-2 {"text-danger" if not hijo2_aceptado else "text-success"}'),
            ], className="p-2"),

            dbc.InputGroup([
                dbc.InputGroupText('Bits'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[0],
                          className=f'p-2 {"text-danger" if not hijo2_aceptado else "text-success"}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[1],
                          className=f'p-2 {"text-danger" if not hijo2_aceptado else "text-success"}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[2],
                          className=f'p-2 {"text-danger" if not hijo2_aceptado else "text-success"}'),
                dbc.Input(readonly=True, value=bits_individuo_hijo2[3],
                          className=f'p-2 {"text-danger" if not hijo2_aceptado else "text-success"}')
            ], className="p-2")

        ], className='d-flex'),

    ]), className='mx-5 mt-3')

    return card
