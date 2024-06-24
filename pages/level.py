from dash import dcc, html, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
from data import df

# Список возможных регионов
regions = df['region'].unique()

# Список возможных лет
years = df['year'].unique()

# Словарь для маппинга имен столбцов на их русские эквиваленты
age_group_labels = {
    'dis_unagegroup_to20': 'до 20 лет',
    'dis_unagegroup_20-29': 'от 20 до 29 лет',
    'dis_unagegroup_30-39': 'от 30 до 39 лет',
    'dis_unagegroup_40-49': 'от 40 до 49 лет',
    'dis_unagegroup_50-59': 'от 50 до 59 лет',
    'dis_unagegroup_60older': '60 и более лет',
    'dis_emagegroup_to20': 'до 20 лет',
    'dis_emagegroup_20-29': 'от 20 до 29 лет',
    'dis_emagegroup_30-39': 'от 30 до 39 лет',
    'dis_emagegroup_40-49': 'от 40 до 49 лет',
    'dis_emagegroup_50-59': 'от 50 до 59 лет',
    'dis_emagegroup_60older': '60 и более лет'
}

# Макет страницы
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Распределение безработных и занятых по возрастным группам по регионам РФ", className="text-center"))
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Выберите регион"),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': region, 'value': region} for region in regions],
                value=regions[0], 
                placeholder="Выберите регион",
                style={'width': '100%'}
            )
        ], width=6),
        dbc.Col([
            html.Label("Выберите год"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in years],
                value=years[-1],  
                placeholder="Выберите год",
                style={'width': '100%'}
            )
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='unemployed-age-group-pie')),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='employed-age-group-pie')),
    ]),
], fluid=True) 

# Обратные вызовы для обновления графиков при изменении параметров

@callback(
    Output('unemployed-age-group-pie', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_unemployed_age_group_pie(region, year):
    # Фильтрация данных по выбранному региону и году для безработных
    filtered_data = df[(df['region'] == region) & (df['year'] == year)]

    # Суммирование численности безработных по возрастным группам
    unemployed_data = filtered_data[[
        'dis_unagegroup_to20', 'dis_unagegroup_20-29', 'dis_unagegroup_30-39', 
        'dis_unagegroup_40-49', 'dis_unagegroup_50-59', 'dis_unagegroup_60older'
    ]].sum()

    # Перевод меток
    unemployed_data.index = unemployed_data.index.map(age_group_labels)

    # Цветовая гамма для круговой диаграммы
    colors = ['#B2A2C7', '#C4D79A', '#DA9695', '#92CDDC', '#FAD890', '#558ED5']

    fig = px.pie(
        names=unemployed_data.index,
        values=unemployed_data.values,
        title=f'Распределение численности безработных по возрастным группам <br>в регионе {region} ({year})',
        labels={'index': 'Возрастные группы', 'value': 'Численность безработных'},
        color_discrete_sequence=colors
    )

    fig.update_layout(
        legend_title_text='Возрастные группы',
        legend=dict(
            orientation='v',
            yanchor='top',
            y=0.8, 
            xanchor='left',
            x=0.9  
        ),
        title_x=0.5,
        font=dict(size=12, color='#2c3e50'),
        paper_bgcolor='#ecf0f1',
        plot_bgcolor='#ecf0f1'
    )

    return fig

@callback(
    Output('employed-age-group-pie', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_employed_age_group_pie(region, year):
    # Фильтрация данных по выбранному региону и году для занятых
    filtered_data = df[(df['region'] == region) & (df['year'] == year)]

    # Суммирование численности занятых по возрастным группам
    employed_data = filtered_data[[
        'dis_emagegroup_to20', 'dis_emagegroup_20-29', 'dis_emagegroup_30-39',
        'dis_emagegroup_40-49', 'dis_emagegroup_50-59', 'dis_emagegroup_60older'
    ]].sum()

    # Перевод меток
    employed_data.index = employed_data.index.map(age_group_labels)

    # Цветовая гамма для круговой диаграммы
    colors = ['#B2A2C7', '#C4D79A', '#DA9695', '#92CDDC', '#FAD890', '#558ED5']

    fig = px.pie(
        names=employed_data.index,
        values=employed_data.values,
        title=f'Распределение численности занятых по возрастным группам <br>в регионе {region} ({year})',
        labels={'index': 'Возрастные группы', 'value': 'Численность занятых'},
        color_discrete_sequence=colors
    )

    fig.update_layout(
        legend_title_text='Возрастные группы',
        legend=dict(
            orientation='v',
            yanchor='top',
            y=0.8,  
            xanchor='left',
            x=0.9  
        ),
        title_x=0.5,
        font=dict(size=12, color='#2c3e50'),
        paper_bgcolor='#ecf0f1',
        plot_bgcolor='#ecf0f1'
    )

    return fig
