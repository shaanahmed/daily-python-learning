# %% Problem 1: The Safe Lookup (get)
"""
Use .get("bio", "No bio provided") to safely check 
user_profile = {"username": "coder_kid", "email": "coder@email.com"} without crashing. 
Print the result.
"""
user_profile = {"username": "coder_kid", "email": "coder@email.com"}
print(user_profile.get("bio", "No bio provided"))


# %% Problem 2: The Data Merger (Logic)
"""
You have 
inventory = {"gold": 150, "potions": 2} 
loot_drop = {"gold": 50, "magic_scroll": 1}
Write a for key, value in loot_drop.items(): loop. 
If the key is in inventory, add the value. If not, create it. Print the final inventory!
"""
inventory = {"gold": 150, "potions": 2} 
loot_drop = {"gold": 50, "magic_scroll": 1}

for key, value in loot_drop.items():
    if key in inventory:
        inventory[key] += value
    else:
        inventory[key] = value

print(inventory)


# %% Problem 3: The Inflation Hiker (Dict Comprehension)
"""
Write a one-line dictionary comprehension to multiply every value in 
old_prices = {"laptop": 1000, "mouse": 25} by 1.20. 
(Hint: {k: v * 1.20 for k, v in old_prices.items()}). Print the new dictionary.
"""
old_prices = {"laptop": 1000, "mouse": 25, "monitor": 200}
print({key : value * 1.20 for key, value in old_prices.items()})


# %% Problem 4: The Nested Access (Deep Dive)
"""
In the real world, data comes in layers.

users = {
    "user1": {"name": "Alice", "skills": ["Python", "Git"]},
    "user2": {"name": "Bob", "skills": ["Java", "Docker"]}
}
Your Task: Write a single line of code to print Bob's second skill ("Docker").

"""
users = {
    "user1": {"name": "Alice", "skills": ["Python", "Git"]},
    "user2": {"name": "Bob", "skills": ["Java", "Docker"]}
}
print(users["user2"]["skills"][1])


# %% Problem 5: The Frequency Counter (The Classic)
"""
This pattern is used everywhere from counting words in a book to tracking website traffic.

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
count_dict = {}

# Your Task: Use a for loop and .get() to populate count_dict
"""

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
count_dict = {}

for i in votes:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print(count_dict)


# %% Problem 6: The Conditional Filter
"""
grades = {"Alice": 95, "Bob": 62, "Charlie": 88, "David": 50}

Your Task: Use comprehension + an 'if' to get students >= 70
"""

grades = {"Alice": 95, "Bob": 62, "Charlie": 88, "David": 50}
print({name : marks for name, marks in grades.items() if marks >= 70})


# %% Problem 7: The Key-Value Swap
"""
id_to_name = {101: "Alice", 102: "Bob", 103: "Charlie"}
Your Task: Flip them! {name: id}
"""

id_to_name = {101: "Alice", 102: "Bob", 103: "Charlie"}

name_to_id = {val : ke for ke, val in id_to_name.items()}
print(name_to_id)


# %% Problem 8: The .setdefault() Secret
"""
This is how you avoid KeyErrors when appending to lists inside a dictionary.

weekly_tasks = {"Monday": ["Gym"]}

Your Task: Use .setdefault("Tuesday", []).append("Coding") 
and see how it handles the missing key automatically!
"""

weekly_tasks = {"Monday": ["Gym"]}
weekly_tasks.setdefault("Tuesday", []).append("Coding")
print(weekly_tasks)

# %%
