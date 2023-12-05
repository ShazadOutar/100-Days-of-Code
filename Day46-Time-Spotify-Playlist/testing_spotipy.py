import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os

# auth_manager = SpotifyClientCredentials(client_id=os.environ["ClientID"], client_secret=os.environ["ClientSecret"])
# sp = spotipy.Spotify(auth_manager=auth_manager)
# results = sp.current_user_saved_tracks()
# print(results)

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URL = os.environ["SPOTIPY_REDIRECT_URI"]

# print(f"{CLIENT_ID}\n{CLIENT_SECRET}\n{REDIRECT_URL}")
# scope = "user-library-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# results = sp.current_user_saved_tracks()
# print(results)

# TODO: Fix this so it works properly, it's giving a service not found error
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.user_playlist_create(user=sp.current_user(), name="100 Days of Code",
                                  public=False, collaborative=False, description="")
print(results)