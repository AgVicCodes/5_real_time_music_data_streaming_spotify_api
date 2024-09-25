import pandas as pd
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth


with open("keys.json") as file:
    keys = json.load(file)


client = SpotifyOAuth(
    client_id = keys["client_id"], 
    client_secret = keys["client_secret_key"], 
    redirect_uri = keys["redirect_uri"],
    scope = "user-read-recently-played"#"user-library-read"
    )

sp = spotipy.Spotify(auth_manager = client)


with open("user_recently_played.json") as file:
    data = json.load(file)

print(data["items"][1]["track"]["album"]["id"])

df = pd.json_normalize(data["items"][1]["track"])

print(df.head())