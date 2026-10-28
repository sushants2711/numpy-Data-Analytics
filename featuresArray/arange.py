# arange() is used to create an array of numbers with a specified range start, stop, and step.

# syntax

# np.arange(start, stop, step) 

# start - starting point
# stop - stopping point
# step - how many steps follow to get the next value it basically add the value 

import numpy as np

arr = np.arange(1, 10)  # the last number is n-1 it is not included

print(arr)

arr2 = np.arange(1, 10, 3) 

print(arr2)