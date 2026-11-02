import numpy as np

arr = np.array([10, 40, 300, 2, 23, 11])

result = np.where(arr > 30)

print(result)

result2 = np.where(arr > 30, 100, 0)

print(result2)