import numpy as np

arr = np.array([10, 20, 30, 40, 50, 50, 30, 20, 100])

result = np.unique(arr)

print(result)

print("---- ---- ---- ----")

values, counts = np.unique(arr, return_counts=True)

print(values)

print(counts)