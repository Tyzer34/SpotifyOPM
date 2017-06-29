# SpotifyOPM

Spotify Offline Playlist Maker! Convert your offline music library to high quality Spotify playlists!

## Usage

To use the application, simply install the given requirements by using
```
pip intall -r requirements.txt
```

Next, run the application using _run.sh_ and follow the instructions on the terminal.

Alternatively, you can run the script directly using
```
python spotifyopm/spotifyopm.py $username $path
```
where you replace $username with your Spotify username and $path with the path to your offline music library.

## Structure

SpotifyOPM requires your music library to be organised as follows:

The path to the library you supply, must correspond to a main folder, containing multiple subfolders. The names of these subfolders will be taken as names for the playlists. Each and every one of these subfolders should contain the music that you want to be present in this playlist.

## Support

At the moment, SpotifyOPM supports _mp3_, _flac_, _wma_, _m4a_.

This project was made as a quick workaround, but can surely be used by anyone who wants to try this out!
