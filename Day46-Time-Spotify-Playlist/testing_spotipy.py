import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# auth_manager = SpotifyClientCredentials(client_id=os.environ["ClientID"], client_secret=os.environ["ClientSecret"])
# sp = spotipy.Spotify(auth_manager=auth_manager)
# results = sp.current_user_saved_tracks()
# print(results)

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URL = os.environ["SPOTIPY_REDIRECT_URI"]
SPOTIFY_USERNAME = os.environ["Spotify_Username"]
# print(f"{CLIENT_ID}\n{CLIENT_SECRET}\n{REDIRECT_URL}")
# scope = "user-library-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# results = sp.current_user_saved_tracks()
# print(results)

scope = "playlist-modify-private playlist-read-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=REDIRECT_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="ShazadOutar"
    )
)

user_id = sp.current_user()["id"]
print(user_id)


# print(sp.me()["id"])


def create_playlist():
    sp.user_playlist_create(user=user_id,
                            name="100 Days of Code",
                            public=False,
                            description="Day 46 First Try")


# create_playlist()
playlists = sp.current_user_playlists()
print(playlists)
date_playlist = playlists["items"][0]
print(date_playlist)
date_playlist_id = date_playlist["id"]
print(date_playlist_id)


def get_track_id(song_name) -> str:
    track = sp.search(q=song_name, type="track")["tracks"]["items"][0]["id"]
    print(track)
    return track


def get_track_ids(songs_list) -> list:
    song_ids = []
    for song in songs_list:
        track_id = sp.search(q=song, type="track")["tracks"]["items"][0]["id"]
        print(track_id)
        song_ids.append(track_id)
    return song_ids


# get_track_ids(tracks)
# print(get_track_ids(tracks))

def add_track(track_ids):
    # sp.user_playlist_add_tracks(user=user_id, playlist_id=date_playlist_id, )
    pass
