import json
import pandas as pd


with open("user_recently_played.json") as file:
    data = json.load(file)

df = pd.json_normalize([item["track"] for item in data["items"]])

print(df.head())

print(df.shape)