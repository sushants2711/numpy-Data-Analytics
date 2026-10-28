# flatten() - flatten() returns a new, independent copy of the array converted into one dimension.

# Means if we change the element of an array in the new array that old array dont get affected.


import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

new_arr = arr.flatten()

print(new_arr)

new_arr[0] = 9090

print(arr)

print(new_arr)


