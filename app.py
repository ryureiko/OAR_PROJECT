import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from pages import active_people, level, population, reg_analyze

external_stylesheets = [dbc.themes.JOURNAL]
app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#2c3e50", 
    "color": "white", 
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#ecf0f1",  
}

sidebar = html.Div(
    [
        html.H4("Экзаменационный проект", className="display-9", style={"color": "#ecf0f1"}),
        html.Hr(style={"border-color": "#ecf0f1"}),
        html.P(
            "Статистические данные о занятости и безработице", className="lead", style={"color": "#bdc3c7"}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Численность экономически активного населения", href="/", active="exact", style={"color": "#ecf0f1"}),
                dbc.NavLink("Распределение безработных и занятых", href="/page-1", active="exact", style={"color": "#ecf0f1"}),
                dbc.NavLink("Численность безработных и занятых", href="/page-2", active="exact", style={"color": "#ecf0f1"}),
                dbc.NavLink("Региональный анализ на карте РФ", href="/page-3", active="exact", style={"color": "#ecf0f1"}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return active_people.layout
    elif pathname == "/page-1":
        return level.layout
    elif pathname == "/page-2":
        return population.layout
    elif pathname == "/page-3":
        return reg_analyze.layout
    
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run_server(debug=True)
