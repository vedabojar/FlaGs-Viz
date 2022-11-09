from dash import html, dcc
from dash.dependencies import Input, Output

import MyDashApp.src.app as app
from pages import help, home


app.layout = html.Div([
        dcc.Location(id = 'url', refresh = False),
        html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/help':
        return help.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug = True)