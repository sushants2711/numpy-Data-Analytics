import numpy as np

arr1 = np.array([
    [10, 20], [30, 40], [50, 60]
])

print(arr1)

print("---- ------------------- ---------------- -----------")

# delete single value from 2d array 

# axis = 0 row deleted 
newArr1 = np.delete(arr1,1, axis=0)
print(newArr1)

print("---- ------------------- ---------------- -----------")

# axis = 1 column deleted
newArr2 = np.delete(arr1,1, axis=1)
print(newArr2)

print("---- ------------------- ---------------- -----------")

# if we want to delete a single value form 2d aray first change to flattern else not use the axis 

newArr3 = np.delete(arr1, 2)
print(newArr3)

print("---- ------------------- ---------------- -----------")

# if we want to delete a multiple value form 2d aray first change to flattern else not use the axis 

newArr4 = np.delete(arr1, [2,3])
print(newArr4)

print("---- ------------------- ---------------- -----------")

# first convert to flat array and than 
flatArray = arr1.flatten()

# now delete the which value just pass the index
delFla1 = np.delete(flatArray, 0)

print(delFla1)

print("---- ------------------- ---------------- -----------")

# now delete the which value just pass the index
delFla2 = np.delete(flatArray, [0,1])

print(delFla2)