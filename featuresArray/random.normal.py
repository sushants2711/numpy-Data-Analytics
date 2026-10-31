# normal() generates random numbers according to a normal (bell-shaped) distribution.

# syntax

# np.random.normal(loc=0, scale=1, size=None)

# loc → mean (center)
# scale → standard deviation (spread)
# size → number or shape of values for 2d array pass in the bracket (2, 3) like so on

import numpy as np

arr = np.random.normal(loc=50, scale=10, size=4)
print(arr)
