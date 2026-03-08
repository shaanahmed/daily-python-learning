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



# %% Problem 2: Build a Dynamic Array
"""
The Problem:
Python hides the complex math of resizing lists from you. Your task is to build a 
DynamicArray class from scratch using a simulated fixed array under the hood.

It must include:
An append(value) method.
A resize() method that doubles the capacity of the array when it gets full.
A get(index) method to retrieve values.
"""
class DynamicArray:
    def __init__(self, capacity=2):
        self.size = 0           # How many items are actually in the array
        self.capacity = capacity # How many items the array CAN hold
        # Simulating a fixed-size array in memory
        self.array = [None] * self.capacity 

    def get(self, index):
        # Ensure the user doesn't ask for an index out of bounds
        if index < 0 or index >= self.size:
            return "Error: Index out of bounds"
        return self.array[index]

    def append(self, value):
        # Step 1: Check if the array is full
        if self.size == self.capacity:
            self._resize()
            
        # Step 2: Add the new value and increase the size tracker
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        print(f"--> Array full! Resizing capacity from {self.capacity} to {self.capacity * 2}")
        
        # Double the capacity
        self.capacity *= 2
        
        # Create a new, larger fixed array
        new_array = [None] * self.capacity
        
        # Copy all old elements into the new array
        for i in range(self.size):
            new_array[i] = self.array[i]
            
        # Replace the old array with the new one
        self.array = new_array

# --- Testing the code ---
my_array = DynamicArray(capacity=2)

my_array.append(10)
my_array.append(20)
print("Current size:", my_array.size) # Array is now full!

# This 3rd append will trigger the automatic resize
my_array.append(30) 

print("Value at index 2:", my_array.get(2))
print("Internal memory array looks like:", my_array.array)
# %%
