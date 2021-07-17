from fastapi import FastAPI
import googlescraper
import json
from SpotifyAPIManager import Spotify

app = FastAPI()

spotify = Spotify()

@app.get("/current")
async def current():
    spotify.login()
    currentInformation = spotify.currentSong()

    for mark in ['&', '/', ' ']:
        artist = currentInformation['artist'].replace(mark, "+")
        song = currentInformation['song'].replace(mark, "+")
        
    data =  get_info(artist, song)
    return data

@app.get("/")
async def root():
    return {"message": "welcome"}

@app.get("/{artist_name}/{song_name}")
def get_info(artist_name, song_name):
    
    try:
        # url = f"https://www.azlyrics.com/lyrics/{artist_name}/{song_name}.html"
        url = f"http://www.google.com/search?q={artist_name}+{song_name}+lyrics"
        parsed = googlescraper.parse_url(url)
        title = googlescraper.get_title(parsed)
        lyrics = googlescraper.get_lyrics(parsed)
        artist = googlescraper.get_artist(parsed)

        data = {"title": title,
                "artist": artist,
                "lyrics": lyrics}
        return data

    except:
        return {"error": "song can't found"}