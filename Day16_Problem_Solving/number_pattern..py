# %% 1. Simple Right-Angled Triangle
"""This pattern prints the current row number for each column in that row. 
It’s the best place to start.

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()


# %% 2. The Inverted Pyramid
"""This flips the logic. You start with a full row and decrease the count as you go down.

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

"""
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

    
# %% 3. Descending Column Pattern
"""Instead of repeating the row number, this pattern counts down within the row itself.

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

"""

rows = 5
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# %% 4. Floyd's Triangle (Incremental Numbers)
"""This one is slightly different because the number doesn't "reset" at the start of a new
row; it keeps growing.

1 
2 3 
4 5 6 
7 8 9 10

"""

rows = 4
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

    
# %%
