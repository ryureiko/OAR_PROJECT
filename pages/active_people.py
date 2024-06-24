from dash import dcc, html, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
from data import df  

years = df['year'].unique()

regions = df['region'].unique()

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Численность экономически активного населения по годам", className="text-center"))
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Выберите регион"),
            dcc.Dropdown(
                id='region-dropdown-line',
                options=[{'label': region, 'value': region} for region in regions],
                value=regions[0],  
                placeholder="Выберите регион",
                style={'width': '100%'}
            )
        ], width=4),
        dbc.Col([
            html.Label("Выберите период времени"),
            dcc.RangeSlider(
                id='year-range-slider',
                min=min(years),
                max=max(years),
                value=[min(years), max(years)],
                marks={str(year): str(year) for year in years},
                step=None  
            ),
        ], width=8),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='economactive-population-line')),
    ]),
], fluid=True)

@callback(
    Output('economactive-population-line', 'figure'),
    [Input('region-dropdown-line', 'value'),
     Input('year-range-slider', 'value')]
)
def update_economactive_population_line(region, year_range):
    filtered_data = df[(df['region'] == region) & 
                       (df['year'] >= year_range[0]) & 
                       (df['year'] <= year_range[1])]
    
    fig = px.line(filtered_data, x='year', y='num_economactivepopulation_all',
                  title=f'Численность экономически активного населения в регионе {region}',
                  labels={'year': 'Год', 'num_economactivepopulation_all': 'Экономически активное население'})

    fig.update_traces(line=dict(color='#EB6864', width=3, shape='spline'))
    
    fig.update_layout(
        title={'font': {'size': 16}},
        xaxis_title='Период',
        yaxis_title='Население',
        title_x=0.5,
        plot_bgcolor='#ecf0f1',
        paper_bgcolor='#ecf0f1',
        font=dict(color='#2c3e50', size=12),
        xaxis=dict(
            showgrid=True,
            gridcolor='LightGrey',
            zerolinecolor='LightGrey',
            tickmode='linear',
            dtick=1,  
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='LightGrey',
            zerolinecolor='LightGrey'
        ),
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    return fig