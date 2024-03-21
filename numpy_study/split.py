import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
print(arr)

"""
vsplit(): split by axis=0, hsplit(): split by axis=1
"""
arr_vsplit = np.vsplit(arr,3)
print(arr_vsplit)

arr_hsplit = np.hsplit(arr,2)
print(arr_hsplit)

arr = np.random.randint(0, 10, (4, 6, 8))
print(arr)

arr_vsplit = np.vsplit(arr, 2)
print(arr_vsplit)

arr_hsplit = np.hsplit(arr, 2)
print(arr_hsplit)