import numpy as np

# diag -  It is used to find the diagonal from 2d array and created a diagonal from 1d array and fill all other spaces with zero


# it change 1d array into a diagonal 
arr = np.array([1,2,3,4])

print(np.diag(arr))

print("---- ---- ---- ---- ---- ---- ---- ----")


# it find the diagonal from 2d arrray
arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(np.diag(arr2))