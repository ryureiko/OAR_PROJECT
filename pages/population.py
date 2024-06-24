from dash import dcc, html, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
from data import df

regions = df['region'].unique()

years = df['year'].unique()

age_group_labels = {
    'num_unagegroup_to20': 'до 20 лет',
    'num_unagegroup_20-29': 'от 20 до 29 лет',
    'num_unagegroup_30-39': 'от 30 до 39 лет',
    'num_unagegroup_40-49': 'от 40 до 49 лет',
    'num_unagegroup_50-59': 'от 50 до 59 лет',
    'num_unagegroup_60older': '60 и более лет',
    'num_emagegroup_to20': 'до 20 лет',
    'num_emagegroup_20-29': 'от 20 до 29 лет',
    'num_emagegroup_30-39': 'от 30 до 39 лет',
    'num_emagegroup_40-49': 'от 40 до 49 лет',
    'num_emagegroup_50-59': 'от 50 до 59 лет',
    'num_emagegroup_60older': '60 и более лет'
}

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Численность безработных и занятых по возрастным группам по регионам РФ", className="text-center"))
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Выберите регион"),
            dcc.Dropdown(
                id='region-dropdown-bar',
                options=[{'label': region, 'value': region} for region in regions],
                value=regions[0], 
                placeholder="Выберите регион",
                style={'width': '100%'}
            )
        ], width=6),
        dbc.Col([
            html.Label("Выберите год"),
            dcc.Dropdown(
                id='year-dropdown-bar',
                options=[{'label': str(year), 'value': year} for year in years],
                value=years[-1],  
                placeholder="Выберите год",
                style={'width': '100%'}
            )
        ], width=6),
    ], style={'margin-bottom': '20px'}), 
    dbc.Row([
        dbc.Col(dcc.Graph(id='unemployed-age-group-bar')),
    ], style={'margin-bottom': '40px'}), 
    dbc.Row([
        dbc.Col(dcc.Graph(id='employed-age-group-bar')),
    ]),
], fluid=True)

@callback(
    Output('unemployed-age-group-bar', 'figure'),
    [Input('region-dropdown-bar', 'value'),
     Input('year-dropdown-bar', 'value')]
)
def update_unemployed_age_group_bar(region, year):
    filtered_data = df[(df['region'] == region) & (df['year'] == year)]

    unemployed_data = filtered_data[[
        'num_unagegroup_to20', 'num_unagegroup_20-29', 'num_unagegroup_30-39', 
        'num_unagegroup_40-49', 'num_unagegroup_50-59', 'num_unagegroup_60older'
    ]].sum().reset_index()

    # Перевод меток
    unemployed_data['index'] = unemployed_data['index'].map(age_group_labels)

    fig = px.bar(unemployed_data, x='index', y=0,
                 title=f'Распределение численности безработных по возрастным группам <br> в регионе {region} ({year})',
                 labels={'index': 'Возрастные группы', '0': 'Численность безработных'})

    fig.update_traces(marker_color='rgba(93, 164, 214, 0.8)', marker_line_color='rgba(93, 164, 214, 1.0)',
                      marker_line_width=2, width=0.5)  

    fig.update_layout(
        legend_title_text='Возрастные группы',
        xaxis_title='Возрастные группы',
        yaxis_title='Численность безработных',
        title_x=0.5,
        font=dict(size=12, color='#2c3e50'),
        paper_bgcolor='#ecf0f1',
        plot_bgcolor='#ecf0f1',
        xaxis=dict(
            showgrid=False,  
            zeroline=False,  
            tickmode='linear',
            dtick=1  
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

@callback(
    Output('employed-age-group-bar', 'figure'),
    [Input('region-dropdown-bar', 'value'),
     Input('year-dropdown-bar', 'value')]
)
def update_employed_age_group_bar(region, year):

    filtered_data = df[(df['region'] == region) & (df['year'] == year)]

    employed_data = filtered_data[[
        'num_emagegroup_to20', 'num_emagegroup_20-29', 'num_emagegroup_30-39',
        'num_emagegroup_40-49', 'num_emagegroup_50-59', 'num_emagegroup_60older'
    ]].sum().reset_index()

    employed_data['index'] = employed_data['index'].map(age_group_labels)

    fig = px.bar(employed_data, x='index', y=0,
                title=f'Распределение численности занятых по возрастным группам <br> в регионе {region} ({year})',
                labels={'index': 'Возрастные группы', '0': 'Численность занятых'})

    fig.update_traces(marker_color='rgba(255, 144, 14, 0.8)', marker_line_color='rgba(255, 144, 14, 1.0)',
                      marker_line_width=2, width=0.5) 

    fig.update_layout(
        legend_title_text='Возрастные группы',
        xaxis_title='Возрастные группы',
        yaxis_title='Численность занятых',
        title_x=0.5,
        font=dict(size=12, color='#2c3e50'),
        paper_bgcolor='#ecf0f1',
        plot_bgcolor='#ecf0f1',
        xaxis=dict(
            showgrid=False,  
            zeroline=False,  
            tickmode='linear',
            dtick=1  
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