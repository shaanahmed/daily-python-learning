# %% 1. The Warehouse Rounder
"""You are managing a warehouse. You have 142 items that need to be packed into boxes. Each box can hold exactly 12 items.
A. Use a Python function to find out how many full boxes you can pack.
B. Use the math module to find out how many boxes you need in total to ensure every item is in a box (even if the last box isn't full).
C. Use the modulo operator to find out how many items will be left over in that final partially-filled box."""

import math

total_items = 142
items_per_box = 12

# Number of full boxes that can be packed
def get_full_box(total_items, items_per_box):
    return total_items // items_per_box

full_boxes = get_full_box(total_items, items_per_box)
print(f"A. Full boxes that can be packed: \n {full_boxes}")

# Number of boxes needed in total to ensure every item is in a box
total_boxes_needed = math.ceil(total_items / items_per_box)
print(f"Number of boxes needed in total to ensure every item is in a box: \n {total_boxes_needed}")

# Items will be left in the final partially filled box
last_box_items = total_items % items_per_box
print(f"Items will be left in the final partially filled box: \n {last_box_items}")


# %% 2. The Logistical Exponent
"""Suppose you know that 2^x = 65536.
Write a script using the math module to recover the value of x.
Bonus: Ensure the result is an integer using the round() function."""

import math

value = 65536
# I am using logarithms to solve this
x = math.log(value, 2)
print("the math module to recover the value of exponent x: ", round(x), sep="\n")


# %% 3. The Pizza Slice Calculator
"""You have a circular pizza with a radius of 15cm.
A. Calculate the total area of the pizza (Area = pi r^2) using math.pi and math.pow().
B. If you cut the pizza into 8 equal slices, what is the area of a single slice? 
Round your final answer to 2 decimal places."""
import math

pizza_radius = 15
number_of_slices = 8

total_area_of_pizza = math.pi * math.pow(pizza_radius, 2)
print(total_area_of_pizza)

area_of_single_slice = total_area_of_pizza / number_of_slices
print(round(area_of_single_slice, 2))

# %% 4. Trigonometry Challenge
"""A ladder is leaning against a wall at an angle of 60 degrees.
Python’s math.cos() and math.sin() functions expect radians, not degrees.
Convert the 60-degree angle to radians using a math function.
Calculate the cosine of that angle."""

import math

angle_degrees = 60

# Converting degree to radians
angle_radians = math.radians(angle_degrees)
print(f" math.radians({angle_degrees}) = {angle_radians}")

# Calculating the cosine of the angle
cosine_value = math.cos(angle_radians)
print(f"  math.cos({angle_radians}) = {round(cosine_value, 1)}")



# %% 5. Extreme Values
"""Given the list of numbers: [ -15, 0.5, 42, -100, 3.14 ]
A. Use built-in functions to find the largest and smallest numbers in the list.
B. Use a function to find the absolute value of the smallest number."""

list_of_num = [ -15, 0.5, 42, -100, 3.14 ]

# Using Built in function to find largest and smallest number in the list
largest = max(list_of_num)
print(largest)
smallest = min(list_of_num)
print(smallest)

# Finding the absolute value of the smallest number
abs_value = math.fabs(smallest)
print("The absolute value of the smallest number is:", abs_value, sep="\n")


# %%
