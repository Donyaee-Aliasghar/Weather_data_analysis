#!/usr/bin/env python3
"""
Generate 365-day weather JSON with rules from the user:
- temperature between -10 and 30
- precipitation between 0 and 20 mm
- weather type: "Rainy", "Snowy", "Clear"
- days < 0: higher chance of Snowy
- hot days: higher chance of Rainy and Clear

Writes output to `365_weather.json` in the same folder.
"""
import json
import random
from datetime import date, timedelta

random.seed(42)

START = date(2025, 1, 1)
NUM_DAYS = 365
OUT_PATH = "API.json"


def pick_weather(temp_c, precipitation_mm):
    # Base probabilities [Snowy, Rainy, Clear]
    if temp_c < 0:
        probs = [0.7, 0.2, 0.1]
    elif temp_c > 20:
        probs = [0.02, 0.48, 0.5]
    else:
        probs = [0.05, 0.4, 0.55]

    # If there's measurable precipitation and temp >= 0, favor Rainy
    if precipitation_mm > 5 and temp_c >= 0:
        probs = [probs[0] * 0.5, min(1.0, probs[1] + 0.2), max(0.0, probs[2] - 0.2)]

    # If temp is below freezing but precipitation is low, still prefer Snowy
    if temp_c < 0 and precipitation_mm < 1:
        probs = [min(1.0, probs[0] + 0.1), probs[1] * 0.8, probs[2] * 0.9]

    # Normalize
    s = sum(probs)
    probs = [p / s for p in probs]

    r = random.random()
    if r < probs[0]:
        return "Snowy"
    elif r < probs[0] + probs[1]:
        return "Rainy"
    else:
        return "Clear"


data = []
for i in range(NUM_DAYS):
    d = START + timedelta(days=i)
    temp = random.randint(-10, 30)
    precip = round(random.uniform(0, 20), 1)

    # Slight physical constraint: if temp < 0 and precip very small, allow Snowy still
    weather = pick_weather(temp, precip)

    # If weather is Clear, reduce precipitation to near zero
    if weather == "Clear":
        precip = round(random.uniform(0, 1), 1)

    # If Snowy but temp > 3, very unlikely -- force Snowy only when temp <= 3
    if weather == "Snowy" and temp > 3:
        weather = "Rainy"

    entry = {"date": d.isoformat(), "temperature_c": temp, "precipitation_mm": precip, "weather_type": weather}
    data.append(entry)

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(data)} entries to {OUT_PATH}")
