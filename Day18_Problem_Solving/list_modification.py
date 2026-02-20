# %% Problem 1: The Shopping Cart (Adding & Extending)
"""
You are building the backend for an online store. A user starts with a cart, adds a 
high-priority item, and then decides to buy a whole bundle of items.

cart = ["Laptop", "Mouse"]
bundle = ["Monitor", "Keyboard", "Mousepad"]

Your Task:
Use .insert() to put "Charger" at the very front of the cart (index 0).
Use .append() to add "Headphones" to the end of the cart.
Use .extend() to add all the items from the bundle into the cart.
Print the final cart.
"""

cart = ["Laptop", "Mouse"]
bundle = ["Monitor", "Keyboard", "Mousepad"]
cart.insert(0, "Charger")
cart.append("Headphones")
cart.extend(bundle)
print(cart)

# %% Problem 2: The Guest List (Removing)
"""
You are organizing a VIP party, but there are some last-minute changes.

guests = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

Your Task:
"Charlie" can't make it. Use .remove() to take him off the list by his name.

The last person on the list ("Frank") didn't RSVP in time. 
Use .pop() without an index to kick him off the end.

The person at index 1 ("Bob") was accidentally double-booked. 
Use del to remove him by his index.

Print the final guests list.
"""
guests = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
guests.remove("Charlie")
guests.pop()
del guests[1]
print(guests)


# %% Problem 3: The Scoreboard (Updating)
"""
You are tracking live scores for a video game tournament, but need to fix some typos.

scores = [150, 200, 95, 300, 120]

Your Task:
The player at index 2 actually scored 105, not 95. Update their score using standard 
indexing =.
The last player in the list actually scored 125. Update their score using negative 
indexing [-1].
Print the corrected scores list.
"""

scores = [150, 200, 95, 300, 120]
scores[2] = 105
scores[-1] = 125
print(scores)

# %%
