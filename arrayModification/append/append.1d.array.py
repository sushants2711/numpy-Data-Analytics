import numpy as np

arr = np.array([10, 20, 30])

# append a single value in 1d array
newArr1 = np.append(arr, 100)

print(newArr1)


# append multiple value in 1d array
newArr2 = np.append(arr, [100, 200, 2000])

print(newArr2)