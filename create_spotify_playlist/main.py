import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
REDIRECT_URL = "http://example.com"

input_date = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
year = input_date.split("-")[0]

response = requests.get(f"{URL}/{input_date}")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

song_title_tags = soup.find_all(name="span", class_="chart-element__information__song")
song_titles = [tag.getText() for tag in song_title_tags]
print(song_titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()['id']
print(user_id)

song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

