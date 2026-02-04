# %% 1. The Countdown (range with step)
"""Goal: Use range() to count backwards.
Task: Use a for loop and range() to print a countdown from 10 down to 1.
Hint: range(start, stop, step) can use -1 as a step."""

for i in range(10, 1, -1):
    print(i)

# %% 2. The FizzBuzz Lite (Loop + Elif)
"""Goal: Handle multiple conditions inside a loop.
Task: Loop through numbers from 1 to 15.
If the number is divisible by 3, print "Music".
elif the number is divisible by 5, print "Code".
else print the number itself."""

for num in range(1, 15):
    if num % 3 == 0:
        print("Music")
    elif num % 5 == 0:
        print("Code")
    else:
        print(num)


# %% 3. The List Accumulator
"""Goal: Sum up values in a list.
Task: Create a list expenses = [200, 500, 150].
Logic: Create a variable total = 0. 
Use a for loop to add each expense to the total, then print the final sum after the loop finishes."""

expenses = [200, 500, 150]
total = 0

for price in expenses:
    total += price
print(total)


# %% 4. The High-Expense Tracker (Accumulator + If)
"""Goal: Sum only specific items in a list.
Task: Create a list prices = [100, 450, 50, 600, 200].
Logic: Create a total = 0. Use a for loop to look at each price. 
If the price is greater than 300, add it to the total.
Skill: Selective accumulation (adding only what meets a condition)."""

prices = [100, 450, 50, 600, 200]
total = 0

for price in prices:
    if price > 300:
        total += price
print(total)


# %% 5. The Discount Applier (Modifying a Running Total)
"""Goal: Apply logic to items before adding them to a total.
Task: You have a list of song stream counts: streams = [1000, 2000, 5000].
Logic: Create a total_royalties = 0. For every song in the list, calculate the royalty as song * 0.01. 
Add that calculated amount to your total_royalties.
Skill: Processing data mathematically before accumulating it."""

streams = [1000, 2000, 5000]
total_royalties = 0

for num in streams:
    royal = num * 0.001
    total_royalties += royal
print(total_royalties)


# %% 6. The Multi-List Manager (Double Accumulation)
"""Goal: Manage two totals at once.
Task: You have a list of values: data = [10, -5, 20, -2, 30].
Logic: Create two variables: pos_sum = 0 and neg_sum = 0.
Loop: If the number is positive, add it to pos_sum. If it is negative, add it to neg_sum.  
Print both totals at the end."""

data = [10, -5, 20, -2, 30]
pop_sum = 0
neg_sum = 0
for n in data:
    if n >= 0:
        pop_sum += n
    else:
        neg_sum += n

print(pop_sum)
print(neg_sum)


# %%
