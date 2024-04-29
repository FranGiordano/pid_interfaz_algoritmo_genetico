import dash_ag_grid as dag
import pandas as pd


def tabla_objetos():

    data = [
        {'Objeto': 'Objeto 1', 'Utilidad': 4, 'Peso': 7},
        {'Objeto': 'Objeto 2', 'Utilidad': 5, 'Peso': 6},
        {'Objeto': 'Objeto 3', 'Utilidad': 6, 'Peso': 8},
        {'Objeto': 'Objeto 4', 'Utilidad': 3, 'Peso': 2}
    ]

    columnas = [
        {'field': 'Objeto'},
        {
            'headerName': 'Parámetros',
            'headerClass': 'center-aligned-group-header',
            'children': [
                {'field': 'Utilidad',
                 'type': 'numericColumn',
                 'editable': True,
                 "cellEditorParams": {"showStepperButtons": True, "min": 1, "max": 100, "precision": 0},
                 "valueFormatter": {"function": "params.value? params.value : 1 "}
                 },
                {'field': 'Peso',
                 'type': 'numericColumn',
                 'editable': True,
                 "cellEditorParams": {"showStepperButtons": True, "min": 1, "max": 100, "precision": 0},
                 "valueFormatter": {"function": "params.value? params.value : 1 "}
                 },
            ]
        }
    ]

    grid = dag.AgGrid(
        id="tabla_objetos",
        columnDefs=columnas,
        rowData=data,
        columnSize="sizeToFit",
        dashGridOptions={"domLayout": "autoHeight"},
        style={"height": None},
        defaultColDef={"resizable": False, "sortable": False, 'suppressMovable': True}
    )

    return grid
