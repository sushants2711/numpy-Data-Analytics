import numpy as np

# if we do resize with arr.resize() -  it change the array and fill the extra value with 0 
# but while using the np.resize(arr, (value)) - so fill with the value with the repeating value itself

arr = np.array([10,20,30,40,50,60,70,80])

# arr.resize(2,6) 

# print(arr)

arr2 = np.resize(arr, (2,6))

print(arr2)