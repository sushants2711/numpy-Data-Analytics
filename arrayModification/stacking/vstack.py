import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

rs1 = np.vstack((arr1, arr2))
print(rs1)

print("---- ---- ---- ---- ---- ----")

# for 2d array 
arr3 = np.array([[1, 2, 3], [4,5,6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])

rs2 = np.vstack((arr3, arr4))
print(rs2)