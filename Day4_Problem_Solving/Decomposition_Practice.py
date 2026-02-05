# %% 1. The Travel Expense Organizer
"""Goal: Instead of one giant block of code, create small "worker" functions that report to a "manager" function.
Step A: Create a function calc_flight(price) that returns the price after a 5% tax.
Step B: Create a function calc_hotel(nights, daily_rate) that returns nights * daily_rate.
Step C: Create the "Manager" function total_trip_cost(flight, hotel_total). It should simply return the sum of both.
Action: Call the manager function using the results from the first two."""

def calc_flight(price):
    return price * 1.05

def calc_hotel(nights, daily_rate):
    return nights * daily_rate

def total_trip_cost(flight, hotel_total):
    return flight + hotel_total

flight_cost = calc_flight(500)
hotel_cost = calc_hotel(4, 250)

total_trip_cost(flight_cost, hotel_cost)


# %% 2. The String Cleaner (Data Processing)
"""Goal: Decompose the steps of cleaning user-inputted data.
Function 1: remove_spaces(text) -> returns text with leading/trailing spaces removed using .strip().
Function 2: make_lowercase(text) -> returns text in all lowercase using .lower().
Function 3: clean_data(text) -> This function should call Function 1, then pass that result to Function 2, and finally return the fully cleaned string.
Action: Pass the string " UrThirsTyBBy " into clean_data and print the result."""

def remove_spaces(text):
    return text.strip()

def make_lowercase(text):
    return text.lower()

def clean_data(text):
    return make_lowercase(remove_spaces(text))

clean_data("Elon Musk says that in 10 to 20 years, work will be optional and money will be irrelevant thanks to AI and robotics                                                                                                                               ")

# %% 3. The Math Suite (Logic Isolation)
""" Goal: Build a "Calculator" by decomposing math operations.
Task: Create four tiny functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
Challenge: Create a final function complex_operation(x, y, z) that calculates (x + y) * z by only calling your add and multiply functions inside it. """

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        print("Error cannot divided by 0!")
    else:
        return a / b

def complex_operation(x, y, z):
    return multiply(add(x, y),z)

result = complex_operation(3, 5, 2)
print(result)

# %%
