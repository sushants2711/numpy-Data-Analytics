# aggregation - Aggregation in NumPy means combining multiple values of an array into a single summary value.

import numpy as np 

arr = np.array([10, 20, 70, 40, 50])

print(np.sum(arr))

print(np.mean(arr))

print(np.median(arr))

print(np.min(arr))

print(np.max(arr))

print(np.std(arr))  # Standard deviation is simply the square root of variance.


# so how the std is working 

"""
    first it is calculate difference from means 
    10 - 38 = -28
    20 - 38 = -18
    70 - 38 = 32
    40 - 38 = 2
    50 - 38 = 12

    after this calculate the square root of every value 

    784, 324, 1024, 4, 144

    than sum the total value 

    (784 + 324 + 1024 + 4 + 144) = 2280

    And than divind the total number of value count 

    2280 / 5 = 456

    After that find the root of the var
"""

print(np.var(arr))  # Variance tells you how far the values are spread from the mean, using squared differences.

# so how the var is working 

"""
    first it is calculate difference from means 
    10 - 38 = -28
    20 - 38 = -18
    70 - 38 = 32
    40 - 38 = 2
    50 - 38 = 12

    after this calculate the square root of every value 

    784, 324, 1024, 4, 144

    than sum the total value 

    (784 + 324 + 1024 + 4 + 144) = 2280

    And than divind the total number of value count 

    2280 / 5 = 456
"""

a = np.array([10, 20, 30, 40, np.nan])

print(np.mean(a)) # it only return the average when there are all the value is a number if any empty value comes it throw NaN in the result

print(np.nanmean(a)) # it will return the average if the null value is exist or without null value also  

print("----")

print(np.median(a)) 