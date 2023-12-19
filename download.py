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
        ID = os.environ['OLD_ID']
        SECRET = os.environ['OLD_SECRET']
    except KeyError:
        print('Please add env for "OLD_ID" and "OLD_SECRET"')
    os.environ["SPOTIPY_CLIENT_ID"] = ID
    os.environ["SPOTIPY_CLIENT_SECRET"] = SECRET
    os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:5009/api/Spotify'
    scope = 'user-library-read user-library-modify'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp


def get_songs(sp):
    OFFSET, LIMIT = 0, 50
    results = sp.current_user_saved_tracks(LIMIT, OFFSET)
    TOTAL = results['total']
    # id: song['track']['id']
    total_songs = []
    for idx in range(OFFSET, TOTAL, LIMIT):
        results = sp.current_user_saved_tracks(LIMIT, idx)
        songs = results['items']
        # save only id
        total_songs.extend([
            song['track']['id'] for song in songs
        ])
    # write file into csv
    with open('songs.csv', 'w', newline='') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(total_songs)


def get_albums(sp):
    OFFSET, LIMIT = 0, 50
    albums = sp.current_user_saved_albums(LIMIT, OFFSET)
    TOTAL = albums['total']
    total_albums = []
    for idx in range(OFFSET, TOTAL, LIMIT):
        results = sp.current_user_saved_albums(LIMIT, idx)
        albums = results['items']
        total_albums.extend([
            album['album']['id'] for album in albums
        ])

    # write file into csv
    with open('albums.csv', 'w', newline='') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(total_albums)


def main():
    sp = get_sp()
    get_songs(sp)
    get_albums(sp)


if __name__ == '__main__':
    main()
