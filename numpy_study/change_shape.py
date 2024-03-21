import numpy as np

arr = np.arange(12)
print(arr, arr.ndim)

# 3 x 4 matrix
arr = arr.reshape((3, 4))
print(arr, arr.ndim)

# 2 x 3 x 2 matrix
arr = arr.reshape((2, 3, 2))
print(arr, arr.ndim)

# 2 x 2 x 1 x 3 matrix
arr = arr.reshape((2, 2, 1, 3))
print(arr, arr.ndim)

"""
참고 사항: Curse of Dimensionality
차원에 비해 데이터 양이 적어지면서 모델의 성능이 저하되는 현상
"""

# 3 x 4 matrix, change target array
arr.resize(3, 4)
print(arr)

# change to 1-dim
arr = arr.ravel()
print(arr)

arr = np.arange(1, 13)
print(arr)
# auto shape
arr = arr.reshape(3, -1)
print(arr)
arr = arr.reshape(3, 2, -1)
print(arr)
"""
Raise ValueError: can only specify one unknown dimension
"""
# arr = arr.reshape(3, -1, -1)

"""
Expand dims and squeeze
"""

# expand
arr = np.array([1, 2])
print(arr, arr.shape)
# to 1 x 2
arr = np.expand_dims(arr, axis=0)
print(arr, arr.shape)
arr = np.array([1, 2])
# to 2 x 1
arr = np.expand_dims(arr, axis=1)
print(arr, arr.shape)

# squeeze
arr = np.array([[1, 2]]) # 1 x 2
print(arr, arr.shape, arr.ndim)
# remove '1' axis(index=0)
arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)

# 1 x 3 x 1
arr = np.array(([[
    [1],
    [2],
    [3]
]]))
print(arr, arr.shape, arr.ndim)
# to 3 x 1
arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)

# 1 x 1 x 3
arr = np.array([[[1, 2, 3]]])
print(arr, arr.shape, arr.ndim)
# to 1 x 3
arr = np.squeeze(arr, axis=1)
print(arr, arr.shape, arr.ndim)

# without axis param, squeeze will remove all axis which is 1
arr = np.array([[[1, 2, 3]]]) # 1 x 1 x 3
print(arr, arr.shape, arr.ndim)
# to 3, remove all axis value = '1'
arr = np.squeeze(arr)
print(arr, arr.shape, arr.ndim)

"""
Transposed Matrix
"""
arr = np.array([[1, 2],
                [3, 4]])
print(arr.T)
print(np.transpose(arr))
# not changed original matrix
print(arr)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(arr.T)

# 3 x 2
arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])
# 2 x 3 T matrix
print(arr.T)

arr2 = np.full((2, 3), 2)
print(arr2)
print(arr.dot((arr2)))