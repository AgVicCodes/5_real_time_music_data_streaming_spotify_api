
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