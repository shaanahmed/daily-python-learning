# %% 1. The Dynamic Receipt Generator (String Formatting)
"""The Goal: Practice using f-strings to create a formatted receipt for a coffee shop.
Input: A list of items and their prices (e.g., [("Latte", 4.5), ("Muffin", 3.25)]).
Task: Print a receipt where names are left-aligned and prices are right-aligned, rounded to exactly 2 decimal places.
Hint: Use f-string alignment and precision: {name:<20} for left-alignment and :{.2f} for rounding."""

items = [("Latte", 4.5), ("Muffin", 3.25), ("Espresso", 3.0), ("Croissant", 2.75)]

# Print receipt header
print("=" * 30)
print("COFFEE SHOP RECEIPT")
print("=" * 30)

# Calculate total
total = 0

# Print each item
for name, price in items:
    print(f"{name:<20} ${price:>6.2f}")
    total += price

# Print total
print("-" * 30)
print(f"{'TOTAL':<20} ${total:>6.2f}")
print("=" * 30)


# %% 2. The Multi-line Escape Artist (Escape Sequences)
#The Goal: Correctly use escape sequences to display complex paths and text.
#Task: Create a single string variable that, when printed, displays the following exactly:
#Path: C:\Users\Documents\New_Project
#"Note": Use the '\t' character for tabs.
#Hint: Remember that to print a backslash \ or a quote ", you must "escape" them using \\ or \".

output = "Path: C:\\Users\\Documents\\New_Project\n\"Note\": Use the '\\t' character for tabs."
print(output)


# %% 3. The Custom Progress Bar (Sep and End)
"""The Goal: Use sep and end to modify how data is displayed in the console.

Task: Write a loop that prints numbers from 1 to 10 on the same line, separated by a hyphen -, 
and ending with a final exclamation point ! instead of a newline.

Sample Output: 1-2-3-4-5-6-7-8-9-10!

Hint: Use print(i, end='-') for the loop and a special condition for the final number to change the end character."""

print(*range(1, 11), sep='-', end='!')
print()


# %% 4. The Password Strength Validator (String Module)
"""The Goal: Use string module constants for data validation.
Task: Write a function that checks if a password meets these criteria:

Contains at least one character from string.punctuation.
Contains at least one digit from string.digits.
Contains at least one letter from string.ascii_letters.

Hint: Iterate through the password string and use the in membership operator to check against the module constants."""

import string

def check_password(password):
    # Initialize flags for our criteria
    has_digit = False
    has_punctuation = False
    has_letter = False

    # Iterate through the password character by character
    for char in password:
        # Check if character belongs to specific string module groups
        if char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_punctuation = True
        elif char in string.ascii_letters:
            has_letter = True

    # Validate if all criteria are met
    if has_digit and has_punctuation and has_letter:
        return "Strong Password"
    else:
        return "Weak Password: Must include letters, digits, and punctuation."

# Test it out
user_pass = input("Enter a password to test: ")
print(check_password(user_pass))


# %% 5. The CSV to Clean Report (capwords & join)
"""The Goal: Use the string module and join() to reformat data.
Input: A string of messy names: "alice,bob,charlie,delta"
Task: 1. Split the string by the comma.
2. Capitalize each name using string.capwords().
3. Join them back together with a semicolon and a space ; .
Sample Output: Alice; Bob; Charlie; Delta """

import string

# 1. Input string
messy_names = "alice,bob,charlie,delta"

# 2. Split the string by the comma into a list
# Result: ['alice', 'bob', 'charlie', 'delta']
name_list = messy_names.split(",")

# 3. Capitalize each name using string.capwords in a list comprehension
# Result: ['Alice', 'Bob', 'Charlie', 'Delta']
clean_names = [string.capwords(name) for name in name_list]

# 4. Join them back together with a semicolon and a space
# Result: "Alice; Bob; Charlie; Delta"
final_report = "; ".join(clean_names)

print(f"Original: {messy_names}")
print(f"Cleaned Report: {final_report}")
# %%