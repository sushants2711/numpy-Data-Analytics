# uniform() generates random numbers from a uniform distribution.
# That means values within the given range have roughly equal probability.

# syntax

# np.random.uniform(low=0.0, high=1.0, size=None)

# low → starting/lowest value
# high → upper limit (not included)
# size → number or shape of values

import numpy as np 

arr = np.random.uniform(10, 100, 5)

print(arr)

