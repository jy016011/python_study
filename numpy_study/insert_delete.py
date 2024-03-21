import numpy as np

arr = np.arange(1, 9)
print(arr)
arr = np.insert(arr, 2, 50)
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr, arr.shape)
arr = np.insert(arr, 2, 50, axis=0)
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr, arr.shape)
arr = np.insert(arr, 2, 50, axis=1)
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr, arr.shape)
# without axis param, change to 1-dim array and insert
arr = np.insert(arr, 2, 50)
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr)
arr = np.delete(arr, 2, axis=0)
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr)
arr = np.delete(arr, 2, axis=1)
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr)
# without axis param, change to 1-dim array and delete
arr = np.delete(arr, 2)
print(arr)