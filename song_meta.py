# Track ID for the song you want to get metadata for
track_id = 'your-track-id'

# Get track metadata
track = sp.track(track_id)

# Print some metadata
print(f"Track Name: {track['name']}")
print(f"Artist: {track['artists'][0]['name']}")
print(f"Album: {track['album']['name']}")
print(f"Release Date: {track['album']['release_date']}")
print(f"Popularity: {track['popularity']}")


v# Function to get track details
def get_track_details(track_id):
    track = sp.track(track_id)
    return {
        'name': track['name'],
        'artist': track['artists'][0]['name'],
        'album': track['album']['name'],
        'popularity': track['popularity'],
        'id': track['id']
    }

# Example track ID
track_id = 'your-track-id'
track_details = get_track_details(track_id)
print(track_details)


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample data
tracks = [
    {'id': '1', 'name': 'Song1', 'artist': 'Artist1', 'genre': 'Pop'},
    {'id': '2', 'name': 'Song2', 'artist': 'Artist2', 'genre': 'Rock'},
    # Add more tracks
]

# Create a DataFrame
df = pd.DataFrame(tracks)

# Vectorize the genre
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(track_id, cosine_sim=cosine_sim):
    idx = df.index[df['id'] == track_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 recommendations
    track_indices = [i[0] for i in sim_scores]
    return df.iloc[track_indices]

# Get recommendations for a track
recommendations = get_recommendations('1')
print(recommendations)