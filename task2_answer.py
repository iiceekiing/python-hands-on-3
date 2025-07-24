genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

print(genres)

genres.append("Drama")

print(" ")

print(genres)

unique = genres.remove("Fantasy")

print(genres)

numbers_of_genres = len(genres)

print(f"\nthe numbers of genres planned for the even is: ", numbers_of_genres)

print(f"\nthe second genres to be played is: ", genres[1])

print(f"\nThe second to the last genres to be played is: ", genres[-2])
