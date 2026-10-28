import numpy as np

arr = np.array([
    [10, 20],
    [30, 40]
])

# insert a single value 

# axis = 0 row wise
newArr1 = np.insert(arr, 1, [100, 200], axis=0)
print(newArr1)


print("---- ---- ---- ----")


# axis = 1 column wise
newArr2 = np.insert(arr, 1, [100, 200], axis=1)
print(newArr2)

print("---- ---- ---- ----")

# insert a multiple value

# axis = 0 row wise
newArr3 = np.insert(arr, 1, [[1,2], [3,4]], axis=0)
print(newArr3)

# axis = 1 column wise
newArr4 = np.insert(arr, 1, [[1,2], [3,4]], axis=1)
print(newArr4)