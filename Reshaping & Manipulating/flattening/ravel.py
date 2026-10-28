""" 
    ravel() - ravel() returns a 1D view of the array whenever possible, rather than creating a separate copy.

    Means if we change the element of an array in the new array that old array get affected.
"""

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

new_arr = arr.ravel()

print(arr)

print(new_arr)

print("---- ---- ---- ----")

new_arr [0] = 9090

print(arr)

print(new_arr)