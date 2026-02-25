# %% 1. The Basic Logic: Temperature Converter
"""
Problem: Write a function called convert_temp that takes a temperature and 
a unit ("C" for Celsius or "F" for Fahrenheit) and converts it to the other unit.
Formula for C to F: F = C * 9/5 + 32
Formula for F to C: C = (F - 32) * 5/9
"""

def convert_temp(temp, unit):
    if unit.upper() == "C":
        # Converting Celsius to Fahrenheit
        return (temp * 9/5) + 32
    elif unit.upper() == "F":
        # Converting Fahrenheit to Celsius
        return (temp - 32) * 5/9
    else:
        return "Invalid Unit"

# Testing the function
print(f"32°C in Fahrenheit: {convert_temp(32, 'C')}")
print(f"100°F in Celsius: {convert_temp(100, 'F')}")


# %% 2. Lists & Loops: Finding the Peak
"""
Problem: Write a function find_max that takes a list of numbers and returns the largest one 
without using Python's built-in max() function. This helps you understand how functions 
iterate through data.
"""

def find_max(numbers):
    if not numbers:
        return None
    
    # Assume the first number is the biggest to start
    max_val = numbers[0]
    
    for num in numbers:
        if num > max_val:
            max_val = num
            
    return max_val

# Testing the function
my_nums = [15, 42, 7, 88, 21]
print(f"The largest number is: {find_max(my_nums)}")

# %% 3. String Manipulation: The Palindrome Checker
"""
Problem: Create a function is_palindrome that checks if a word reads the same forward and 
backward (like "radar" or "madam"). It should ignore capitalization.
"""

def is_palindrome(word):
    # Standardize to lowercase
    clean_word = word.lower()
    
    # Reverse the string using slicing [start:stop:step]
    reversed_word = clean_word[::-1]
    
    return clean_word == reversed_word


# Testing the function
test_word = "Racecar"
if is_palindrome(test_word):
    print(f"Yes, '{test_word}' is a palindrome!")
else:
    print(f"No, '{test_word}' is not a palindrome.")
# %% The Problem: The "Unique Peak" Finder
"""
You are tasked with writing a function that analyzes a list of integers. A peak is defined as an element that is strictly greater than its immediate neighbors.

The Requirements
Function Name: find_peaks

Input: A list of integers.

Output: A list of all peak values.

Special Rules:

The first and last elements can be peaks if they are greater than their only neighbor.

If the list has fewer than two elements, return an empty list.

The function should handle duplicate peaks (e.g., if 7 is a peak twice, it should appear twice in the output).
"""

def find_peaks(data):
    # Handle the edge case for short lists
    if len(data) < 2:
        return []

    peaks = []
    n = len(data)

    for i in range(n):
        # Check first element
        if i == 0:
            if data[i] > data[i + 1]:
                peaks.append(data[i])
        
        # Check last element
        elif i == n - 1:
            if data[i] > data[i - 1]:
                peaks.append(data[i])
        
        # Check middle elements
        else:
            if data[i] > data[i - 1] and data[i] > data[i + 1]:
                peaks.append(data[i])
                
    return peaks

# Test cases
print(f"Peaks in [1, 3, 2, 8, 5]: {find_peaks([1, 3, 2, 8, 5])}") 

print(f"Peaks in [10, 2, 1, 5, 4]: {find_peaks([10, 2, 1, 5, 4])}") 
# %% The Problem: The "Inventory Auditor"
"""
You are building a system for a grocery store. You receive a list of "transaction" dictionaries, but the data is messy. Some items are repeated, and some have negative values (returns).

The Requirements
Function Name: audit_inventory

Input: A list of dictionaries, where each dictionary has a name (string) and a quantity (integer).

Output: A single dictionary containing the total count for each item.

Special Rules:

If an item's final total is zero or less, it should be removed from the final dictionary.

The item names should be treated as case-insensitive (e.g., "Apple" and "apple" are the same item).
"""

def audit_inventory(transactions):
    totals = {}

    for item in transactions:
        # Standardize the name to lowercase for case-insensitivity
        name = item['name'].lower()
        quantity = item['quantity']
        
        # Add the quantity to the existing total, or start at 0 if new
        totals[name] = totals.get(name, 0) + quantity

    # Create a new dictionary excluding items with 0 or fewer counts
    # This is called a Dictionary Comprehension
    final_inventory = {k: v for k, v in totals.items() if v > 0}
    
    return final_inventory

# Test Case
stock_updates = [
    {"name": "Apple", "quantity": 10},
    {"name": "banana", "quantity": 5},
    {"name": "APPLE", "quantity": -3},
    {"name": "pear", "quantity": 2},
    {"name": "banana", "quantity": -5}
]

print(audit_inventory(stock_updates))

# %%
