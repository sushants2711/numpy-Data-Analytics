# astype(new type) --  It is used to change the data type of the variable

import numpy as np

arr = np.array([1,2,3])

print(arr.dtype)

change_Arr = arr.astype(float)

print(change_Arr.dtype)