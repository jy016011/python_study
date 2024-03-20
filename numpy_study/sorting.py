import numpy as np

arr = np.random.randint(10, size=10)
print(arr)
print(np.sort(arr))
print(np.sort(arr)[::-1])
print(arr)
# arr = np.sort(arr)
# print(arr)
arr.sort()
print(arr)

arr = np.random.randint(15, size=(3, 4))
print(arr)
print(np.sort(arr))
print(np.sort(arr, axis=0))
print(np.sort(arr, axis=None))

print(np.sort(arr, axis=1))
print(np.argsort(arr, axis=1))

print(np.sort(arr, axis=0))
print(np.argsort(arr, axis=0))