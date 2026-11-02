import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 50, 30, 20, 100])

# result = np.sort(arr)

# print(result)

# print("---- ---- ----")

# print(arr)

# print("---- ---- ----")

# arr.sort()

# print(arr)

# print("decending array using np.sort()")

# print(np.sort(arr)[:: -1])

# print("decending array using arr.sort()")

# arr.sort()
# print(arr[::-1])


# reverse an array

# res = arr[:: -1]

# print(res)

arr2 = np.array([
    [10, 30, 40, 2],
    [22, 33, 1, 43]
])

print(np.sort(arr2))  # by default column wise 

print("---- ---- ----")

print(np.sort(arr2, axis=0)) # row wise

print("---- ---- ----")

print(np.sort(arr2, axis=1)) # column wise

