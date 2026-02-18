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

    
# %%
