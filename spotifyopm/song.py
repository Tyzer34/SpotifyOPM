from mutagen import easyid3, asf, flac, mp4
import warnings


class Song(object):

    title = ""
    artist = ""
    album = ""

    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __new__(cls, title, artist, album):
        if title is None and artist is None:
            return None
        return super(Song, cls).__new__(cls)

    def __repr__(self):
        if self.album != "":
            return self.title + " by " + self.artist + \
             " from the album " + self.album
        else:
            return self.title + " by " + self.artist

    @staticmethod
    def set_song_attributes(f):
        # Try to read file attributes
        try:
            if f.endswith(".mp3"):
                audio = easyid3.EasyID3(f)
                title = audio['title'][0]
                artist = audio['artist'][0]
                album = audio['album'][0]
            elif f.endswith(".wma"):
                audio = asf.ASF(f)
                title = str(audio.tags['Title'][0])
                artist = str(audio.tags['Author'][0])
                album = str(audio.tags['WM/AlbumTitle'][0])
            elif f.endswith(".flac"):
                audio = flac.FLAC(f)
                title = audio.tags['TITLE'][0]
                artist = audio.tags['ARTIST'][0]
                album = audio.tags['ALBUM'][0]
            elif f.endswith(".m4a"):
                audio = mp4.MP4(f)
                title = audio.tags['\xa9nam'][0]
                artist = audio.tags['\xa9ART'][0]
                album = audio.tags['\xa9alb'][0]
            else:
                warnings.warn("The following file is not supported: " + f)
            # Return all data values
            return title, artist, album
        # If title or artist unknown or non existing, check for - in title
        # and extract title and artist from there
        except KeyError:
            if '-' in f:
                tupl = f.split(' - ')
                title = tupl[0]
                artist = tupl[1]
                album = ""
                return title, artist, album
            else:
                warnings.warn("Could not extract information from the " +
                              "following file: " + f)
                return None, None, None
