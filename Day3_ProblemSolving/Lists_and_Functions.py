# %% 1. The Artist Tool (len & Indexes)
"""Task: Create a list called genres with 4 types of music you produce.
Logic: Print the total number of genres using len().
Print the first genre using genres[0].
Print the last genre using genres[-1]."""

genres = ['pop','hoodtrap','jersey club','trap']
print(len(genres))
print(genres[0])
print(genres[-1])


# %% 2. The Score Stats (max & min)
"""Task: Create a list of 5 numbers called exam_scores = [85, 92, 78, 90, 88].
Logic: Print the highest score using max().
Print the lowest score using min()."""

exam_scores = [85, 92, 78, 90, 88]
print(max(exam_scores))
print(min(exam_scores))


# %% 3. List Mutability
"""Task: Start with travel_cities = ["Ho Chi Minh", "Dalat"].
Logic: Add "Nha Trang" to the list using .append("Nha Trang").
Change the first city to "Hanoi" using travel_cities[0] = "Hanoi".
Print the final list."""

travel_cities = ["Ho Chi Minh", "Dalat"]
travel_cities.append("Nha Trang")
travel_cities[0] = "Hanoi"
print(travel_cities)



