class Song(object):

    title = ""
    artist = ""
    album = ""

    def __init__(self, file):
        set_song_attributes(file)

    def set_song_attributes(self, file):
        # Read file attributes

        # If title or artist unknown or non existing, check for - in title
        # and extract title and artist from there

        # Set all data values
        self.title = titl
        self.artist = art
        self.album = alb
