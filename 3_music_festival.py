artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

unique_artists = set()

for artist in artist_names:
    unique_artists.add(artist)

# dupe check
duplicates_found = len(artist_names) != len(unique_artists)

print("Unique Names:", unique_artists)

print("Duplicate Names Found:", duplicates_found)

