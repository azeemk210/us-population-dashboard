import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import numpy as np

# Load dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/JoshData/historical-state-population-csv/refs/heads/primary/historical_state_population_by_year.csv",
    names=["State", "Year", "Population"], header=0
)

# Convert columns to correct types
df["Year"] = df["Year"].astype(int)
df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

# Initialize Dash app
app = Dash(__name__)

# Define function to create choropleth map
def create_choropleth(year):
    df_year = df[df["Year"] == year]

    fig = px.choropleth(
        df_year,
        locations="State",
        locationmode="USA-states",
        color="Population",
        color_continuous_scale="Viridis",  # You can use 'Portland', 'YlOrRd', 'Plasma'
        scope="usa",
        hover_data=["State", "Population"],
        labels={"Population": "Population"},
        title=f"US Population by State ({year})"
    )
    
    fig.update_layout(height=600, margin={"r":0, "t":40, "l":0, "b":0})
    return fig

# Define function to create population trend line chart
def update_line_chart(clickData, selected_year):
    if clickData is None:
        return px.line(title="Click a state to view population trend")

    state_abbr = clickData["points"][0]["location"]
    state_df = df[df["State"] == state_abbr]

    fig = px.line(
        state_df,
        x="Year",
        y="Population",
        title=f"Population Trend for {state_abbr}",
        markers=True
    )
    
    fig.update_layout(height=400)
    fig.add_vline(x=selected_year, line_dash="dash", line_color="red")
    return fig

# App layout
app.layout = html.Div([
    html.H1("US Population Dashboard", style={"textAlign": "center"}),

    # Choropleth Map
    dcc.Graph(id="choropleth-map"),

    # Year dropdown
    html.Label("Select Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(year), "value": year} for year in sorted(df["Year"].unique())],
        value=df["Year"].max()
    ),

    # Population trend graph
    dcc.Graph(id="population-trend")
])

# Define callbacks
@app.callback(
    Output("choropleth-map", "figure"),
    Input("year-dropdown", "value")
)
def update_map(selected_year):
    return create_choropleth(selected_year)

@app.callback(
    Output("population-trend", "figure"),
    Input("choropleth-map", "clickData"),
    Input("year-dropdown", "value")
)
def update_trend(clickData, selected_year):
    return update_line_chart(clickData, selected_year)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
