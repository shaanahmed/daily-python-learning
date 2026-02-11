#  %% 1. Write a recursive function to find the sum of the first N natural numbers.
# Goal: If N=5, the result should be 5+4+3+2+1 = 15.
# Hint: The base case is when N = 1.

def rec_fun(n):
    # Base Case
    if n == 1:
        return 1
    else:
        return n + rec_fun(n-1)
    
print(rec_fun(5))


# %% 2.Write a recursive function to reverse a string.
"""Goal: reverse("hello") should return "olleh".
Hint: Take the last letter and add it to the reverse() of the rest of the string."""

def rev_str(word):
    if len(word) == 0:
        return word
    else:
        return word[-1] + rev_str(word[:-1])  #[:-1] takes everything except the last character
    
print(rev_str("Hello"))


# %% 3. The "Fibonacci Sequence" Challenge
# The Fibonacci sequence is a famous series where each number is the sum of the two preceding ones: 
# 0, 1, 1, 2, 3, 5, 8, 13 
# The Goal: Write a function fib(n) that returns the n^{th} Fibonacci number.
# Base Case: If n=0, return 0. If n=1, return 1.
# Recursive Step: Return fib(n-1) + fib(n-2).

def fib(n):
    # Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fib(n-1) + fib(n-2)
print(fib(13))


# %% 4. The "Palindrome Checker"
# A palindrome is a word that reads the same backward as forward (like "level" or "racecar").
# The Goal: Write a recursive function is_palindrome(string).
# Base Case: If the string has 0 or 1 characters, it is a palindrome.
# Recursive Step: Check if the first and last letters are the same. If they are, call the function again on the string without the first and last letters.

def palin(word):
    if len(word) <= 1:
        return "It is a palindrome"
    
    # Recursive Step
    if word[0] == word[-1]:
        return palin(word[1:-1])
    else:
        return "It is not a palindrome"

print(palin("racecar"))
print(palin("level"))
print(palin("hello"))

# %% 5. The "Digit Sum" Problem
# The Goal: Given a positive integer like 1234, return the sum of its digits (1+2+3+4 = 10).
# Base Case: If the number is less than 10, just return the number itself.
# Recursive Step: Take the last digit (n % 10) and add it to the result of the 
# function called on the rest of the digits (n // 10).

def sum_digit(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sum_digit(n//10) 

print(sum_digit(12345))

# %% 6. Nested List Summing
#Sometimes lists contain other lists, like [1, [2, 3], 4].
#The Goal: Write a function to sum every number, even the ones inside the nested lists.
#The Logic: Loop through the items. If an item is a number, add it to the total. 
# If an item is a list, call your sum_nested() function on that list (recursion!) and 
# add that result to your total.

def sum_nested(lst):
    total = 0
    
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    
    return total

print(sum_nested([1, [2, 3], 4]))          