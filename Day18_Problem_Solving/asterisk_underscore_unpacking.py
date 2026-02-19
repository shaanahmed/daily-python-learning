# %% Problem 1: The Throwaway Sandwich
"""
You are processing a data log from a weather sensor. It outputs a list where the first 
item is the start temperature, the last item is the end temperature, and everything in 
between is just noisy data you don't care about.

sensor_data = [65.2, 66.1, 66.5, 67.0, 68.2, 69.1, 70.5]

Your Task: Write a single line of unpacking code that assigns the first number to a 
variable called start_temp, the last number to a variable called end_temp, and uses the 
* and _ conventions to explicitly ignore all the middle numbers.
"""
sensor_data = [65.2, 66.1, 66.5, 67.0, 68.2, 69.1, 70.5]
start_temp, *_, end_temp = sensor_data
print(start_temp, end_temp)


# %% Problem 2: Splitting the Path
"""
You have a string representing a file path. You want to separate the actual file name 
from all the folders that came before it.

file_path = "usr/local/bin/python/scripts/main.py"

# Step 1: Split the string into a list of words using .split("/")
parts = file_path.split("/")

Your Task:Using unpacking on the parts list, assign the very last item ("main.py") to a variable 
called filename, and gather all the preceding folder names into a list called folders.
"""
file_path = "usr/local/bin/python/scripts/main.py"
*folders, filename = file_path.split("/")
print(filename)


# %% Problem 3: The Flexible Loop
"""
You have a list of employee records. Each record is a tuple. 
The first item is always the employee's name, but the remaining items are the projects 
they are working on (and everyone has a different number of projects!).

employees = [
    ("Alice", "Project A", "Project B"), 
    ("Bob", "Project C"), 
    ("Charlie", "Project D", "Project E", "Project F")
]

Your Task: Write a for loop that unpacks these tuples directly in the loop definition. 
For each employee, print a string formatted like this: Alice is working on 2 projects. 
(Hint: You will need to use len() on the gathered starred variable).
"""
employees = [
    ("Alice", "Project A", "Project B"), 
    ("Bob", "Project C"), 
    ("Charlie", "Project D", "Project E", "Project F")]

for items in employees:
    emp_name, *projects = items
    print(f"{emp_name} is working on {len(projects)} projects.")


# %% Problem 4: The Podium Finish
"""
You have a list of runners who just finished a 100m sprint, ordered from 1st place to last 
place. You need to assign the winner to a variable, the runner-up to a second variable, 
and group everyone else together into a list of "participants".

race_results = ["Usain", "Tyson", "Yohan", "Justin", "Asafa"]

Your Task: Write a single line of unpacking code that assigns "Usain" to a variable called
gold, "Tyson" to a variable called silver, and gathers the remaining runners into a list 
called participants. Print all three variables to check your work!
"""

race_results = ["Usain", "Tyson", "Yohan", "Justin", "Asafa"]
gold, silver, *participants = race_results
print(gold, silver, participants, sep="\n")


# %% Problem 5: The Weekend Forecast
"""
You have a list containing the daily high temperatures for a full 7-day week, starting on 
Monday and ending on Sunday. You only care about the weekend (Friday, Saturday, and Sunday), 
and want to completely ignore Monday through Thursday.

week_temps = [72, 74, 71, 75, 77, 79, 81]

Your Task: Write a single line of unpacking code that assigns the last three numbers to 
variables called friday, saturday, and sunday. Use the *_ convention at the beginning of 
your variables to gather and throw away all the earlier days in the week.
"""

week_temps = [72, 74, 71, 75, 77, 79, 81]
*_, friday, saturday, sunday = week_temps
print(f"Friday: {friday:>10} \nSaturday: {saturday:>8} \nSunday: {sunday:>10} ")
# %%
