# randn() - It generates random numbers from a standard normal distribution.

# 1D → 5 values
# np.random.randn(5)

# 2D → 2 rows, 3 columns
# np.random.randn(2, 3)

# 3D → 2 × 3 × 4
# np.random.randn(2, 3, 4)

# 2 → number of blocks
# 3 → rows in each block
# 4 → columns in each row

import numpy as np

arr = np.random.randn(5)

print(arr)

print(np.random.randn(2, 3, 4))