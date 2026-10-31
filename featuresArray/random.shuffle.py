# shuffle() - randomly rearranges the elements of an array in-place. It not return the new array

# syntax

# np.random.shuffle(arr) - the array that you want to rearrange

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])


np.random.shuffle(arr)

print(arr)