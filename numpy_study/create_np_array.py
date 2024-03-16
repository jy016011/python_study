import numpy as np

# 1dim array
arr = np.array([1, 2, 3])
print(arr)

# 2dim array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)

print(type([1,2,3]))
print(type(arr))

tpl = (4, 5, 6)
arr = np.array(tpl)
print(arr)

lst = [1, 2, 3]
arr = np.array(lst)
print(arr)

lst2 = [[1, 2, 3], [4, 5, 6]]
arr2 = np.array(lst2)
print(arr2)

# shape
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1.shape)
print(arr2.shape)

# ndim
print(arr1.ndim)
print(arr2.ndim)

# size
print(arr1.size, arr2.size)