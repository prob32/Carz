# Cars!


Welcome to my interactive dashboard for an analysis of used car 2017 used car prices from truecar.com as found on Kaggle
https://carz2.herokuapp.com/

This dash app was built using Plotly, Dash and Dash bootstrap packages on python

# The basic outline of this program is as follow:

index.py <- Master python file that runs the web application, all callbacks are based on this page 
homepage.py <-Home page layout and verbage
app.py<- simply statistics page, includes layouts and graph templates before population
app2.py<- Random forest vs OLS page, includes layouts and graph templates

# Heroku web based requirments
requirments.txt <- a list of imported packages for heroku to download to run the app
procfile <- required for heroku to run the app
favicon <- url image widget 
gui<- tell heroku what to launch

All other files are imports for the program and include model import saved in compressed format, images to call and data sets to import for analysis 
