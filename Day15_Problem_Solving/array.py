#  %% Problem 1: Move Zeros (Fixed Array Constraint)
"""The Problem:
Given an integer array nums, move all 0s to the end of it while maintaining the 
relative order of the non-zero elements.

Constraint: You must do this in-place without making a copy of the array. 
You must treat the array as a fixed-size array, meaning you cannot use Python's 
built-in .append(), .remove(), or .pop() methods to change its length."""

def move_zeroes(nums):
    # This pointer will track where the next non-zero element should go
    insert_position = 0
    
    # Step 1: Shift all non-zero elements to the front of the fixed array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_position] = nums[i]
            insert_position += 1
            
    # Step 2: Fill the remaining positions at the end with zeros
    for i in range(insert_position, len(nums)):
        nums[i] = 0
        
    return nums

# --- Testing the code ---
fixed_array = [0, 1, 0, 3, 12]
print("Result:", move_zeroes(fixed_array)) 



# %%
