import dash_ag_grid as dag
import pandas as pd


def tabla_individuos():
    data = [
        {'Individuo': 'Individuo 1', '1': 1, '2': 1, '3': 0, '4': 0},
        {'Individuo': 'Individuo 2', '1': 0, '2': 1, '3': 1, '4': 0},
        {'Individuo': 'Individuo 3', '1': 0, '2': 0, '3': 1, '4': 1},
        {'Individuo': 'Individuo 4', '1': 1, '2': 0, '3': 0, '4': 1},
    ]

    columnas = [
        {'field': 'Individuo'},
        {
            'headerName': 'Bits',
            'headerClass': 'center-aligned-group-header',
            'children': [
                {'field': '1',
                 'type': 'numericColumn',
                 'editable': True,
                 'width': 90,
                 "cellEditorParams": {"showStepperButtons": True, "min": 0, "max": 1, "precision": 0},
                 "valueFormatter": {"function": "params.value? params.value : 0 "}
                 },
                {'field': '2',
                 'type': 'numericColumn',
                 'editable': True,
                 'width': 90,
                 "cellEditorParams": {"showStepperButtons": True, "min": 0, "max": 1, "precision": 0},
                 "valueFormatter": {"function": "params.value? params.value : 0 "}
                 },
                {'field': '3',
                 'type': 'numericColumn',
                 'editable': True,
                 'width': 90,
                 "cellEditorParams": {"showStepperButtons": True, "min": 0, "max": 1, "precision": 0},
                 "valueFormatter": {"function": "params.value? params.value : 0 "}
                 },
                {'field': '4',
                 'type': 'numericColumn',
                 'editable': True,
                 'width': 90,
                 "cellEditorParams": {"showStepperButtons": True, "min": 0, "max": 1, "precision": 0},
                 "valueFormatter": {"function": "params.value? params.value : 0 "}
                 }
            ]
        }
    ]

    grid = dag.AgGrid(
        id="tabla_individuos",
        columnDefs=columnas,
        rowData=data,
        columnSize="sizeToFit",
        dashGridOptions={"domLayout": "autoHeight"},
        style={"height": None},
        defaultColDef={"resizable": False, "sortable": False, 'suppressMovable': True}
    )

    return grid
