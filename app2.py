import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from predictions import model_inputs
import joblib
from navbar import Navbar


options= pd.read_csv('list_of_options.csv')
list_years =  options['Year'].to_list()
list_years = [x for x in list_years if str(x) != 'nan']
list_years = [ int(x) for x in list_years ]
list_years = sorted(list_years, reverse = True)
list_state = options['State'].to_list()
list_state = [x for x in list_state if str(x) != 'nan']
list_make = options['Make'].to_list()
list_make = [x for x in list_make if str(x) != 'nan']





fig = go.Figure()

nav = Navbar()


##### Inputs form for the graph ####
graph_controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Model Options"),
                dcc.Dropdown(
                    id="model_select",
                    options=[
                        {'label': 'Large Data set', 'value': 1},
                        {'label': 'Small Data Set', 'value': 2},

                    ],value=1,

                ),
            ]
        ),

    ],
    body=True,
)

##### Inputs for the models #####
estimate_controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                
				dbc.Label("Year"),
                dcc.Dropdown(
                    id="year",
                    options=[
                        {'label': i, 'value': i} for i in list_years


                    ],

                ),
				dbc.Label("Make"),
                dcc.Dropdown(
                    id="make",
                    options=[
                        {'label': i, 'value': i} for i in list_make


                    ],
                    value='Acura',

                ),
                dbc.Label("Model"),
                dcc.Dropdown(
                    id="model"
                ),
            ]
        ),
        dbc.FormGroup(
            [
            dbc.Label("Mileage"),
            dbc.Input(id="mileage", type="number", value=50000),
            html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
            ]
        ),

    ],
    body=True,
)

#### OLS Model predictions output card ######
model_ols = dbc.Card(
    [
        dbc.FormGroup(
            [
            dbc.Label("OLS Estimate"),
            html.Div(id="model-ols"),

            ]
        ),

    ],
    body=True,
)

#### RF Model predictions output card ######
model_rf = dbc.Card(
    [
        dbc.FormGroup(
            [
            dbc.Label("RF Estimate"),
            html.Div(id="model-rf"),
            ]
        ),

    ],
    body=True,
)

#### Bringing it together with the app layout ####
layout2 = dbc.Container(
    [
        html.H1("Models vs actual"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(graph_controls, md=3),
                dbc.Col(dcc.Graph(id="model_graph"), md=8),
            ],

            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(estimate_controls, md=3),
                dbc.Col(model_ols, md=3),
                dbc.Col(model_rf, md=3),
            ],

            align="center",
        ),
    ],
    fluid=True,
)


def App2():
    layout = html.Div([

    nav,

        layout2,

    ])
    return layout
