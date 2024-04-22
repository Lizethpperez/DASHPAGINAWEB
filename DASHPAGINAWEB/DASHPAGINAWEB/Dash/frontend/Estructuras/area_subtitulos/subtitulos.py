from dash import html
import dash_bootstrap_components as dbc

variableB = dbc.Container([
        html.Button('INICIO', style={'background-color':'grey'}),
        html.Button('CANAL RECTANGULAR', style={'background-color':'grey'}),
        html.Button('CANAL TRAPEZOIDAL', style={'background-color':'grey'}),
        html.Button('CANAL CIRCULAR', style={'background-color':'grey'}),
        html.Button('CANAL TRIANGULAR', style={'background-color':'grey'})
    ])