import numpy as np

arr1 = np.arange(1, 13).reshape(3, 4)
arr2 = np.arange(13, 25).reshape(3, 4)
"""
append()
"""
print(arr1)
print(arr2, end="\n\n")

# axis=0
arr3 = np.append(arr1, arr2, axis=0)
print(arr3, end="\n\n")
# axis=1
arr3 = np.append(arr1, arr2, axis=1)
print(arr3, end="\n\n")
# without axis, change to 1-dim and append
arr3 = np.append(arr1, arr2)
print(arr3, end="\n\n")

"""
vstack(): merge by axis=0 , hstack() merge by axis=1
"""

arr1 = np.arange(1, 7).reshape(2, 3)
arr2 = np.arange(7, 13).reshape(2, 3)
arr3 = np.vstack((arr1, arr2))
print(arr3)

arr3 = np.hstack((arr1, arr2))
print(arr3)

"""
concatenate()
"""
arr1 = np.arange(1, 7).reshape(2, 3)
arr2 = np.arange(7, 13).reshape(2, 3)

arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)
arr3 = np.concatenate([arr1, arr2], axis=1)
print(arr3)