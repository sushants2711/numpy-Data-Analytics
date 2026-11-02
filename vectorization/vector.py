# vectorization - Vectorization means performing an operation on an entire NumPy array at once, instead of using a Python for loop to process each element individually

# without vectorization 

import numpy as np

arr = np.array([10, 20, 30, 40])

res = []

for x in arr:
    res.append(x * 10)

print(res)



# without vectorization

print("Printing the same data without vectorization")

arr2 = np.array([10, 20, 30, 40])

result = arr * 10

print(result)

