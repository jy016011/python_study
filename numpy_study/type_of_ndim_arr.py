import numpy as np

# float64 array
arr = np.array([1, 2, 3], dtype=np.float_)
print(arr, arr.dtype)

# int64 array
arr = np.array([1.1, 2.2, 3.6], dtype=np.int_)
print(arr, arr.dtype)

# bool array
arr = np.array([0, 1, 1], dtype=np.bool_)
print(arr, arr.dtype)

# change type
arr = arr.astype(np.float32)
print(arr, arr.dtype)

# case: mixed data type input
arr = np.array([1, 2, 3.4])
# then: types of all elements all the same
print(arr, arr.dtype)
arr = np.array([1, 2, 3.4, "64"])
print(arr, arr.dtype)



