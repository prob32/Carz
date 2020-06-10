import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
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
import webbrowser
from app2 import App2
from app import App, counts_viz, reg_sp
from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True
server = app.server

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

####Front page call backs
@app.callback(Output('page-content', 'children'),
             [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/simple-stats':
        return App()
    if pathname == '/predictions':
        return App2()
    else:
        return Homepage()


### Interactive call backs
@app.callback(
    Output(component_id='bar_count', component_property='figure'),
    [Input(component_id='product', component_property='value')])

def update_figure1(product):
    count_fig2 = counts_viz(product)
    return count_fig2

@app.callback(
    Output(component_id='scat_plot', component_property='figure'),
     [Input(component_id='X', component_property='value'),
     Input(component_id='Y', component_property='value')
     ])
def update_figure2(X,Y):
       sp_fig = reg_sp(X,Y)
       return  sp_fig


##### APP2###############
### Chained inputs for model by make #####
@app.callback(
    Output('model', 'options'),
    [Input('make', 'value')])
def set_model_options(selected_make):
    makes_by_model = pd.read_csv('makes_by_models.csv')
    makes_by_model = dict(makes_by_model.groupby('Make').agg(list).to_records())
    return [{'label': i, 'value': i} for i in makes_by_model[selected_make]]


##### Updating graph call backs #####
@app.callback(
    Output("model_graph", "figure"),
    [Input("model_select", "value"),
    ],)

def test (model_select):
    df = pd.read_csv('Model_Comparison.csv')
    df = df.sample(250)
    df = df.sort_values('Actual', ascending=True).reset_index(drop=True)
    t='markers'
    if model_select == 1:
        data =[

            go.Scatter(
                y=df.iloc[:,1],
                mode=t,
                name="RF_80% Acurate model",
            ),
            go.Scatter(
                y=df.iloc[:, 3],
                mode=t,
                name="OLS_80% Acurate mode",
            ),
            go.Scatter(
                y=df.iloc[:, 0],
                mode="lines",
                marker={"size": 8},
                name="Actual(base)"
            ),
        ]
    else:
        data = [

            go.Scatter(
                y=df.iloc[:, 2],
                mode=t,
                name="RF_60% Acurate model",
            ),
            go.Scatter(
                y=df.iloc[:, 4],
                mode=t,
                name="OLS_60% Acurate model",
            ),
            go.Scatter(
                y=df.iloc[:, 0],
                mode="lines",
                marker={"size": 8},
                name="Actual(base)"
            ),
        ]

    layout = {"yaxis": {"title": "Plot of Models"}}
    return  go.Figure(data=data, layout=layout)


#### OLS Predictions Call backs

@app.callback(Output("model-ols", "children"),
    [Input('submit-button-state', 'n_clicks')],
    [State("year", "value"),
     State("make", "value"),
     State("model", "value"),
     State("mileage", "value")])

def ols_return (n_clicks,year,make,model,mileage,):
    filename0 = 'input_list.sav.gz'
    df_list = joblib.load(filename0)
    year = str(year)
    make = str(make)
    model = str(model)
    estimate = model_inputs(mileage, year, make, model, df_list)
    filename2 = 'OLS_model.sav.gz'
    reg = joblib.load(filename2)
    ols_predictions = int(reg.predict(estimate))
    return ols_predictions

#### Repeat for RF model
@app.callback(Output("model-rf", "children"),
    [Input('submit-button-state', 'n_clicks')],
    [State("year", "value"),
     State("make", "value"),
     State("model", "value"),
     State("mileage", "value")])

def rf_return (n_clicks,year,make,model,mileage,):
    filename0 = 'input_list.sav.gz'
    df_list = joblib.load(filename0)
    year = str(year)
    make = str(make)
    model = str(model)
    estimate = model_inputs(mileage, year, make, model, df_list)
    filename = 'RF_model.sav.gz'
    rfc = joblib.load(filename)
    rf_predictions = int(rfc.predict(estimate))
    return rf_predictions
if __name__ == '__main__':
    app.run_server(port=8080, debug=True)