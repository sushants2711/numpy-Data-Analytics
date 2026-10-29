import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

rs1 = np.stack((arr1, arr2))
print(rs1)

print("---- ---- ---- ---- ---- ----")

rs2 = np.stack((arr1, arr2), axis=0)
print(rs2)

print("---- ---- ---- ---- ---- ----")

rs3 = np.stack((arr1, arr2), axis=1)
print(rs3)