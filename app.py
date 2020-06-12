

import pandas as pd
import plotly.express as px
import base64


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from navbar import Navbar
import dash_bootstrap_components as dbc



df = pd.read_csv('cars_500k.csv')
df["Model"] = df["Make"] + " " + df["Model"]
scatterplot_items=['Price','Mileage','Year']

corr_png = 'corrheat.png'
corr_base64 = base64.b64encode(open(corr_png, 'rb').read()).decode('ascii')



def counts_viz (type):
    make_more_than_twenty_thousand = df.groupby(type).filter(lambda x: len(x) > 1000)
    count_fig = px.histogram(make_more_than_twenty_thousand,x=type)
    return count_fig

def reg_sp(X,Y):
    dfSample = df.sample(1000)
    reg_fig = px.scatter(dfSample, x=X, y=Y, trendline="ols")
    return reg_fig

nav = Navbar()

myheading1='Carz Test'
header = html.Div([html.H1(myheading1), html.P("Learning Dash is so interesting!!")],)



count_graphics = html.Div([

     dbc.Row([
      dbc.Col(

            ### column 1 div
            html.Div([
                 ##label
                html.H2("A graphic outlining the total number car listed by make and model"),
                ###dropdown
                html.Label('Make or model'),
                dcc.Dropdown(
                    id='product',
                    options=[
                        {'label': 'Make', 'value': 'Make'},
                        {'label': 'Model', 'value': 'Model'}], value='Make'),



            html.P(
              """A large part of car used car buying is knowing how big a pool of total vehicles is available, browse by make or model. Due to the number large number of cars makes and models a manufacturer must have a minimum of 10,0000 makes or models to appear on this graphic."""
          )],style={'marginLeft': 20,'width': '90%','display':'inline-block'}),

         ),

    ### column 2 graphic
      dbc.Col(
          html.Div([
              html.H2("Bar chart"),
              dcc.Graph(id='bar_count'), ],style={'width': '100%','display':'inline-block'}),

       ),
     ],
     ),
    ### row 2 drop down and graphic
     dbc.Row([
         #### column 1 drop downs
        dbc.Col(
            html.Div([
                html.H2("A graphic outlining the total number car listed by make and model"),
                html.Label('Input X variable'),
                ### label
                dcc.Dropdown(
                    id='X',
                    options=[{'label': i, 'value': i} for i in scatterplot_items], value='Mileage'),

                ### Y Input
                html.Label('Input Y variable'),
                dcc.Dropdown(
                    id='Y',
                    options=[{'label': i, 'value': i} for i in scatterplot_items], value='Price'),
                html.P(
              """Intuitively we know that used car buying is largely a tradeoff between mileage, vehicle age and price. Use the below inputs to create different scatterplots. See if you can determine relationships between, price and mileage or years and mileage. Try it out!"""
                )
                ],style={'marginLeft': 20,'width': '90%','display':'inline-block'})

            ),    #### column 2 div
      ### Column 2 graphics
      dbc.Col([
            html.Div([
                    html.H2("Scatterplot"),
                    dcc.Graph(id='scat_plot', figure=reg_sp('Mileage', 'Price')),




                ],     style={'width': '100%','display':'inline-block'},)
            ]),
     ]),
      dbc.Row([
          dbc.Col(
              html.Div([
                html.H2("A correlation heatmap of all variables"),
                html.P(
                    """This heatmap is a static PNG created from the seaborn package for python. It maps the correlation 
                        coefficient between variables. We can see from the chart that years of a vehicle has a positive
                        correlation coefficient with vehicle price. We can also see that mileage and year and year and
                        price have a negative coefficient. The coefficient for year is by far the largest at 40%, what 
                        are some other things you have noticed?"""
                )
              ], style={'marginLeft': 20, 'width': '90%', 'display': 'inline-block'})



          ),
          dbc.Col(
              html.Div([
                        html.H2("Correlation heatmap"),
                        html.Img(src='data:image/png;base64,{}'.format(corr_base64),
                        style={'height': '70%','width': '70%','display':'inline-block'})
              ],
              )
          ),
      ])
    ])


def App():
    layout = html.Div([

    nav,

        count_graphics,

    ])
    return layout

