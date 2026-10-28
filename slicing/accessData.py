import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])


print(arr[0: 2])

print(arr[0: 5: 2])

print(arr[:: -1])


arr2 = np.array([
    [10,11,12],
    [13,14,15],
    [16,17,18]
])

print(arr2[0: 1, 0:3])