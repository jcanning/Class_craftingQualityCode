import song

class Playlist:
    """ A playlist of songs."""

    def __init__(self, title):
        """ (Playlist, str) -> NoneType

        A playlist of songs titled title.

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.title
        'Canadian Artists'
        >>> playlist.songs
        []
        """

        self.title = title
        self.songs = []

    def add(self, song):
        """ (Playlist, song) -> NoneType

        Add song to this playlist.

        >>> stompa = song.Song('Our Lady Peace', '4 AM', 3, 15)
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add('4 am')
        >>> playlist.songs[0] == '4 am'
        True
        """

        self.songs.append(song)

    def get_duration(self):
        """ (Playlist) -> tuple of (int, int)

        Return the duration of this playlist as a tuple of minutes and seconds.

        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Our Lady Peace', '4 AM', 3, 15))
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3)
        >>> playlist.get_duration()
        (8, 18)
        """

        total_minutes = 0
        total_seconds = 0

        for song in self.songs:
            total_minutes = total_minutes + song.minutes
            total_seconds = total_seconds + song.seconds

        return (total_minutes + total_seconds // 60, total_seconds % 60)

    def __str__(self):
        """ (Playlist) -> str

        Return a string representation of this playlist.
        
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Our Lady Peace', '4 AM', 3, 15))
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3)
        >>> str(playlist)
        ''' Canadian Artists (8:18)
        1. Our Lady Peace, 4 AM (3:15)
        2. Neil Young, Harvest Moon (5:03)'''
        """

        duration = self.get_duration()
        minutes = str(duration[0])
        seconds = str(duration[1]).rjust(2, '0')

        result = self.title + ' (' + minutes + ':' + seconds + ')'

        song_num = 1
        for song in self.songs:
            result = result + '\n' + str(song_num) + '. ' + str(song)
            song_num = song_num + 1

        return result

if __name__ == '__main__':
    playlist = Playlist('Canadian Artists')
    playlist.add(song.Song('Our Lady Peace', '4 AM', 3, 15))
    playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
    playlist.add(song.Song("Stompin' Tom Connors", "The Hockey Song", 2, 17))

    print(playlist)
