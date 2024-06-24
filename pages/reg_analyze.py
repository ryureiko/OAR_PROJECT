from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df_region, counties

max_unemployed = 300
max_employed = 3500
df_region['unemployed_num_all'] = df_region['unemployed_num_all'].clip(upper=max_unemployed)
df_region['employed_num_all'] = df_region['employed_num_all'].clip(upper=max_employed)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H2("Карта уровня безработицы и занятости по регионам России", style={'textAlign': 'center'}),
            ])
        )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.P("Выберите параметр для отображения на карте:", style={'textAlign': 'center'}),
                dbc.RadioItems(
                    options=[
                        {'label': 'Уровень экономической активности', 'value': 'eactivity_lvl'},
                        {'label': 'Уровень безработицы', 'value': 'unemployment_lvl'},
                        {'label': 'Уровень занятости', 'value': 'employment_lvl'},
                        {'label': 'Численность безработных', 'value': 'unemployed_num_all'},
                        {'label': 'Численность занятых в экономике', 'value': 'employed_num_all'},
                    ],
                    value='eactivity_lvl',
                    id='crossfilter-ind',
                    inline=False  
                ),
            ]), width=3  
        ),
        dbc.Col([
            dcc.Graph(id='choropleth', config={'displayModeBar': False}, style={'height': '80vh', 'width': '100%'}),
        ], width=9)  
    ])
], fluid=True)

@callback(
    Output('choropleth', 'figure'),
    Input('crossfilter-ind', 'value'),
)
def update_choropleth(indication):

    figure = px.choropleth_mapbox(
        df_region,
        geojson=counties,
        featureidkey='properties.name',  
        color=indication, 
        locations='region', 
        color_continuous_scale=px.colors.sequential.BuPu,
        hover_name='region', 
        hover_data={
            'region': False,
            'eactivity_lvl': True,
            'unemployment_lvl': True,
            'employment_lvl': True,
            'unemployed_num_all': True,
            'employed_num_all': True,
        },
        labels={
            'region': 'Регион',
            'eactivity_lvl': 'Уровень экономической активности',
            'unemployment_lvl': 'Уровень безработицы',
            'employment_lvl': 'Уровень занятости',
            'unemployed_num_all': 'Численность безработных',
            'employed_num_all': 'Численность занятых в экономике',
        },
        mapbox_style="carto-positron",
        zoom=1.5,  
        center={"lat": 70, "lon": 100},
        opacity=0.5,
    )

    figure.update_layout(
        mapbox_style="carto-positron",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=False,
        coloraxis_colorbar={
            'orientation': 'h',
            'x': 0.5,
            'xanchor': 'center',
            'y': -0.1,
            'yanchor': 'bottom',
            'title': None
        },
        height=500,
    )

    return figure