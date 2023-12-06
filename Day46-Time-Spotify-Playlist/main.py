from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URL = os.environ["SPOTIPY_REDIRECT_URI"]
SPOTIFY_USERNAME = os.environ["Spotify_Username"]


def get_date():
    # TODO: make this an input later
    # input_date = input("Which date to use? Please enter a date in the format YYYY-MM-DD")
    input_date = "2022-11-19"
    return input_date


def get_top_100_at_date(input_date: str) -> list:
    # Use requests to get the page content
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{input_date}")
    billboard_site = response.text

    # parse the html data returned
    soup = BeautifulSoup(billboard_site, "html.parser")

    song_tags = soup.find_all(name="div", class_="o-chart-results-list-row-container")
    # print(len(song_tags))
    song_names = [song.find_all(name="li")[3].find(name="h3").getText().strip() for song in song_tags]
    print(f"{len(song_names)} in songs_list")
    return song_names


def get_user_id(my_spotipy):
    user_id = my_spotipy.current_user()["id"]
    return user_id


def create_playlist(my_spotipy, user_id, name="100 Days of Code", description="Day 46 First Try"):
    my_spotipy.user_playlist_create(user=user_id,
                                    name=name,
                                    public=False,
                                    description=description)


def main():
    # handle the date and getting the songs from the top 100
    input_date = get_date()
    songs_list = get_top_100_at_date(input_date=input_date)
    print(songs_list)

    # handle making the playlist and adding the songs
    # Connect with spotipy to authorize with Spotify
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

    user_id = get_user_id(sp)
    create_playlist(sp, user_id=user_id)

    # after creating the playlist, get its id to reference later
    # TODO: Add to the playlist next

if __name__ == "__main__":
    main()
