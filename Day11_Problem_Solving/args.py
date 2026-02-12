# %%Problem 1: The Multi-Multiplier
"""Create a function called multiply_all that can take any number of integers and 
returns the result of multiplying them all together. If no numbers are provided, 
it should return 1.
Example:
multiply_all(1, 2, 3) should return 6.
multiply_all(5, 10) should return 50."""

def multiply_all(*args):
    if not args:
        return 1
    
    result = 1
    for i in args:
        result *= i
    return result

print(multiply_all(1, 2, 3))
print(multiply_all(5, 10))

# %%Problem 2: The Guest List
# Create a function called announce_party that takes one required argument (host_name) and
# then any number of additional guests using *args.
"""The function should print:
"Host: [host_name]"
"Guests: [guest1], [guest2], ..."

Example:
announce_party("Alice", "Bob", "Charlie")

Host: Alice
Guests: Bob, Charlie"""

def announce_party(host_name, *guests):
    print(f"Host: {host_name}")
    if guests:
        print(f"Guests: {', '.join(guests)}")
    else:
        print("Guests: None")

announce_party("Alice", "Bob", "Charlie")


# %% Problem 3: The Unpacker Challenge
# Suppose you have a list of scores:
# scores = [85, 92, 78, 90, 88]
"""
You have a function defined like this:

def show_top_three(first, second, third, *others):
    print(f"Gold: {first}, Silver: {second}, Bronze: {third}")
The Goal: Use the unpacking operator to pass the scores list into the function. 
What will happen to the scores 90 and 88?"""

def show_top_three(first, second, third, *others):
    print(f"Gold: {first}, Silver: {second}, Bronze: {third}")

scores = [85, 92, 78, 90, 88]
show_top_three(*scores)

# %% Problem 4: The String Joiner
""" Write a function make_sentence that takes a separator (as a keyword-only argument) and
any number of words. It should join the words using that separator.
Example:
make_sentence("Apple", "Banana", "Cherry", sep=" & ")

Result: "Apple & Banana & Cherry" """

def make_sentence(*words, sep=" "):
    return sep.join(words)

print(make_sentence("Apple", "Banana", "Cherry", sep=" & "))
# %%
