echo "Welcome to SpotifyOPM!"
echo "This program will traverse your offline music library"
echo "and convert them to Spotify playlists."
echo "Please follow the instructions if given in the terminal."
echo ""
echo "What is your Spotify username?"
read -p "" username
echo "What folder do you wish to traverse?"
read -p "" path
python spotifyopm/spotifyopm.py $username $path
