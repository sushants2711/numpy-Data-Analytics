import numpy as np

arr = np.array([1,2,3,4])

# axis=0 is only possible in 1d array 
rs1 = np.split(arr, 2)
print(rs1)

print("---- ---- ---- ---- ")

arr2 = np.array([ [1,2,3,4], [5,6,7,8]])

print(np.split(arr2, 2))

print("---- ---- ---- ---- ")

print(np.split(arr2, 2, axis=0))

print("---- ---- ---- ---- ")

print(np.split(arr2, 2, axis=1))