import dash_bootstrap_components as dbc
import dash_ag_grid as dag


def tabla_poblacion(poblacion_final):

    nro_poblacion = poblacion_final['nro_poblacion']
    individuos = poblacion_final['individuos']

    data = [
        individuos[0],
        individuos[1],
        individuos[2],
        individuos[3]
    ]

    columnas = [
        {
            'headerName': f'Población {nro_poblacion}',
            'children': [
                {'field': 'Individuo', 'width': 150, 'headerName': 'Individuos'}
            ]
        },
        {
            'headerName': 'Variables',
            'children': [
                {'field': '1', 'width': 90, 'headerName': 'X1'},
                {'field': '2', 'width': 90, 'headerName': 'X2'},
                {'field': '3', 'width': 90, 'headerName': 'X3'},
                {'field': '4', 'width': 90, 'headerName': 'X4'}
            ]
        },
        {'field': 'Z', 'headerName': 'Utilidad Total del Individuo', 'width': 125},
        {'field': 'Peso', 'headerName': 'Peso Total del Individuo', 'width': 125},
        {'field': 'Prob', 'headerName': 'Probabilidad', 'valueFormatter': {"function":"""d3.format(",.2f")(params.value)"""}, 'width': 125},
        {'field': 'Prob Acum', 'headerName': 'Probabilidad Acumulada', 'valueFormatter': {"function":"""d3.format(",.2f")(params.value)"""}, 'width': 150},
    ]

    tabla = dag.AgGrid(
        columnDefs=columnas,
        rowData=data,
        columnSize="sizeToFit",
        dashGridOptions={"domLayout": "autoHeight"},
        style={"height": None, 'width': '100%', 'margin': 'auto'},
        defaultColDef={"resizable": False,
                       "sortable": False,
                       'suppressMovable': True,
                       "wrapHeaderText": True,
                       "autoHeaderHeight": True,
                       },
    )

    return tabla
