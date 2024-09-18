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

# user_playlists = sp.current_user_playlists(limit = 50)

# user_recently_played = sp.current_user_recently_played(limit = 50, after = 1726426434)

# json. user_playlists["items"].json()

# with open("user_recently_played.json", "w") as file:
#     json.dump(user_recently_played, file, indent = 4)

# with open("userplaylist.json", "w") as file:
#     json.dump(user_playlists, file, indent = 4)

# print(data)

# print("Playlist keys:", [key for key in user_playlists.keys()])
# # Playlist keys: ['href', 'limit', 'next', 'offset', 'previous', 'total', 'items']
# print("Song keys:", [key for key in user_recently_played.keys()])
# # Song keys: ['items', 'next', 'cursors', 'limit', 'href']

with open("user_recently_played.json") as file:
    data = json.load(file)

df = pd.read_dict(data)

    # if data["type"] == "album":
    #     print("True")
    
    # else:
    #     print("False")