# ndim - (no of dimension) -- It will return the total number of dimension

import numpy as np

arr = np.array([1,2,3])

print(arr.ndim)

arr2 = np.array([
    [1,2,3],
    [3,4,4],
    [5,5,6]
])

print(arr2.ndim)