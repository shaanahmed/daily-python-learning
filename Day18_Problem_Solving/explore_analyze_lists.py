# %% Problem 1: The Quick Audit
"""The Setup:
Copy and paste this list of daily step counts (from a fitness tracker) over a two-week 
period into your editor:

steps = [8500, 10200, 7800, 10200, 12050, 9300, 10200, 15000, 4200, 11500, 10200, 8900, 13400, 9900]

Your fitness app needs to show your user their basic stats for the last two weeks. 
Write code to calculate and print:

The lowest number of steps they took (min).
The highest number of steps they took (max).
The total number of steps they took over the whole two weeks (sum).
Their average daily steps (Hint: Divide the total sum by the length of the list!).

"""
steps = [8500, 10200, 7800, 10200, 12050, 9300, 10200, 15000, 4200, 11500, 10200, 8900, 13400, 9900]
print(
    f"The lowest number of steps you took: {min(steps)}\n"
    f"The highest number of steps you took: {max(steps)}\n"
    f"The total number of steps you took over the whole two weeks: {sum(steps)}\n"
    f"Your average daily steps: {sum(steps)/len(steps)}"
)

# %% Problem 2: The 10k Milestone
"""
The app wants to know about the user's "perfect" 10,200 step days.
Use the in operator to print a boolean (True or False) checking if 10200 is in the list.
If it is, use .count() to print exactly how many times the user hit exactly 10200 steps.
Use .index() to find out what day (index) they first hit 10200 steps.
"""
steps = [8500, 10200, 7800, 10200, 12050, 9300, 10200, 15000, 4200, 11500, 10200, 8900, 13400, 9900]
print(10200 in steps)
print(steps.count(10200))
print(steps.index(10200))

# %% Problem 3: Finding the Median
"""
Sometimes averages are skewed by one really lazy day (like that 4200!). 
Let's find the median (the middle number when sorted).

Create a new variable called sorted_steps using the sorted() function.
Find the middle index by dividing the length of the list by 2 using integer division (len(steps) // 2).
Print the step count located at that middle index in your sorted_steps list!
"""

steps = [8500, 10200, 7800, 10200, 12050, 9300, 10200, 15000, 4200, 11500, 10200, 8900, 13400, 9900]

sorted_steps = sorted(steps)
middle_index = len(sorted_steps) // 2
print(sorted_steps[middle_index])

# %% Problem 4: Server Health (all and any)
"""
You are monitoring a network of servers. 1 means online, and 0 means offline.

main_servers = [1, 1, 1, 1, 1]
database_nodes = [1, 1, 0, 1]
backup_cluster = [0, 0, 0, 0]

Your Task:
Use all() to print whether the main_servers are all perfectly online.
Use all() to check if the database_nodes are all online (this should evaluate to False because of the 0).
Use any() to check if there is at least some sign of life in the backup_cluster.
"""
main_servers = [1, 1, 1, 1, 1]
database_nodes = [1, 1, 0, 1]
backup_cluster = [0, 0, 0, 0]

print(all(main_servers))
print(all(database_nodes))
print(all(backup_cluster))

# %% Problem 5: The Identity Trap (== vs is)
"""
This is a classic Python interview question!

list_a = [10, 20, 30]
list_b = [10, 20, 30]
list_c = list_a

Your Task:
Write code to print the answers to these three questions and see how Python behaves behind the scenes:

Does list_a == list_b? (Do they have the same values?)
Does list_a is list_b? (Are they the exact same object in memory?)
Does list_a is list_c?
"""
list_a = [10, 20, 30]
list_b = [10, 20, 30]
list_c = list_a

print(list_a == list_b)
print(list_a is list_b)  # no its not the same because its a different object in different memory space
print(list_a is list_c)   # it will be true

# %% Problem 6: Software Versions (>)
"""
Comparing lists with > is incredibly useful for checking software version numbers, 
because Python compares them item-by-item from left to right (Major, Minor, Patch).

current_version = [2, 1, 5]
update_v1 = [2, 1, 9]
update_v2 = [2, 2, 0]

Your Task:
Write two print() statements using the > operator to ask Python:
Is update_v1 strictly greater than current_version?
Is update_v2 strictly greater than update_v1?
"""
current_version = [2, 1, 5]
update_v1 = [2, 1, 9]
update_v2 = [2, 2, 0]

print(current_version < update_v1)
print(update_v1 < update_v2)

# %%
