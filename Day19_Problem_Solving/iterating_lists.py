# %% Problem 1: The Leaderboard (enumerate)

"""
You have a list of race winners in order. You want to print them out with their placement 
number.

winners = ["Usain", "Tyson", "Yohan"]

Your Task:
Use enumerate() on the winners list, wrap it in list(), and print it.
(Bonus: Try adding a second argument to enumerate like this: enumerate(winners, start=1) 
to make the numbering start at 1 instead of 0!)
"""

winners = ["Usain", "Tyson", "Yohan"]
for position, name in enumerate(winners, start = 1):
    print(f"{position}. {name}")

# %% Problem 2: The Character Counter (map)
"""
You want to know exactly how many letters are in each password in a list. The built-in len() 
function calculates the length of a single string.

passwords = ["admin", "password123", "qwerty"]

Your Task:
Use map() to apply the len function to the passwords list. Wrap it in list() and print it. 
(You should see [5, 11, 6]).
"""

passwords = ["admin", "password123", "qwerty"]
for i in map(len, passwords):
    print(i)

#Another way if you want to print a list
print(list(map(len, passwords)))


# %% Problem 3: The Bouncer (filter)
"""
You have a list of ages, and a pre-written helper function that checks if someone is 18 or 
older.

ages = [16, 21, 17, 30, 14, 18]

# A simple function that returns True if age >= 18
def is_adult(age):
    return age >= 18

Your Task:
Use filter() to pass the is_adult function and the ages list. Wrap it in list() and 
print the result. It should kick out everyone under 18!
"""

ages = [16, 21, 17, 30, 14, 18]

def is_adult(age):
    return age >= 18

for i in filter(is_adult, ages):
    print(i)

#If want to print in a list
print(list(filter(is_adult, ages)))

# %%
