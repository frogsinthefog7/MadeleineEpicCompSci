
class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:

    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def add_song(self, song):

        self.songs.append(song)

    def get_total_duration(self):

        total_length = 0
        
        for i in self.songs:
            total_length += int(i.duration)

        total_length = str(round(total_length / 60, 2)).split(".")
        total_length[-1] = int(total_length[-1])
        total_length[-1] = round(total_length[-1] * .6)
        total_length[-1] = str(total_length[-1])

        total_length = ":".join(total_length)

        print("")
        print(f"Total Duration of Playlist is: {total_length}")


    def find_by_artist(self, artist_name):

        total_songs_by_artist = 0

        for i in self.songs:

            if i.artist == artist_name:
                total_songs_by_artist += 1

        if total_songs_by_artist == 0:
            print(f"THERE ARE NO SONGS BY {artist_name.upper()}")
            return

        print("")
        print(f"SONGS BY {artist_name.upper()}")
        print("----------------------------")

        for i in self.songs:

            if i.artist == artist_name:
                print(f"{i.title} by {i.artist}")

    def print_playlist(self):

        print(self.name.upper())
        print("----------------------------")

        for i in self.songs:
            print(f"{i.title}, {i.artist}")

    def load_songs(self, filename):

        with open(filename, "r") as f:
            playlist = f.readlines()

        for i in playlist[1:]:
            t, a, d = i.split(",")
            i = Song(t, a, d)
            self.songs.append(i)

def main():

    playlist = Playlist("My Playlist", [])
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")

if __name__ == '__main__':
    main()