# %% Problem 1: The Reference Trap (=)
"""
You are managing a restaurant menu. You want to create a special weekend menu based on the 
weekday menu, but you accidentally use the = sign.

weekday_menu = ["Burger", "Salad", "Steak"]
weekend_menu = weekday_menu

# The chef swaps the Steak for Lobster on the weekend
weekend_menu[2] = "Lobster"

Your Task:
Print weekday_menu. Notice how the Steak was destroyed on the weekday menu too!
Fix the code. Change weekend_menu = weekday_menu to use the .copy() method so the 
weekday_menu stays safe.
Print both lists to prove they are now independent.
"""
weekday_menu = ["Burger", "Salad", "Steak"]
weekend_menu = weekday_menu.copy()
weekend_menu[2] = "Lobster"
print(weekday_menu)
print(weekend_menu)

# %% Problem 2: The Backup Roster ([:])
"""
You are about to make some risky changes to a team roster, so you want to make a quick back
up using slicing.

team = ["Alice", "Bob", "Charlie", "Diana"]

Your Task:
Create a variable called team_backup and use slicing ([:]) to copy the team list.
.pop() the last person off the original team list.
Print team_backup to prove your backup still has all four original members!
"""
team = ["Alice", "Bob", "Charlie", "Diana"]
team_backup = team[:]
print(team.pop())
print(team_backup)

# %% Problem 3: The Inception Problem (deepcopy)
"""
Shallow copies only copy the first level of a list. If you have a list inside a list, a 
shallow copy will still link those inner lists together! You need a deep copy.


import copy
vault = ["Gold", "Silver", ["Ruby", "Diamond"]]

Your Task:
Create a variable called fake_vault and assign it a copy.deepcopy(vault).
A thief steals the "Diamond" from the fake_vault by changing fake_vault[2][1] = "Glass".
Print the original vault to prove that your real Diamond is still perfectly safe inside 
the nested list!
"""
import copy

vault = ["Gold", "Silver", ["Ruby", "Diamond"]]
fake_vault = copy.deepcopy(vault)
fake_vault[2][1] = "Glass"
print(vault[2][1] is fake_vault[2][1])
print(vault) 

# %%
