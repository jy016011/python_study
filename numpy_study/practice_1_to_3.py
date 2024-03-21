import numpy as np

"""
Practice #1: 원소가 모두 3인 (3, 4, 5) 형태의 array 출력
"""
arr1 = np.full((3, 4, 5), 3)
print(arr1, arr1.shape)


"""
Practice #2: 정수 -50 ~ 50의 범위 안의 난수로 이루어진 (4,5) 형태의 array를 출력하고
행을 기준으로 오름차순 정렬한 결과와
전체 배열을 1차원 배열로 변경하여 오름차순 정렬한 결과룰 출력
"""
arr2 = np.random.randint(-50, 51, (4, 5))
print(arr2)
print(np.sort(arr2, axis=0))
print(np.sort(arr2, axis=None))

"""
Practice #3: 다음과 같은 list가 존재한다.
list안에 있는 각 np.array의 원소들의 평균값과 표준편차, 중앙값을 순서대로 구하여
구한 순서대로 원소가 이루어진 새로운 list를 구성하고 출력
예: 각 배열의 평균 값이 3.0, 4.0, 5.0 이고 표준편차가 1.5, 1.7, 1.9이며 중앙값이 1.0, 2.0, 3.0 이라면
답은 [3.0, 1.5, 1.0, 4.0, 1.7, 2.0, 5.0, 1.9, 3.0] 이다.
"""
py_list = [
    np.full(3, 8),
    np.array([33, -15, 26]),
    np.linspace(17, 26, 3)]
answer = []
for narray in py_list:
    answer.append(np.mean(narray))
    answer.append(np.std(narray))
    answer.append(np.median(narray))
print(answer)