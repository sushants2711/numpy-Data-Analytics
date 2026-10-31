# permutation() - randomly rearranges the elements of an array
# and returns a new array without modifying the original array.

# syntax

# np.random.permutation(x) - x is an array 

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

arr2 = np.random.permutation(arr)

print(arr2)