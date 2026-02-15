# %% Pattern 1: Pyramid (Increaisng, Centered)
"""
    *
   ***
  *****
 *******
*********

"""
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))


# %% Pattern 2: Inverted Pyramid(Decreasing, centered)
"""
*********
 *******
  *****
   ***
    *
"""
rows = 5
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))


# %% Problem 3: Diamond Pattern(Upper + Lower)
"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
rows = 5
#upper half
for i in range(1, rows+1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
#lower half
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# %% Pattern 4: Butterfly

"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

rows = 5
#upper part
for i in range(1, rows + 1):
    print('*' * i + ' ' * (2 * (rows - i)) + '*' * i)
#lower part
for i in range(rows, 0, -1):
    print('*' * i + ' ' * (2 * (rows - i)) + '*' * i)


# %% Pattern 5: Right Triangle
"""
*
**
***
****
*****
"""
rows = 5
for i in range(1, rows+1):
    print('*' * i)


# %% Pattern 6: Inverted Right Triangle(Upside Down)
"""
*****
****
***
**
*
"""
rows = 5
for i in range(rows, 0, -1):
    print('*' * i)

# %% Problem 7: Hollow square (or box)
"""
*****
*   *
*   *
*   *
*****

"""
rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print('*' * rows)
    else:
        print('*' + " " * (rows - 2) + '*')

# %% Problem 8: 5x5 square of asterisks
"""
*****
*****
*****
*****
*****

"""
rows = 5
for i in range(rows):
    print('*' * rows)


# %%
