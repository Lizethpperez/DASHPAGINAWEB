from dash import html
import dash_bootstrap_components as dbc

variableD = dbc.Container([
     dbc.Row([
         html.Br(),
         dbc.Col('IMAGEN FORMULA APLICADA', md=3, style={'textAlign': 'center', 'background-color': 'gray'}),
         html.Br(), 
         html.Br(),
          html.Br(),
           html.Br(),
            html.Br(),
             html.Br(),
              html.Br(),
               html.Br(),
                html.Br(),
                 html.Br(),
                  html.Br(),
                   html.Br(),
                    html.Br(),
        dbc.Col('RESULTADOS', md=8, style={'textAlign': 'center'})
    ])
])