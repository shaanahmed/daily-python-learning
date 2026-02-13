# %%Problem 1: The Square
"""Write a lambda function that takes one number and returns its square.

Input: 5
Expected Output: 25"""

square = lambda x : x ** 2
print(square(5))

#Another way without assigning to any variable

print((lambda x : x**2)(4))
# %%Problem 2: The Inverse
"""Write a lambda function that takes a number. If it is positive, return its negative (inverse). If it is negative or zero, return it as is.

Input: 10, -5
Expected Output: -10, -5"""

negative = lambda x : -x if x < 0 else x
print(negative(10))

# %% Problem 3: The String Slicer
"""Write a lambda function that takes a string and returns the last 3 characters reversed. (e.g., "Python" -> "noh").

Input: "GitHub"
Expected Output: "buH" """

reverse = lambda x: x[-3:][::-1]
print(reverse("GitHub"))

# %% Problem 4: The Temperature Converter (Map)
"""You have a list of temperatures in Celsius: [0, 20, 37, 100].
Use map() and a lambda function to convert them all to Fahrenheit.

Formula: F = (C * 9/5) + 32
Expected Output: [32.0, 68.0, 98.6, 212.0]"""

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)


# %% Problem 5: The Bouncer (Filter)
"""You have a list of ages: [12, 18, 35, 17, 21, 55, 9].
Use filter() and a lambda function to keep only the ages that are 18 or older.

Expected Output: [18, 35, 21, 55]"""

ages = [12, 18, 35, 17, 21, 55, 9]

adults = list(filter(lambda age: age >= 18, ages))
print(adults)


# %%Problem 6: The Custom Sort (Sorted)
"""You have a list of tuples representing students and their grades:
students = [("Alice", 88), ("Bob", 45), ("Charlie", 92), ("David", 78)]
Use sorted() with a key lambda to sort this list by grade (lowest to highest).

Expected Output: [('Bob', 45), ('David', 78), ('Alice', 88), ('Charlie', 92)]"""

students = [("Alice", 88), ("Bob", 45), ("Charlie", 92), ("David", 78)]

# Using sorted() with lambda function as key
sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)


# %% Problem 7: The Exponential Factory
"""Write a standard function called power_factory(n). It should return a lambda function 
that raises any number x to the power of n.

Usage:

Python
square = power_factory(2)
cube = power_factory(3)
print(square(4)) 
print(cube(4))
Expected Output: 16, 64"""

def power_factory(n):
    return lambda x: x ** n

square = power_factory(2)
cube = power_factory(3)

print(square(4)) 
print(cube(4))

# %%
