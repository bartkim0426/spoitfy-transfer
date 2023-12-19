import os
import csv

import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_sp():
    try:
        os.remove('.cache')
    except FileNotFoundError:
        pass
    try:
        ID = os.environ['NEW_ID']
        SECRET = os.environ['NEW_SECRET']
    except KeyError:
        print('Please add env for "NEW_ID" and "NEW_SECRET"')
    os.environ["SPOTIPY_CLIENT_ID"] = ID
    os.environ["SPOTIPY_CLIENT_SECRET"] = SECRET
    os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:5009/api/Spotify'
    scope = 'user-library-read user-library-modify'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


def add_songs(sp):
    with open('songs.csv', newline='') as f:
        reader = csv.reader(f)
        songs_list = list(reader)[0]
    # add saved songs
    LIMIT, OFFSET = 50, 0
    TOTAL = len(songs_list)
    for idx in range(OFFSET, TOTAL, LIMIT):
        print(f'[{idx}:{idx+LIMIT}]')
        sp.current_user_saved_tracks_add(tracks=songs_list[idx:idx+LIMIT])


def add_albums(sp):
    with open('albums.csv', newline='') as f:
        reader = csv.reader(f)
        albums_list = list(reader)[0]
    # add saved albums
    LIMIT, OFFSET = 30, 0
    TOTAL = len(albums_list)
    for idx in range(OFFSET, TOTAL, LIMIT):
        sp.current_user_saved_albums_add(albums=albums_list[idx:idx+LIMIT])


def main():
    sp = get_sp()
    add_songs(sp)
    add_albums(sp)


if __name__ == '__main__':
    main()
