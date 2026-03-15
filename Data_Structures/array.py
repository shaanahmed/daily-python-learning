#
import array as arr

# 1. Initialize an array of integers ('i' stands for signed integer)
# This is more memory-efficient than a standard Python list.
numbers = arr.array('i', [10, 20, 30, 40, 50])

print(f"Initial Array: {numbers.tolist()}")

# 2. Accessing elements (O(1) complexity)
print(f"Element at index 2: {numbers[2]}")

# 3. Insertion (O(n) complexity)
# Inserting 25 at index 2
numbers.insert(2, 25)
print(f"After Insertion: {numbers.tolist()}")

# 4. Deletion (O(n) complexity)
# Removing the value 40
numbers.remove(40)
print(f"After Deletion: {numbers.tolist()}")

# 5. Searching (O(n) complexity for Linear Search)
def search_element(arr_obj, target):
    for i in range(len(arr_obj)):
        if arr_obj[i] == target:
            return f"Value {target} found at index {i}"
    return "Value not found"

print(search_element(numbers, 30))

# 6. Updating (O(1) complexity)
numbers[0] = 100
print(f"After Update: {numbers.tolist()}")