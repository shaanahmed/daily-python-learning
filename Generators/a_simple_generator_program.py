# %% generators 

def count_to_infinity(start):
    """A generator that counts up forever (without crashing your PC)."""
    while True:
        yield start  # This 'pauses' the function and sends the value out
        start += 1

# 2. Setup the generator
counter = count_to_infinity(10)

# 3. Execute instantly
print(next(counter))  # Output: 10
print(next(counter))  # Output: 11
print(next(counter))  # Output: 12

# You can also use it in a loop with a break
for num in counter:
    print(f"Looping: {num}")
    if num >= 15: 
        break

    
# %%
