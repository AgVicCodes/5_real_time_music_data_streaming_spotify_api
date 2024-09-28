from glob import glob as gg
import pandas as pd
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

"""
    To do
    - Get apache airflow up and running
    - Extract spotify track metadata from id
    - Extract important stuff from the rest of the data
"""

json_files = gg(f"recently_played*.json")

json_file_count = len(json_files)

with open("keys.json") as file:
    keys = json.load(file)


client = SpotifyOAuth(
    client_id = keys["client_id"], 
    client_secret = keys["client_secret_key"], 
    redirect_uri = keys["redirect_uri"],
    scope = "user-read-recently-played"#"user-library-read"
    )

sp = spotipy.Spotify(auth_manager = client)

recently_played = sp.current_user_recently_played(limit = 50, before = "1725147380")

with open(f"recently_played_{json_file_count - 1}.json", "w") as file:
    json.dump(recently_played, file, indent = 4)