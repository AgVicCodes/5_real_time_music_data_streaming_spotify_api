
# df = pd.json_normalize(data)

# print(df.head())

    # if data["type"] == "album":
    #     print("True")
    
    # else:

# client = SpotifyOAuth(
#     client_id = keys["client_id"], 
#     client_secret = keys["client_secret_key"], 
#     redirect_uri = keys["redirect_uri"],
#     scope = "user-read-recently-played"#"user-library-read"
#     )


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

    #     print("False")

# for i in range(len(data["items"])):
#     temp_df = pd.json_normalize(data["items"][i]["track"])
#     df = df._append(temp_df) 

# df = pd.DataFrame(columns = ["artists", "available_markets", "disc_number", 
#                              "duration_ms", "explicit", "href", "id", 
#                              "is_local", "name", "popularity", "preview_url", 
#                              "track_number", "type", "uri", "album.album_type", 
#                              "album.artists", "album.available_markets", 
#                              "album.external_urls.spotify", "album.href", 
#                              "album.id", "album.images", "album.name", 
#                              "album.release_date", "album.release_date_precision", 
#                              "album.total_tracks", "album.type", "album.uri", 
#                              "external_ids.isrc", "external_urls.spotify"])

# pd.set_option("display.max_columns", None)