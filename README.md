# Spotify transfer


## How To

1. prepare accounts

2. Make applications

https://github.com/JustSxm/SpotifyMigrator

3. Prepare client id, secret

4. Set env for 2 accounts

```
export OLD_ID=''
export OLD_SECRET=''
export NEW_ID=''
export NEW_SECRET=''
```

5. Log in old spotify account in default web brwoser (That want to move songs, albums from)

6. execute download.py

before, need to install spotipy

```
pip install -r requirements.txt
python download.py
# have to authenticate from browser
```

After download, you can see `songs.csv` and `albums.csv`

7. Log in new spotify account in default web brwoser (That want to move songs, albums into)

8. execute transfer.py


## Todo

- [ ] add saved playlist
- [ ] add saved podcasts
- [ ] automation for authentication if possible
