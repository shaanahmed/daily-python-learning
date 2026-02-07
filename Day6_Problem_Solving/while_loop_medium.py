# %% Problem 3: Fibonacci Sequence Under Limit
""" Difficulty: Medium
Write a program that takes a positive integer N as input and prints all Fibonacci numbers that are less than N.
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two."""

n = int(input())
a, b = 0, 1

while a < n:
    print(a, end=" ")
    a, b = b, a+b


# %% Problem 4: Reverse Digits
"""Difficulty: Medium
Write a program that takes a positive integer as input and prints its digits in reverse order 
(as separate digits, one per line). Use a while loop to extract digits."""

n = int(input())
rev_dig = 0

while n > 0:
    dig = n % 10
    print(dig)
    n //= 10

# %% Problem 5: Password Validator
"""Difficulty: Medium
Write a program that keeps asking the user to enter a password until they enter a valid one. 
A valid password must:
##Be at least 8 characters long
##Contain at least one digit
After each invalid attempt, print why it was invalid. When a valid password is entered, print "Password accepted!"."""

while True:
    password = input("Enter your password")
    if len(password) < 8 :
        print("Invalid Password: Password must contain at least 8 characters.")
    elif not any(ch.isdigit() for ch  in password):
        print("Invalid Password: Password must containn at least one digit")
    else:
        print("Password Accepted!")
        break

# %% Bonus Challenge: Greatest Common Divisor (GCD)
""" Difficulty: Hard
Write a program that takes two positive integers as input and finds their GCD using the Euclidean algorithm with a while loop.
Algorithm: Repeatedly replace the larger number with the remainder of dividing the larger by the smaller until one number becomes 0. 
The other number is the GCD."""

a = int(input())
b = int(input())

while b != 0:
    reminder = a % b
    a = b
    b = reminder
print("GCD is", a)

# %%
