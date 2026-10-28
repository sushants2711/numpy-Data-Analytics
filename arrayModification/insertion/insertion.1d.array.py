import numpy as np

arr = np.array([10, 20, 30])

# insert a single value in 1d array
newArr = np.insert(arr, 1, 400)

print(newArr)

# insert a multiple value in 2d array
newArr2 = np.insert(arr, 1, [100, 200, 300])

print(newArr2)