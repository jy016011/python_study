import numpy as np

"""
Basic operations
"""
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
arr2 = np.full((3, 3), 2)
print(arr1)
print(arr2)

# addition
print(arr1 + arr2)
print(np.add(arr1, arr2))

# subtraction
print(arr1 - arr2)
print(np.subtract(arr1, arr2))

# multiplication, not product
print(arr1 * arr2)
print(np.multiply(arr1, arr2))

# division
print(arr1 / arr2)
print(np.divide(arr1, arr2))

# power
print(arr1 ** 2)
print(np.square(arr1))

# square root
print(np.sqrt(arr1))

# quotient
print(arr1 // 2)

# modular
print(arr1 % 2)


"""
Dot product
"""
# 1-dim
arr1 = np.array([2, 3, 4])
arr2 = np.array([1, 2, 3])
print(np.dot(arr1, arr2))

# 2dim
'''
[[a, b] [[e, f]    [[ae + bg, af + bg]  
[c, d]] [g, h]] => [ce + dg, cf + dh]]
'''
arr1 = np.array([[1, 2],
                 [4, 5]])
arr2 = np.array([[1, 2],
                 [0, 3]])
print(np.dot(arr1, arr2))

"""
Abs, ceil, floor, round, trunc
"""
# absolute
arr1 = np.array([[1, -2],
                 [-4, 5]])
print(np.abs(arr1))

# ceil
arr1 = np.array([[1.932, -2.339],
                 [-4.145, 5.206]])
print(np.ceil(arr1))

#floor
print(np.floor(arr1))

#round
print(np.round(arr1))

#trunc
print(np.trunc(arr1))

"""
Min, max, sum, mean, standard Deviation, cumulative sum, median
"""
# min
arr = np.array([[1, 2, 3],
               [0, 1, 4]])
print(np.min(arr))
print(arr.min())
print(arr.min(axis=0))
print(arr.min(axis=1))

# max
print(np.max(arr))
print(arr.max())
print(arr.max(axis=0))
print(arr.max(axis=1))

# sum
print(np.sum(arr))
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))

# mean
print(np.mean(arr))
print(arr.mean())
print(arr.mean(axis=0))
print(arr.mean(axis=1))

# standard Deviation
print(np.std(arr))
print(arr.std())
print(arr.std(axis=0))
print(arr.std(axis=1))

# cumulative sum
print(np.cumsum(arr))
print(arr.cumsum())
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))

# median
# 원소가 짝수개 일 경우 가운데 두 값 사이의 값을 반환
print(np.median(arr))

arr = np.array([[1, 2, 3],
               [0, 1, 4],
                [1, 5, 2]])
print(np.median(arr, axis=0))
print(np.median(arr, axis=1))

"""
Comparison operation, trigonometry
"""

# Comparison operations
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr2 = np.array([[1, 0, 3],
                 [4, -2, 9]])
print(arr1 == arr2)
print(arr1 > arr2)
print(np.array_equal(arr1, arr2))

# trigonometry
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))
print(np.pi)

"""
Broadcasting operation for between different shape matrix
"""

arr1 = np.array([[0, 0, 0],
                 [1, 1, 1],
                 [2, 2, 2]])
arr2 = np.array([5, 6, 7])
print(arr1 + arr2)

arr1 = np.array([1, 1, 1])
arr2 = np.array([[0],
                 [1],
                 [2]])
print(arr1 + arr2)

"""
Advantages of vector operations: much better performance than basic loop
"""
import time
# arr = np.arange(99999999)
#
# # loop
# sum_val = 0
# before = time.time()
# for i in arr:
#     sum_val += i
# after = time.time()
# print(sum_val, after - before, "sec")
#
# # vector operation
# before = time.time()
# sum_val = np.sum(arr)
# after = time.time()
# print(sum_val, after - before, "sec")

arr1 = np.arange(99999999)
arr2 = np.arange(99999999)

# loop
sum_val = 0
before = time.time()
for i, j in zip(arr1, arr2):
    sum_val += i * j
after = time.time()
print(sum_val, after - before, "sec")

# vector operation
before = time.time()
sum_val = np.dot(arr1, arr2)
after = time.time()
print(sum_val, after - before, "sec")