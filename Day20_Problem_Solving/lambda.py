# %% Problem 1: The Quick Math (map + lambda)
"""
You need to calculate the square of a list of numbers (number multiplied by itself).

numbers = [2, 4, 6, 8]

Your Task:
Use map() with a lambda function that takes an input x and returns x ** 2.
Wrap it in list() and print the result. (You should see [4, 16, 36, 64]).
"""
numbers = [2, 4, 6, 8]
num = list(map(lambda x : x ** 2, numbers))
print(num)


# %% Problem 2: The "A" List (filter + lambda)
"""
You have a guest list, but you only want to send invitations to people whose names start 
with the letter "A".


guests = ["Alice", "Bob", "Amanda", "Charlie", "Adam"]

Your Task:
Use filter() with a lambda function that takes a name x and checks if x[0] == "A".
Wrap it in list() and print the result!
"""
guests = ["Alice", "Bob", "Amanda", "Charlie", "Adam", "anil"]
print(list(filter(lambda x : x.lower().startswith("a"), guests)))

# %%  Problem 3: The Inventory Manager (sorted + key)
"""
You have a list of tuples representing your warehouse inventory: (Item Name, Quantity in Stock). 
You want to find out what you are running out of by sorting the list from the lowest 
quantity to the highest.

inventory = [("Laptops", 15), ("Mice", 2), ("Keyboards", 45), ("Monitors", 8)]

Use sorted() and pass the key=lambda x: x[1] argument to tell Python to sort based on the 
second item in each tuple (the quantity). Print the sorted inventory.
"""

inventory = [("Laptops", 15), ("Mice", 2), ("Keyboards", 45), ("Monitors", 8)]
print(sorted(inventory, key = lambda x : x[1]))


# %%
