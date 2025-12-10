"""Main module for analyze weather datas."""

import os
import time
import pandas as pd
import plotly.express as px

start = time.time()

# Get current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_json("./API.json")

print(
    f"""------------------------------
Mean temperature(C): {df['temperature_c'].mean():.3f}
Mean precipitation(mm): {df["precipitation_mm"].mean()}
Count of "Clear" days: {df["weather_type"].value_counts()['Clear']}
Count of "Rainy" days: {df["weather_type"].value_counts()['Rainy']}
Count of "Snowy" days: {df["weather_type"].value_counts()['Snowy']}
The coldest day: {df["temperature_c"].min()}
The hottest day: {df["temperature_c"].max()}
------------------------------"""
)
end = time.time()
print(f"[⌛️] Program execution time: >>>{end-start:.10f}s <<<")

fig = px.scatter(
    df,
    x="date",
    y="temperature_c",
    hover_data=["date", "temperature_c", "precipitation_mm", "weather_type"],
    title="Daily Temperature (Interactive)",
)
fig.show()
