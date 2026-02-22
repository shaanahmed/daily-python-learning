# %% Problem 1: The Shouty List (Replacing map)
"""
You have a list of words, and you need them all to be fully uppercase.

words = ["hello", "world", "python", "code"]

Write a list comprehension that loops through words and applies .upper() to each word. 
Assign it to a variable called shouty_words and print it. (Hint: [word.upper() for ...])
"""
words = ["hello", "world", "python", "code"]
shouty_words = [word.upper() for word in words]
print(shouty_words)


# %% Problem 2: The Evens Only (Replacing filter)
"""
You have a list of numbers, and you only want to extract the even ones.

numbers = [12, 15, 18, 21, 24]

Write a list comprehension that loops through numbers but only keeps the item 
if num % 2 == 0. Assign it to even_numbers and print it.
"""

numbers = [12, 15, 18, 21, 24]
print(list(num for num in numbers if num % 2 == 0))


# %% Problem 3: The Premium Tax (Combining map and filter)
"""
You need to apply a 10% tax (multiply by 1.10), but only to luxury items that cost more 
than $100. If it is $100 or less, ignore it entirely.

prices = [45.0, 120.0, 8.50, 350.0, 99.99]

Your Task:
Write a list comprehension that multiplies the price by 1.10, loops through the prices 
list, and filters for items strictly > 100. Print the final list.
"""

prices = [45.0, 120.0, 8.50, 350.0, 99.99]
print(list(p * 1.10 for p in prices if p > 100))


# %% Problem 4: The Shortest to Longest (sorted + len)
"""
You have a list of random words. You need a new list where all the words are capitalized 
(.title()), but you want them ordered from the shortest word to the longest word.

words = ["strawberry", "fig", "apple", "banana", "kiwi"]

Your Task:
Write a list comprehension that loops through sorted(words, key=len). For each word, apply 
.title(). Print the final list. (Output should start with 'Fig' and end with 'Strawberry').
"""

words = ["strawberry", "fig", "apple", "banana", "kiwi"]
print([word.title() for word in sorted(words, key = len)])


# %% Problem 5: The Podiums (sorted + lambda)
"""
You have race results as a list of tuples: (Runner Name, Time in minutes). You want to 
extract just the names of the runners, ordered from fastest (lowest time) to slowest.

race_results = [("Alice", 25.5), ("Bob", 19.8), ("Charlie", 22.1)]

Your Task:
Write a list comprehension that loops through sorted(race_results, key=lambda x: x[1]). 
Extract just the name (index 0) of each runner. Print the list of names.
"""
race_results = [("Alice", 25.5), ("Bob", 19.8), ("Charlie", 22.1)]
print([runner[0] for runner in sorted(race_results, key = lambda x : x[1])])


# %% Problem 3: The Ultimate Combo (Sort + Filter + Extract)
"""
You have a list of store inventory: (Item, Price).

inventory = [("Laptop", 1200), ("Mouse", 25), ("Monitor", 300), ("Keyboard", 150), ("Cable", 15)]

Your Task:
Write a single list comprehension that does all of this at once:

Loops through sorted(inventory, key=lambda x: x[1]) (sorting from cheapest to most expensive).

Adds an if condition at the very end of the comprehension to only keep the item if the 
price (index 1) is strictly > 50.

Extracts just the name (index 0) at the very beginning of the comprehension.
"""

inventory = [("Laptop", 1200), ("Mouse", 25), ("Monitor", 300), ("Keyboard", 150), ("Cable", 15)]
print(list(item[0] for item in sorted(inventory, key = lambda x : x[1]) if item[1] > 50))


# %%
