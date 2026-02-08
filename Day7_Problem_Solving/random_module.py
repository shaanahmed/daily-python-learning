# %% 1. The Coin Flip Simulator
"""Write a program that simulates flipping a coin 10 times.
Goal: For each "flip," the program should randomly choose between the strings "Heads" or "Tails".
Hint: Use a function that picks one random element from a non-empty sequence."""
import random

coin = ["Heads", "Tails"]

for i in range(10):
    print(f"Flip {i+1}: {random.choice(coin)}")


# %% 2. The Lottery Ticket Generator
"""You want to generate a set of lottery numbers.
Task: Pick exactly 6 unique numbers from a range of 1 to 49.
Constraint: Ensure there are no duplicate numbers in your selection.
Hint: Use the function designed for "sampling without replacement". """

lottery_number = random.sample(range(1, 49), 6)
print(f"The lottery numbers are: \n {lottery_number}")


# %% 3. The Digital Dice
"""Create a "Digital D20" (a 20-sided die).
Task: Generate a random integer between 1 and 20 (where both 1 and 20 are possible results).
Hint: Remember that randint(a, b) includes both endpoints, unlike randrange()."""
import random

digital_dice20 = random.randint(1, 20)
print(digital_dice20)


# %% 
# %% 4. The Digital Dice(Several Roles)
"""Create a "Digital D20" (a 20-sided die).
Task: Generate a random integer between 1 and 20 (where both 1 and 20 are possible results).
Hint: Remember that randint(a, b) includes both endpoints, unlike randrange()."""
import random

for _ in range(5):
    print(random.randint(1, 20))


# %% 4. Card Shuffler
"""You have a list representing a deck of cards: ['Ace', 'King', 'Queen', 'Jack', '10'].
Task: Randomly rearrange the order of the cards in the list.
Warning: Remember that this specific function modifies the list in-place and returns None."""
import random
cards = ['Ace', 'King', 'Queen', 'Jack', '10']
random.shuffle(cards)
print(cards)


# %% 5. The Predictable "Random"
"""If you want to share a "random" result with a friend so they get the exact same numbers as you:
Task: What function do you need to call at the very beginning of your script to ensure the results are reproducible?.
Goal: Set this to the number 42 and then generate a random float between 0 and 1."""

import random

random.seed(42)
result = random.random()

print("Predictable random number:", result, sep="\n")
# %% 
