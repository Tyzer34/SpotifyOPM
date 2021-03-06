import spotipy
from spotipy import util
import os
import sys
import time
from song import Song

songdict = dict()
spotify = None


def traverse_map_structure(directory):
    global songdict
    print("Listing songs..")
    # Check if directory is valid
    if os.path.isdir(directory):
        # List all maps within the folder
        dir_names = [x[1] for x in os.walk(directory)][0]
        # For each map, list all audio files within the folder as Song objects
        for i in range(len(dir_names)):
            d_path = directory + "/" + dir_names[i]
            songdict[dir_names[i]] = []
            for f in os.listdir(d_path):
                f_path = d_path + "/" + f
                title, artist, album = Song.set_song_attributes(f_path)
                song = Song(title, artist, album)
                if song:
                    songdict[dir_names[i]].append(song)
        print("Song listing has been completed!")
    else:
        print(directory)
        raise ValueError("The directory that was provided isn't valid!")


def make_playlists(username):
    global songdict
    print("Creating playlists..")
    # For each entry in dict, make new playlist
    for pl_name, songs in songdict.items():
        response = spotify.user_playlist_create(username, pl_name, False)
        pl_id = response['id']
        # Search SpotifyID's for each song in array
        song_ids = []
        for song in songs:
            query = "artist:" + song.artist + " track:" + song.title,
            results = spotify.search(query)
            if len(results['tracks']['items']) > 0:
                result = results['tracks']['items'][0]['id']
                song_ids.append(result)
            else:
                print(song.title + " by " + song.artist +
                      " could not be found.")
        # Add songs to playlist
        for chunk in chunk_array(song_ids, 100):
            results = spotify.user_playlist_add_tracks(username, pl_id, chunk)
        print("Playlist " + pl_name + " was successfully created.")
    print("Done!")


def chunk_array(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def build_spotify_playlists():
    username = sys.argv[1]
    path = sys.argv[2]
    global spotify
    scope = 'playlist-modify-public playlist-modify-private'
    token = util.prompt_for_user_token(username, scope, client_id='5824f9dcd6d14d159109d0b0e640b128', client_secret='138b161a99e64268b4c976c9c5e0d27d', redirect_uri="https://github.com/Tyzer34/SpotifyOPM")
    spotify = spotipy.Spotify(auth=token)
    traverse_map_structure(path)
    make_playlists(username)


build_spotify_playlists()
