import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64



test_png = 'lighting_mcqueen.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

from navbar import Navbar
nav = Navbar()

body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("CarZZZ"),
                     html.P(
                         """This is my first multipage dash test! The purpose of the dashboard is to break out the effect of mileage, years, make and model on used car prices."""
                           ),
                           dbc.NavLink("View github", href="https://github.com/prob32/Carz"),

                   ],
                  md=4,
               ),
              dbc.Col(
                 html.Div([
                     html.H2("Lighting McQueen! Is not for sale sorry :("),
                     html.Img(src='data:image/png;base64,{}'.format(test_base64),
                        style={'height': '80%','width': '80%','display':'inline-block'})])
                     ),
                ]
            )
       ],
className="mt-4",
)
def Homepage():
    layout = html.Div([nav,body])
    return layout


