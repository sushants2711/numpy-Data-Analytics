import numpy as np

arr1 = np.array([
    [10, 20],
    [30, 40]
])

arr2 = np.array([
    [50, 60],
    [70, 80]
])

# axis = 0 row wise
newArr1 = np.concatenate((arr1, arr2), axis=0)

print(newArr1)

# axis = 1 column wise
newArr2 = np.concatenate((arr1, arr2), axis=1)

print(newArr2)