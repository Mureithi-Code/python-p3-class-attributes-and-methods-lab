class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update all relevant data
        self.add_to_count()
        self.update_list_and_count(Song.genres, genre)
        self.update_list_and_count(Song.artists, artist)
        self.update_count(Song.genre_count, genre)
        self.update_count(Song.artist_count, artist)

    @classmethod
    def add_to_count(cls):
        """Increment total song count."""
        cls.count += 1

    @classmethod
    def update_list_and_count(cls, collection, item):
        """Updates both a list (if item not already present) and dictionary (for counting)."""
        if item not in collection:
            collection.append(item)

    @classmethod
    def update_count(cls, count_dict, item):
        """Updates the count of an item in the dictionary."""
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
