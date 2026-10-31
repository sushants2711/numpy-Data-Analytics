import numpy as np

# empty() - creates an array without initializing its values.
# It is useful when we want to create an array first
# and fill it with values later.

arr = np.empty(5)

print(arr)


for i in range(5):
    arr[i] = i * 20

print(arr)