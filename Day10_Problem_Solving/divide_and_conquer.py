# %% 1. Divide and Conquer Sum of numbers in an array

def calc_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    #DIVIDE
    mid = len(arr) // 2

    #CONQUER : Recursively solve the left and right halves
    left_sum = calc_sum(arr[:mid]) 
    right_sum = calc_sum(arr[mid:]) 

    # COMBINE: Adding the two halves together
    return left_sum + right_sum

print(calc_sum([1, 4, 2, 8, 3, 1, 6]))


# %%
