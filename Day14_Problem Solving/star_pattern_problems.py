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


# %% Pattern 9: Hollow Diamond
"""

    *
   * *
  *   *
 *     *
  *   *
   * *
    *

"""
rows = 5
#upper part
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))
#lower part
for i in range(rows -1, 0, -1):
    print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))


# %% Pattern 10: Hollow Pyramid
"""

    *
   * *
  *   *
 *     *
*********

"""
rows = 5
for i in range(1, rows + 1):
    if i == rows:
        print('*' * (2 * i - 1))
    else:
        print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))


# %% Pattern 2: Left facing Right-Aligned Triangle
"""
    *
   **
  ***
 ****
*****

"""

rows = 5
for i in range(1, rows+1):
    print(' ' * (rows - i) + '*' * i)


# %%Pattern 3: X Pattern
"""

*   *
 * *
  *
 * *
*   *

"""

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == j or i + j == rows + 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# %% Star using star Pattern

import math

def main():
    # q is tan(72°), w is tan(36°)
    q = math.tan(math.pi * 0.4)
    w = math.tan(math.pi * 0.2)

    try:
        # Ask for input and convert it to a float
        n = float(input("Enter the size (try 15 for a good result):\n"))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Calculate the vertical (j) and horizontal (i) bounds
    height = math.ceil(n * q)
    width = math.ceil(0.55 * n * q / w - n)

    # j loops from top to bottom
    for j in range(height, -1, -1):
        
        # i loops from left to right. Added + 1 to fix the missing right edge!
        for i in range(-width, width + 1):
            
            # The three mathematical regions that draw the star
            arms      = (j <= 0.55 * n * q) and (j >= (i + n) * w) and (j >= (n - i) * w)
            left_leg  = (j >= (i + n) * w) and (j <= (i + n) * q) and (j <= (n - i) * q)
            right_leg = (j <= (n - i) * q) and (j >= (n - i) * w) and (j <= (i + n) * q)
            
            if arms or left_leg or right_leg:
                print("*", end="")
            else:
                print(" ", end="")
        
        # Move to the next line after finishing a row
        print()

if __name__ == "__main__":
    main()


# %%
