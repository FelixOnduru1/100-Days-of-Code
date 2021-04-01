from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os
import pprint

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'


URL = "https://www.billboard.com/charts/hot-100/"
user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
year = user_date.split("-")[0]

response = requests.get(url=f"{URL}{user_date}")
hot_billboard = response.text

soup = BeautifulSoup(hot_billboard, "html.parser")
songs = soup.findAll(name="span", class_="chart-element__information__song text--truncate color--primary")
songs_list = [song.getText() for song in songs]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)
song_uri = []
for song in songs_list:
    try:
        uri = sp.search(q=f"{song}", type="track")["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} wasn't found")

print(song_uri)
name_of_playlist = f"{user_date} Billboard 100"
playlist_id = sp.user_playlist_create(user=user_id,
                                      name=name_of_playlist,
                                      public=False)["id"]

print(playlist_id)

sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
