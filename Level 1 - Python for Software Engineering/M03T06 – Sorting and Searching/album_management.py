# Creating the class Album
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"('{self.album_name}', {self.number_of_songs}, '{self.album_artist}')"
    

    #creating the list of 5 albums
albums1 = [
    Album("Follow the Leader", 14, "Korn"), 
    Album("All Hope is Gone", 28, "Slipknot"),
    Album("Shadow Zone", 13, "Static X"),
    Album("Guitar Gangsters & Cadillac Blood", 14, "Volbeat"),
    Album("Eat me, Drink me", 12, "Marilyn Manson")]

# Printing Album list
for album in albums1:
    print(album)

# Sorting the list according to number of songs
albums1.sort(key=lambda album:album.number_of_songs)
print("\nSorting the albums according to number of songs:")
for album in albums1:
    print(album)

# Swapping the first and second albums in the list
