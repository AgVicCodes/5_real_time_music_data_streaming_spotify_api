# Spotify Data Streaming into SQL Server Database

This repository contains experimental scripts for fetching listening data from the Spotify Web API, normalizing it with pandas, and laying the groundwork for loading the results into a SQL Server database.

## Features
- Authenticate with Spotify using [Spotipy](https://spotipy.readthedocs.io/)
- Extract a user's recently played tracks
- Flatten nested track metadata into a tabular format

## Prerequisites
- Python 3.9+
- A Spotify developer account with a registered application

## Installation
```bash
git clone https://example.com/5_real_time_music_data_streaming_spotify_api.git
cd 5_real_time_music_data_streaming_spotify_api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Credentials
Create a `keys.json` file in the project root with your Spotify credentials:
```json
{
  "client_id": "<your_client_id>",
  "client_secret_key": "<your_client_secret>",
  "redirect_uri": "http://localhost:8888/callback"
}
```

## Usage
1. **Extract recently played tracks**
   ```bash
   python extract.py
   ```
   Saves the API response to a timestamped `recently_played_<n>.json` file.

2. **Transform the raw JSON**
   ```bash
   python transform.py
   ```
   Reads `user_recently_played.json` and prints a flattened `pandas` DataFrame.

## Sample Data
Example JSON responses (`recently_played*.json`, `user_recently_played.json`, etc.) are included for experimentation. Avoid committing personal data or secrets.

## Roadmap
- Load normalized data into SQL Server
- Orchestrate extraction and transformation with Apache Airflow
- Expand transformation logic and add a loading step

