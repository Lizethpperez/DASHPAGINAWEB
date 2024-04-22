from dash import html
import dash_bootstrap_components as dbc

variableA = dbc.Container([
    dbc.Row([
        dbc.Col('LOGO', md=14, style={'background-color': 'red'}),
        dbc.Col('DISEÑA TU CANAL', md=14, style={'background-color': 'skyblue'}, align="center"),
    ])
])