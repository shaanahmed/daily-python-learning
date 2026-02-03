# %% 1. The Trip Budgeter (Variables & Arithmetic)
"""Goal: Calculate the remaining travel budget after a set of expenses.
   Task: Create a variable for a starting_budget. Subtract three different expenses (e.g., food, transport, and a souvenir). 
   Bonus: Use the modulo operator (%) to see if you have an even or odd amount of money left."""

starting_budget = int(input("Enter the budget: "))
food_expenses = int(input("Enter the food expense: "))
transport_expenses = int(input("Enter the trannsport expense: "))
souvenir_expenses = int(input("Enter the souvenir expense: "))

remaining_budget = starting_budget - food_expenses - transport_expenses - souvenir_expenses
print(f"{remaining_budget} is our remining budget.")
print("Even" if remaining_budget % 2 == 0 else "Odd")

# %%2. The Rectangle Architect (Input & Numbers)Goal:
""" 
Create a tool that calculates the area and perimeter of a rectangle.Task: Use input() to get the length and width from the user. 
Remember to convert these inputs to float or int.
Logic:Area = length * width
Perimeter = 2 * (length + width)"""

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

print("area of rectangle is: ", length * width)
print("perimeter of rectangle is: ", 2 * (length + width))

# %% 3. The Digital "Age" Teller (Integer Arithmetic)Goal: 
''' Calculate how many days, hours, and minutes a person has lived based on their age in years.
Task: Ask the user for their age as an integer.
Calculation: Days = Age * 365
Hours = Days * 24
Minutes = Hours * 60
Note: Don't worry about leap years for this basic version!'''

age = int(input("Enter your age in years: "))

days = age * 365
hours = days * 24
minutes = hours * 60

print(f"The person has lived {days} days, {hours} hours, {minutes} minutes.")


# %% 4. The Bill Splitter (Taking User Input)
"""Goal: Help a group of friends split a restaurant bill including a tip.
Task: 1. Input the total bill amount. 2. Input the number of people. 3. Input the tip percentage (e.g., 10 or 15).
Logic: Calculate the total bill (amount + tip) and then divide it by the number of people to find the "Individual Share." """

bill = float(input("Enter the bill amount: "))
persons = float(input("Enter the number of people: "))
tip_percent = int(input("Enter  the  tip percent: "))

print("total bill per person is:", (bill + (bill * tip_percent/100)) / persons)

# %% 5. Type Investigator (Basic Data Types & Booleans)Goal: 
""" Build a script that "tests" the properties of an input.
 Task: Ask the user to enter a number.
 Logic: Create a boolean variable is_positive that checks if the number is > 0
 Create a boolean variable is_even that checks if the number is divisible by 2.
 Print both results (True/False) to the console."""

user = int(input("Enter a number: "))
is_positive = user > 0
is_even = user % 2 == 0
print(f"Is positive {is_positive}")
print(f"Is even {is_even}")

# %%
