# %%1. The Weather Advisor (If/Else)
"""Goal: Use a single condition to give advice.
Task: Ask the user for the current temperature in Nha Trang.
Logic: * If the temperature is greater than 30, print "It's a hot day! Stay hydrated."
Otherwise (Else), print "The weather is pleasant for a walk."
Skill: Applying basic if and else logic to user input."""

current_temp = int(input("Enter the current temperature in Nha Trang: "))
if current_temp > 30:
    print("It's a hot day! Stay hydrated.")
else:
    print("The weather is pleasant for a walk.")


# %% 2. The Budget Guardian (Comparison & If/Else)
"""Goal: Check if a purchase is affordable.
Task: Create a variable wallet_balance = 1000. Ask the user for the item_price.
Logic: If wallet_balance is greater than or equal to item_price, print "Purchase successful!" and show the remaining balance.
Else, print "Insufficient funds. You need [amount] more."
Skill: Using comparison operators (>=) within a conditional block."""

wallet_balance = 1000
item_price = float(input("Enter the price of the item: "))

if wallet_balance >= item_price:
    print("Purchase Successful!")
else:
    print(f"Insufficient funds. You need {item_price - wallet_balance} more.")


# %% 3. The Even-Odd Classifier (Modulo & Conditionals)
"""Goal: Determine the property of an integer.
Task: Take an integer input from the user.
Logic: If the number % 2 == 0, print "This is an even number."
Else, print "This is an odd number."
Skill: Combining arithmetic operators with if statements."""

num = int(input("Enter a number: "))
print("This is an even number." if num % 2 == 0 else "This is an odd number.")


# %% 4. The Grade Calculator (Multiple Conditions)
""" Task: Ask for a score (0-100).
Logic:If score >= 90: print "Grade: A"
elif score >= 80: print "Grade: B"
elif score >= 70$: print "Grade: C"
else: print "Grade: F"
Goal: Understand that Python checks these in order and stops at the first True one. """

score = int(input("Enter the score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Garde: F")


# %%  5. The Number Signer (Positive, Negative, or Zero)
"""Task: Take a number input.
Logic:If number > 0: print "Positive"
elif number < 0: print "Negative"
else: print "It is Zero" """

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("It is zero")


# %% 3. The Music Volume Warning (Range Checking)
"""Task: Ask for a volume level (0-100).
Logic:If volume > 80: print "Too loud! Risk of hearing damage."
elif volume > 50: print "Moderate volume."
else: print "Safe volume." """

vol = int(input("Enter volume between 0 - 100: "))
if vol > 80:
    print("Too loud! Risk of hearing damage.")
elif vol > 50:
    print("Moderate Volume")
else:
    print("Safe Volume.")


