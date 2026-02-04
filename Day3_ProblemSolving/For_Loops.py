# %% 1. The Genre Announcer (Iteration)
"""Goal: Loop through a collection of items and perform a repeated action.
Task: Use your genres = ['pop', 'hoodtrap', 'jersey club', 'trap'] list from before.
Logic: Write a for loop that iterates through the list and prints: "I produce: [genre]" for every item.
Skill: Understanding the basic syntax of for item in list:."""

genres = ['pop', 'hoodtrap', 'jersey club', 'trap']

for genre in genres:
    print(f"I produce {genre}.")


# %% 2. The Number Doubler (Arithmetic in Loops)
"""Goal: Perform math on every element in a sequence.
Task: Create a list numbers = [1, 2, 3, 4, 5].
Logic: Use a for loop to multiply each number by 2 and print the result.
Skill: Processing data elements one by one."""

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)


# %% 3. The Current Location Searcher (Loop + If)
"""Goal: Combine iteration with decision-making.
Task: Create a list cities = ["Hanoi", "Dalat", "Nha Trang"].
Logic: Loop through the cities. If the city is "Nha Trang", print "I am currently here!". 
Otherwise (else), just print the name of the city.
Skill: Nesting a conditional statement inside a loop."""

cities = ["Hanoi", "Dalat", "Nha Trang"]
for city in cities:
    if city == "Nha Trang":
        print(f"I am in {city}")
    else:
        print(city)

