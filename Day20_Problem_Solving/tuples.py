# %% Problem 1: The Unpacker
"""
Tuples are famous for "unpacking" multiple variables at the exact same time. You have a 
tuple representing the RGB (Red, Green, Blue) color code for pure purple.

purple = (128, 0, 128)

Your Task:
In a single line of code, unpack this tuple into three separate variables called r, g, and 
b. Print them out to verify! (Hint: x, y, z = my_tuple)
"""

purple = (128, 0, 128)
r, g, b = purple
print(r, g, b)

# %% Problem 2: The Multi-Return
"""
Functions can normally only return one thing. But if you separate return values with commas, 
Python automatically packs them into a tuple for you!

numbers = [15, 22, 8, 99, 4]

def get_min_max(nums):
    # Your code here!

Your Task:
Finish the function so it returns both the min(nums) and the max(nums) separated by a 
comma. Call the function, assign the result to a variable called extremes, and print it. 
(You should see a tuple (8, 99)).
"""

numbers = [15, 22, 8, 99, 4]

def get_min_max(nums):
    return min(nums), max(nums)

extremes = get_min_max(numbers)
print(extremes)

# %% Problem 3: The "Gotcha" Comma
"""
Creating a tuple with multiple items is easy: (1, 2). But creating a tuple with only one 
item is a famous Python trap. If you just write (5), Python thinks you are doing math and 
makes it an integer.

not_a_tuple = (5)
print(type(not_a_tuple)) # Outputs: <class 'int'>

Your Task:
Create variable called actual_tuple that contains just the number 5, but formatted correctly 
as a tuple. Print its type() to prove it is a <class 'tuple'>. 
(Hint: It needs a trailing comma!)
"""
actual_tuple = (5,)
print(type(actual_tuple))

# %%
