import numpy as np
"""
Create an N-dim array of a given format
"""
# create 2 x 2 zeros matrix
arr = np.zeros([2, 2])
print(arr)

# create 3 x 3 ones matrix
arr = np.ones([3, 3])
print(arr)

# create 2 x 3 fives matrix
arr = np.full((2, 3), 5)
print(arr)

# create 3 x 3 unit matrix
arr = np.eye(3)
print(arr)

# create 3 x 4 diagonal matrix
arr = np.eye(3, 4, k=0)
print(arr)
arr = np.eye(3, 4, k = 1)
print(arr)
arr = np.eye(3, 4, k = -1)
print(arr)

# copy shape
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
arr_z = np.zeros_like(arr)
print(arr_z)
arr_o = np.ones_like(arr)
print(arr_o)
arr_f = np.full_like(arr, 7)
print(arr_f)

"""
Create an N-dim array with values in a specific range
"""
# np.arange(start, stop, step)
arr = np.arange(9)
print(arr)
arr = np.arange(3, 12)
print(arr)
arr = np.arange(3, 13, 3)
print(arr)

arr = np.linspace(0, 100, 11)
print(arr)

arr = np.linspace(1, 10, 10)
print(arr)
arr = np.logspace(1, 10, 10, base=2)
print(arr)
arr = np.logspace(1, 10, 10)
print(arr)

"""
Create an N-dim array with random values
"""

import matplotlib.pyplot as plt


# 정규 분포 난수 생성
arr = np.random.normal(0, 1, (2, 3))
print(arr)
arr = np.random.normal(0, 1, 1000000)
plt.hist(arr, bins=100)
plt.show()

# 0 ~ 1의 값을 균등한 비율로 표본 추출
arr = np.random.rand(1000)
plt.hist(arr, bins=100)
plt.show()

# -1 ~ 1 사이의 값을 정규 분포의 표본으로 추출
arr = np.random.randn(1000)
plt.hist(arr, bins=100)
plt.show()

# 랜덤한 정수 생성, low이상 high미만의 값을 size만큼 선택
arr = np.random.randint(low=1, high=5, size=10)
print(arr)
arr = np.random.randint(low=1, high=5, size=(3, 4))
print(arr)
arr = np.random.randint(100, 200, 1000)
plt.hist(arr, bins=100)
plt.show()

"""
Random number generation control using seed value
"""
np.random.seed(1)
arr = np.random.rand(10)
print("난수 발생1 \n", arr)

np.random.seed(1)
arr = np.random.rand(10)
print("난수 발생2 \n", arr)