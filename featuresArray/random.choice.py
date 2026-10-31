# random.choice() - randomly selects values from an array.
# replace=True  -> values can repeat
# replace=False -> values cannot repeat

# syntax

# np.random.choice(a, size=None, replace=True, p=None)

# a → array or range from which to select we also pass directly range like in an array 10 length than pass 6 than first 6 count
# size → how many values to select (pass in bracket if 2d array)
# replace → whether values can repeat
# p → probability of selecting each value (optional) it takes an array

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,0,100])

arr2 = np.random.choice(arr, 5, replace=True)

print(arr2)