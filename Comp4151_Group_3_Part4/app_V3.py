# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import portfolio
import datetime
import dash_table
import csv

external_stylesheets = ['https://codepen.io/chridd`yp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
port_df = pd.read_csv('my_portfolio.csv')

my_portfolio = portfolio.Portfolio()

app.layout = html.Div(children=[

    html.H1(children='Stock Portfolio'),

    html.Div(id='flavor_txt',
             children=[]
    ),

    html.Div(id='alo_txt',
             children=[]
    ),

    html.Div(id='ROI',
             children=[]
    ),

    html.Div(id='volatillity',
             children=[]
    ),

    dcc.Graph(
        id='stock_graph'
    ),

    dcc.Slider(
        id='time-slider',
        min=0,
        max=0,
        value=0,
    ),

    html.Div(id='cur_time',
             children=[]
    ),

    html.Div(id='error',
             children=[]
    ),

    html.Div(id='cap',
             children=[]
    ),

    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False} for i in port_df.columns
        ],
        data = port_df.to_dict('records'),
        editable=False,
        sort_action="native",
        sort_mode="multi",
        row_selectable="single",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),

    html.Div(["Stock Symbol: ",
              dcc.Input(id='stock_symbol', value='', type='text'),
              "Stock Allocation: ",
              dcc.Input(id='stock_allocation', value='', type='text'),
              "Investment Money",
              dcc.Input(id='capital', value='', type='text')]

    ),

    html.Button(id='submit-button-state', n_clicks=0, children='Submit')

])

@app.callback(
    [Output(component_id='time-slider', component_property='min'),
     Output(component_id='time-slider', component_property='max'),
     Output(component_id='time-slider', component_property='marks'),
     Output(component_id='cur_time', component_property='children'),
     Output(component_id='flavor_txt', component_property='children'),
     Output(component_id='alo_txt', component_property='children'),
     Output(component_id='ROI', component_property='children'),
     Output(component_id='volatillity', component_property='children'),
     Output(component_id='error', component_property='children'),
     Output(component_id='cap', component_property='children'),
     Output('stock_graph', 'figure'),
     Output('datatable-interactivity', 'data')],
    [Input('submit-button-state', 'n_clicks'),
     Input('time-slider', 'value')],
    [State('stock_symbol', 'value'),
     State('stock_allocation', 'value'),
     State('capital', 'value'),
     State('datatable-interactivity', 'data'),
     State('datatable-interactivity', 'data_previous')]
)

def update_graph(n_clicks, n, stock_symbol, allo, capital, cur_data, prev):

    fig=px.line()

    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    update_txt = 'Current Stock: '
    update_alo = 'Allocation: '
    update_ROI = 'Weighted ROI: '
    update_vol = 'Weighted Volatillity: '
    update_time = 'Current Time Range: '
    update_error = 'Notice: '
    update_cap = 'Capital Distribution: '

    marks={}
    alo_list = []
    updated_port = []

    df = pd.read_csv('my_portfolio.csv')
    temp = []
    if len(df) != len(cur_data):
        for k in cur_data:
            temp.append(k)
        df = pd.DataFrame.from_dict(temp)
        df.to_csv('my_portfolio.csv', index=False)

    data=df.to_dict('records')

    if stock_symbol != '' and allo != '':

        my_portfolio.add_stock_symbol(stock_symbol)
        my_portfolio.download_stock_summary(stock_symbol)
        ###################### FIX STOCK NAME ######################
        my_portfolio.initialize_stock('Stock_Name', stock_symbol, f'yf_{stock_symbol}.html')
        start = datetime.datetime(2015, 1, 2)
        end = datetime.datetime.now()
        my_portfolio.add_stock_price(stock_symbol, start, end)

        alo_list.append((stock_symbol, float(allo)))
        my_portfolio.allocate(alo_list)

        temp_df = pd.read_csv('my_portfolio.csv')
        updated_port = temp_df.to_dict('records')

        if stock_symbol in df.values:

            index = df.index[df['stock_symbol'] == stock_symbol][0]
            df['allocation'][index] = float(allo)
            data = df.to_dict('records')
            df.to_csv('my_portfolio.csv', index=False)

        else:

            with open('my_portfolio.csv', 'a+') as csvfile:

                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([stock_symbol, allo])

            df = pd.read_csv('my_portfolio.csv')
            data = df.to_dict('records')

        L = [df['stock_symbol'], df['allocation']]

        err, cap_list = my_portfolio.allocation_manager(L, float(capital))

        str_cap = ', '.join(str(e) for e in cap_list)
        update_txt += stock_symbol
        update_alo += allo
        update_error += err
        update_cap += str_cap

        df = my_portfolio.stocks[stock_symbol].prices[n:]
        n = len(my_portfolio.stocks[stock_symbol].prices)-2

        update_time = ('Current Time Range: ' +
                       df.index[0].strftime('%B %d, %Y') +
                       ' - ' +
                       df.index[len(df)-1].strftime('%B %d, %Y'))
        if n != 0:

            update_start = df.index[0]
            my_portfolio.add_stock_price(stock_symbol, update_start, end)

            alo_list.append((stock_symbol, float(allo)))
            my_portfolio.allocate(alo_list)

        update_ROI = 'Weighted ROI: {}'.format(my_portfolio.stocks[stock_symbol].weighted_ROI)
        update_vol = 'Weighted Volatillity: {}'.format(my_portfolio.stocks[stock_symbol].weighted_vol)

        fig = px.line(df, x=df.index, y=['Close'])

        colors = {
            'background': '#111111',
            'text': '#7FDBFF'
        }

        fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
        )

        marks={year: year for year in df.index.strftime('%Y-%m-%d')}

    return 0, n, marks, update_time, update_txt,  update_alo, update_ROI, update_vol, update_error, update_cap, fig, data



if __name__ == '__main__':
    app.run_server(debug=True)
