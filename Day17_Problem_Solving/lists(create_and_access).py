# %% Question 1: The Basics
"""
You have the following list of colors:
colors = ["red", "blue", "green", "yellow", "purple"]
What code would you write to access the word "green"?
"""

colors = ["red", "blue", "green", "yellow", "purple"]
print(colors[2])


# %% Question 2: Negative Indexing
"""
Using the same colors list above, what will be the output of print(colors[-2])?
"""
colors = ["red", "blue", "green", "yellow", "purple"]
print(colors[-2]) 


# %% Question 3: Slicing
"""
Given the list of numbers:
nums = [10, 20, 30, 40, 50, 60]
What will print(nums[1:4]) output?
"""

nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])


# %% Question 4: Step Slicing
"""
Using the same nums list, what code would you write using slicing to extract only the 
numbers [10, 30, 50]? (Hint: Think about the step parameter).
"""

nums = [10, 20, 30, 40, 50, 60]
print(nums[:5:2])


# %% Question 5: Nested Lists (2D Arrays)
"""
You have a list that contains other lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
What exact code would you write to access the number 6?
"""
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
print(matrix[1][2])


# %% Question 6: The len() Trick
"""
You have a list of students:
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
Without using negative indexing (like [-1]), write the exact code to access the very last 
student ("Eve") by using the len() function.
"""

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(students[len(students) - 1])


# %% Question 7: Write the code to find out how many times you rolled a 6 in this list: 
# rolls = [3, 6, 1, 6, 2, 6, 4]

rolls = [3, 6, 1, 6, 2, 6, 4]
print(rolls.count(6))


# %% Question 8: Ask Python for the exact index number of "Deploy code" in this list: 
# tasks = ["Email boss", "Fix bug", "Deploy code", "Eat lunch"]

tasks = ["Email boss", "Fix bug", "Deploy code", "Eat lunch"]
print(tasks.index("Deploy code"))


# %% Question 9: Given countdown = [1, 2, 3, 4, 5], 
# what will be the output if you run print(countdown[::-1])?

countdown = [1, 2, 3, 4, 5]
print(countdown[::-1])


# %% Question 10: Deeply Nested Lists
"""
Things are getting complex. You have a list inside a list inside a list:
data = ["Apple", [10, 20, ["X", "Y", "Z"]], "Banana"]
Write the exact code to access the letter "Y".
"""

data = ["Apple", [10, 20, ["X", "Y", "Z"]], "Banana"]
print(data[1][2][1])

# %%