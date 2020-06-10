import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Simple Statistics", href="/simple-stats")),
            
            dbc.NavItem(dbc.NavLink("Random forest vs OLS", href="/predictions")),



        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
    )


    return navbar
