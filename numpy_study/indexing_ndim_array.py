import numpy as np

"""
Access to array index
"""
arr = np.arange(10)
print(arr)
print(arr[3])
print(arr[-1])
print(arr[-3])
print(arr[-10])
print(arr[3:8])

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr, arr.shape, arr.ndim)
print(arr[0][3])
print(arr[0, 3])
print(arr[0, :])
print(arr[:, 1])
print(arr[:3, :])
print(arr[:2, 2:])

"""
Fancy indexing
"""
arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[[0, 2, 4]])

arr = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60]
])
print(arr[[0, 2], 2:])
print(arr[1:, [2, 3]])

"""
Boolean indexing
"""
arr = np.array([1, 2, 3, 4])
print(arr[[True, False, True, True]])

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(arr[[True, False], True])
print(arr[arr > 3])
print(arr[arr <= 2])