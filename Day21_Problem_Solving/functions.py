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
    if len(data) < 2:
        return []

    peaks = []
    n = len(data)

    for i in range(n):
        if i == 0:
            if data[i] > data[i + 1]:
                peaks.append(data[i])
        
        elif i == n - 1:
            if data[i] > data[i - 1]:
                peaks.append(data[i])
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
        name = item['name'].lower()
        quantity = item['quantity']
        
        totals[name] = totals.get(name, 0) + quantity

    final_inventory = {k: v for k, v in totals.items() if v > 0}
    
    return final_inventory

stock_updates = [
    {"name": "Apple", "quantity": 10},
    {"name": "banana", "quantity": 5},
    {"name": "APPLE", "quantity": -3},
    {"name": "pear", "quantity": 2},
    {"name": "banana", "quantity": -5}
]

print(audit_inventory(stock_updates))

# %% The Problem: The "Run-Length Encoder
"""
In data compression, Run-Length Encoding (RLE) is a simple way to represent repeated data. For example, instead of writing "AAAABBBCC", you would write "4A3B2C".

The Requirements
Function Name: compress_string

Input: A single string of characters (e.g., "AAABBC")

Output: A compressed string representing the counts (e.g., "3A2B1C")

Special Rules:

If the input string is empty, return an empty string.

The function should be case-sensitive ("a" and "A" are different).
"""

def compress_string(text):
    if not text:
        return ""

    compressed = []
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(str(count) + text[i - 1])
            count = 1
    compressed.append(str(count) + text[-1])
    
    return "".join(compressed)

print(compress_string("AAABBC")) 
print(compress_string("GGGGoooo"))
print(compress_string("abc"))     


# %% The Problem: The "Heatmap Filter"
"""
Imagine you have a 2D grid (a list of lists) representing temperatures in a room. You need to "sanitize" this data by identifying any coordinate that exceeds a certain threshold.

The Requirements
Function Name: find_hot_spots

Input: * grid: A list of lists of integers (e.g., [[20, 25], [30, 15]]).

threshold: An integer.

Output: A list of tuples, where each tuple is the (row, column) index of a "hot spot."

Special Rules:

If no spots exceed the threshold, return an empty list.

The output should be ordered by row, then by column.
"""

def find_hot_spots(grid, threshold):
    hot_spots = []
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > threshold:
                hot_spots.append((i, j))
                
    return hot_spots

room_temp = [
    [22, 25, 19],
    [30, 24, 21],
    [18, 29, 20]
]

print(find_hot_spots(room_temp, 24))


# %%
