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

# %%
