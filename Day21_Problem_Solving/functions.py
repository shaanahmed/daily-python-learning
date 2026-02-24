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
# %%
