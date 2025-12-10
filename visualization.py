"Module for analyze visualization."

import plotly.express as px

from pandas import DataFrame


def vis(df: DataFrame):

    fig_dt = px.scatter(
        df,
        x="date",
        y="temperature_c",
        hover_data=["date", "temperature_c", "precipitation_mm", "weather_type"],
        title="Daily Temperature (Interactive)",
    )

    fig_l = px.line(
        df,
        x="date",
        y="precipitation_mm",
        title="Daily Precipitation Trend",
    )
    fig_t = px.histogram(
        df,
        x="temperature_c",
        nbins=30,
        title="Temperature Distribution",
    )
    fig_tvp = px.scatter(
        df,
        x="temperature_c",
        y="precipitation_mm",
        color="weather_type",
        title="Temperature vs Precipitation",
    )
    fig_dt.show()
    fig_l.show()
    fig_t.show()
    fig_tvp.show()
