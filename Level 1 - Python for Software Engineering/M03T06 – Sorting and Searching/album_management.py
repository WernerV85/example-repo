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
    Album("Eat me, Drink me", 12, "Marilyn Manson")
    ]

# Printing Album list
for album in albums1:
    print(album)

# Sorting the list according to number of songs
albums1.sort(key=lambda album:album.number_of_songs)
print(f'''\nList of albums with albums 
sorted according to number of songs on the album: ''')
for album in albums1:
    print(album)

# Swapping the first and second albums in the list
albums1[0], albums1[1] = albums1[1], albums1[0]
print(f'''\nList of albums, 
with the first and second albums swapped: ''')
for album in albums1:
    print(album)

# Creating a new list
albums2 = [
    Album("House of Gold & Bones - Part 1", 11, "Stone Sour"),
    Album("Magma", 10, "Gojira"),
    Album("Mer de Noms", 12, "A Perfect Circle"),
    Album("Disclaimer", 12, "Seether"),
    Album("Wilder as die Wildtuin", 14, "Die Heuwels Fantasties")
]

# Printing List 2 of Albums
print(f'''\nThe second list of Albums: ''')
for album in albums2:
    print(album)

# Copying albums from album 1 into album 2
albums2.extend(albums1)
print(f'''\nThe complete list of albums 
from both list: ''')
for album in albums2:
    print(album)

# Adding 2 albums to the list
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyed"))
albums2.append(Album("Oops!.... I Did It Again", 16, "Britney Spears"))

# Sorting the newly created list alphabetically by Album Name          
albums2.sort(key=lambda album:album.album_name)
print(f'''\nThe new list of albums,
with new albums added from list 1 and additional albums,
sorted alphabetically by Album Name: ''')
for album in albums2:
    print(album)

# Searching for an album name and printing the index
search_album = "Dark Side of the Moon"
for index, album in enumerate(albums2):
    if album.album_name == search_album:
        print(f"\nThe album '{search_album}' is  the number {index + 1} album (index {index}) on the list.")
        break   
else:
    print(f"\nThe album '{search_album}' is not found in the list.")


