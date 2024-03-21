import numpy as np
"""
Practice #4: 다음과 같은 np.array가 존재한다. 이 배열을 행을 기준으로 3개의 배열로 분할하여
분할된 각 배열의 원소들을 제곱한 결과를 다시 원본 배열에 행을 기준으로 병합하시오
(단, 마지막 출력 결과는 원본 배열과 차원이 같아야한다.)
"""
arr = np.arange(2, 20, 2).reshape((3, 3))
arr1 = np.vsplit(arr, 3)
arr2 = np.square(arr1)
arr2 = arr2.squeeze()
arr = np.vstack((arr, arr2))
# for a in arr1:
#     arr = np.vstack((arr, a ** 2))
print(arr)

"""
Practice #5: 삼각함수의 특수각(0, 30, 60, 90)을 np.array로 생성한 후
특수각에 해당하는 sin, cos, tan 값을 각각 구하여
파이썬 list에 담은 다음 해당 list에 들어있는 값들을 출력하시오
(단, 값이 무한대라면 " INF"문자열을 출력할 것)
"""
arr = np.arange(0, 91, 30)
lst = []
lst.append(np.sin(arr * np.pi / 180))
lst.append(np.cos(arr * np.pi / 180))
lst.append(np.tan(arr * np.pi / 180))

for values in lst:
    for value in values:
        if value > 999999999:
            print('INF')
            continue
        print(value)
    print()

"""
Practice #6: np.array를 이용하여 바둑판 패턴을 출력하시오
(단, 출력시 반복문을 사용하여 출력한다.)
"""
arr = np.zeros((7, 7), np.int_)
# for K in range(-5, 6, 2):
#     arr += np.eye(7, 7, k=K, dtype=np.int_)
# print(arr)
arr[::2, 1::2] = 1
arr[1::2, ::2] = 1
for row in arr:
    for e in row:
        print(e, end=" ")
    print()


