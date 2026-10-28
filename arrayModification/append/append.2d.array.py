import numpy as np

arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])


# append a single value in 2d array

# axis = 0 row wise append
arr1 = np.append(arr, [[1000, 2000]], axis=0)

print(arr1)

print("---- ---- ----")

# axis = 1 column wise append
arr2 = np.append(arr, [[12], [13], [14]], axis=1)

print(arr2)

print("---- ---- ----")

# append a multiple value in 2d array

# axis = 0 row wise append
arr3 = np.append(arr, [[100, 200], [300, 400]], axis=0)

print(arr3)

print("---- ---- ----")

# axis = 1 column wise append
arr4 = np.append(arr,[ [100, 200], [300, 400], [500, 600] ], axis=1)

print(arr4)