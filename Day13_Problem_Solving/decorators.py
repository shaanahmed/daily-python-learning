# %% Problem 1: Currency Formatter
"""You are building a checkout system. We have a function called new_price(quantity) that 
calculates the total price by multiplying the quantity of items by 0.9.

Your Task:

Write a decorator named price_string.

The decorator should intercept the result of any function it is applied to, convert that 
result into a string, and add a British Pound symbol ("£") to the very beginning of it.

Apply the @price_string decorator to the new_price function.

Example:
If you call new_price(10), the final output should be the string "£9.0" 
instead of the float 9.0."""

def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))
    return wrapper

@price_string
def new_price(quantity):
    return quantity * 0.9

print(new_price(10))
print(type(new_price(10)))


# %% Problem: The HTML Tagger
"""Background:
We have a predefined function called from_input(inp) that receives some user input and removes 
any extra spaces at the beginning and at the end of the string using the built-in strip() method.
Starter Code:

Python
def from_input(inp):
    string = inp.strip()
    return string
Your Task:

Create a decorator named tagged.
The decorator should intercept the cleaned string returned by from_input and wrap it 
inside HTML title tags: <title></title>.
Apply the @tagged decorator to the from_input function.

Constraints & Tips:
You must return the newly formatted string from your wrapper, not print it.
You do not need to write the code to take user input or call the function yourself; just focus on writing the body of the decorator.

Example:
If the input string is "   Test   ", the from_input function will strip it down to "Test". Your decorator should then catch it and output:
"<title>Test</title>" """

def tagged(func):
    def wrapper(inp):
        return f"<title>{func(inp)}</title>"
    return wrapper

@tagged
def from_input(inp):
    string = inp.strip()
    return string

print(from_input("  Shaan  ")) 


# %% Problem: Math Operations Decorator
"""Background:
Consider the following decorator, print_info, that takes a function with two arguments and
 prints those arguments before actually calling the function.

Python
def print_info(func):
    def wrapper(arg1, arg2):
        print("The arguments of the function are:", arg1, arg2)
        return func(arg1, arg2)
    return wrapper
Your Task:

Write the body of the addition function so that it computes and returns the sum of its two
arguments.
Decorate the addition function with the @print_info decorator.

Constraints & Tips:

You must use the return keyword inside the addition function, not print()"""

def print_info(func):
    def wrapper(arg1, arg2):
        print("The arguments of the function are:", arg1, arg2)
        return func(arg1, arg2)
    return wrapper

@print_info
def addition(arg1, arg2):
    return arg1 + arg2

result = addition(22, 25)
print(result)

# %%The Timer (Performance Testing)
"""
Ever wonder exactly how many milliseconds a function takes? 
Don't add time.time() to every function. Use a decorator.The Timer (Performance Testing)
Ever wonder exactly how many milliseconds a function takes? 
Don't add time.time() to every function. Use a decorator."""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def heavy_computation():
    time.sleep(1.5)
    return "Done!"

heavy_computation()


# %%
