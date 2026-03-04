# %% try and except

try:
    num = int(input("Enter a divisor: "))
    result = 10/num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("ERROR! You cannot divide by 0.")
except ValueError:
    print("ERROR! Please enter a valid whole number.")


# %% The Full Power Trio (else + finally)

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File doesn't exist.")
else:
    print("File read successfully!")
    print(content)
finally:
    if 'file' in locals():
        file.close()
        print("File resources released.")


# %% Raising our Own Exceptions

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Age set to {age}"

try:
    set_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")


# %% Problem 1: The "Safe Calculator"
"""Create a function called safe_divide() that takes two arguments, a and b.
Goal: Return the result of a / b.
Requirements:Handle ZeroDivisionError if the user tries to divide by zero.
Handle TypeError in case the user passes a string instead of a number.
Use an else block to print "Calculation successful!" if it works.
Use a finally block to print "Execution complete." regardless of the outcome.
"""

def safe_divide(a, b):
    return a / b

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(safe_divide(a, b))
except ZeroDivisionError:
    print('ERROR! You cannot divide by 0.')
except TypeError:
    print("ERROR! Enter an innteger not string")
else:
    print("Calculation Successfull!")
finally:
    print('Execution complete.')


# %% Problem 2: The "ATM Simulator"
"""
Write a script that asks a user how much money they want to withdraw from a fake balance 
of $500.

Goal: Process a withdrawal amount from input().

Requirements:

Input Handling: Use try/except to catch ValueError if the user types something that isn't 
a number (like "twenty").

Logic Validation: If the user enters a negative number or an amount greater than 500, 
use raise to trigger a ValueError with a custom message (e.g., "Insufficient funds" or "Invalid amount").

Success: If the input is valid, print the remaining balance.
"""

avail_balance = 500

def withdraw(amount):
    if amount > avail_balance:
        raise ValueError("Insufficient Funds!")
    elif amount <= 0:
        raise ValueError("Invalid amount!")
    else:
        return avail_balance - amount
    
try:
    user_input = input('Enter the amount you want to withdraw: ')
    amount = int(user_input) 

    remaining_balance = withdraw(amount)

except ValueError as e:
    print(f"ERROR: {e}")

else:
    print("Please wait, the transaction is being processed...")
    print(f"The remaining balance is ${remaining_balance}")
finally:
    print("The Transaction has been completed. THANK YOU.")



# %%
