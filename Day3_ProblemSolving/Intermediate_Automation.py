# %% 1. The Target Search (Break Keyword)
"""Goal: Stop a loop once a specific condition is met to save processing power.
Task: Create a list inventory = ["Apple", "Banana", "Orange", "Target", "Grapes"].
Logic: Loop through the list. Print each item. If you encounter "Target", print "Found it!" and use the break keyword to stop the loop immediately.
Challenge: Observe that "Grapes" is never printed because the loop "broke" early."""

inventory = ["Apple", "Banana", "Orange", "Target", "Grapes"]
for items in inventory:
    print(items)
    if items == "Target":
        print("Found it!")
        break


# %% 2. The Index Hunter (range(len()))
""" Goal: Access both the item and its position in the list.
Task: Create a list tasks = ["Email", "Code", "Music"].
Logic: Use for i in range(len(tasks)): to loop.
Print: "Task #[i+1]: [tasks[i]]".
Skill: Using the index i to create a numbered list."""

tasks = ["Email", "Code", "Music"]
for i in range(len(tasks)):
    print(f"{i+1} : {tasks[i]}")

# %% 3. The Maximum Finder (Manual Logic)
"""Goal: Find the largest number in a list without using the max() function.
Task: numbers = [12, 45, 2, 99, 31].
Logic: Create a variable highest = numbers[0]. Loop through the rest of the numbers. 
If the current number is greater than highest, update highest to be that number.
Skill: Implementing an algorithm manually—this is how the max() function actually works under the hood!"""

numbers = [12, 45, 2, 99, 31]
highest = numbers[0]
for i in numbers:
    if i > highest:
        highest = i
print(highest)
# %%
