"""Main module for analyze weather datas."""

import os
import time
import pandas as pd
import plotly.express as px

start = time.time()

# Get current working directory
BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_json(os.path.join(BASE, "API.json"))

df = pd.read_json("./API.json")
df = df.sort_values("data")
df["date"] = pd.to_datetime(df["date"])

counts = df["weather_type"].value_counts()
clear_days = counts.get("Clear", 0)
rainy_days = counts.get("Rainy", 0)
snowy_days = counts.get("Snowy", 0)


print(
    f"""------------------------------
Mean temperature(C): {df['temperature_c'].mean():.3f}
Mean precipitation(mm): {df["precipitation_mm"].mean()}
Count of "Clear" days: {clear_days}
Count of "Rainy" days: {rainy_days}
Count of "Snowy" days: {snowy_days}
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
