from bs4 import BeautifulSoup
import requests
from requests import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from spotipy import SpotifyException

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URL = os.environ["SPOTIPY_REDIRECT_URI"]
SPOTIFY_USERNAME = os.environ["Spotify_Username"]


def get_date():
    # TODO: make this an input later
    input_date = input("Which date to use? Please enter a date in the format YYYY-MM-DD:\t")
    # input_date = "2022-11-19"
    return input_date


def get_top_100_at_date(input_date: str) -> list:
    try:
        # Use requests to get the page content
        response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{input_date}")
        response.raise_for_status()
        print(f"Response code is: {response.status_code}")
        billboard_site = response.text
        # parse the html data returned
        soup = BeautifulSoup(billboard_site, "html.parser")

        song_tags = soup.find_all(name="div", class_="o-chart-results-list-row-container")
        # print(len(song_tags))
        song_names = [song.find_all(name="li")[3].find(name="h3").getText().strip() for song in song_tags]
        print(f"{len(song_names)} in songs_list")
        return song_names

    except (AttributeError, HTTPError):
        print("Please enter another date")
        input_date = get_date()
        get_top_100_at_date(input_date)


def get_user_id(my_spotipy):
    user_id = my_spotipy.current_user()["id"]
    return user_id


def create_playlist(my_spotipy, user_id, name="100 Days of Code", description="From Day 46 in 100 Days of Code"):
    my_spotipy.user_playlist_create(user=user_id,
                                    name=name,
                                    public=False,
                                    description=description)


def get_most_recent_playlist(my_spotipy):
    date_playlist = my_spotipy.current_user_playlists()["items"][0]["id"]
    return date_playlist


def get_track_ids(my_spotipy, songs: list) -> list:
    """
    Convert each song from its name to its spotify id value
    """
    song_ids = []
    count = 0
    # print(my_spotipy.search(q="", type="track")["tracks"]["items"][0]["id"])
    for song in songs:
        try:
            track_id = my_spotipy.search(q=song, type="track")["tracks"]["items"][0]["id"]
            print(f"{count}) {track_id}")
            song_ids.append(track_id)
            count += 1
        except SpotifyException:
            # If the name pulled was empty
            # song_ids.append("")
            print(f"No name found")
            pass
    return song_ids


def add_songs(my_spotipy, user_id, playlist_id, songs: list):
    my_spotipy.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=songs)


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
    create_playlist(sp, user_id=user_id, name=f"Top 100 song in the week of {input_date}")

    # after creating the playlist, get its id to reference later
    top_100_at_date_playlist = get_most_recent_playlist(sp)
    top_100_tracks_ids = get_track_ids(sp, songs_list)
    add_songs(my_spotipy=sp, user_id=user_id, playlist_id=top_100_at_date_playlist, songs=top_100_tracks_ids)


if __name__ == "__main__":
    main()
