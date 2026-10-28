import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

# delete a single value pass the index number
newArr1 = np.delete(arr1, 1)

print(arr1)
print(newArr1)

# delete the multiple value by passing the index number
newArr2 = np.delete(arr1, [1,2,3,4])

print(arr1)
print(newArr2)  # delete the all array except the 0 index
