import dash
from dash import html
import dash_bootstrap_components as dbc 

#importamos los enlaces de las otras carpetas
from Dash.frontend.Estructuras.area_superior.titulo import variableA
from Dash.frontend.Estructuras.area_subtitulos.subtitulos import variableB
from Dash.frontend.Estructuras.area_datos.datosentrada import variableC
from Dash.frontend.Estructuras.area_resultados.resultados import variableD

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([
     dbc.Row([
        dbc.Col(variableA, md=12, style={'textAlign': 'center'}),
        dbc.Col(variableB, md=12, style={'background-color':'green', 'textAlign': 'center'}),
        dbc.Col(variableC, md=12, style={'background-color':'yellow'}),
        dbc.Col(variableD, md=12, style={'background-color':'skyblue'}),
     ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
