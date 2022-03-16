import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output, State

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['total exports', 'beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']

mycolumn='corn'
tabtitle = 'Old McDonald'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/pratikadyalkar/301-old-mcdonald'
myheading1 = f"Wow! That's a lot of {mycolumn}!"
colors = {
    'background': '#999999',
    'text': '#7FDBFF',
    'top': '#454545'
}

########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/usa-2011-agriculture.csv')



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

@app.callback(Output('figure-1', 'figure'),
             [Input('options-drop', 'value')])
def create_graph(col):
    
    myheading1 = f"Wow! That's a lot of {col}!"
    mygraphtitle = '2011 US Agriculture Exports by State'
    mycolorscale = 'Reds' # Note: The error message will list possible color scales.
    mycolorbartitle = "Millions USD"
    
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'], # Spatial coordinates
        z = df[col].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = mycolorscale,
        colorbar_title = mycolorbartitle,
    ))

    fig.update_layout(
        title_text = myheading1,
        geo_scope='usa',
        width=1200,
        height=800
    )
    
    return fig

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(
        children = '2011 Agricultural Exports, by State',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'background': colors['top']
            
        }),
    html.Div([
        html.Div([
                html.H6('Select a variable for analysis:'),
                dcc.Dropdown(
                    id='options-drop',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value='corn'
                ),
        ], className='twelve columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='twelve columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.br(),
    html.A("Data Source", href=sourceurl),
    ],className='blockquote'
)
############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
