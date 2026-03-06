# %% 

if (n := len("Shaan")) > len('Ali'):
    print(f"That's a short name {n} characters.")

# %% Practical Scenarios (Intermediate)
"""
The while Loop Pattern
This is the most "illegal" feeling use case. 
Imagine you are asking a user for input until they type "quit."
"""

while (command := input("Enter a command: ")) != "quit":
    print(f"Executing {command}")


# %% List Comprehensions (Advanced Level)
"""
You have a list of numbers, and you want to find their cubes—
but conly if the cube is over 100.
"""
# Pro method
nums = [2, 4, 5, 6]
print([cube for x in nums if (cube := x**3) > 100])


#Standard basic method
result = [i**3 for i in nums if i**3 > 100]
print(result)


# %%


