L = ['Bob', 'Cat', 'Spam', 'Programmers']
print(L)
# >> ['Bob', 'Cat', 'Spam', 'Programmers']
print(L[1]) # indexing
# >> Cat
print(L[-2])
# >> Spam

# 1. 덧붙이기: O(1) 소요
L.append('New')
print(L)
# >> ['Bob', 'Cat', 'Spam', 'Programmers', 'New']

# 2. 끝에서 꺼내기: O(1) 소요
print(L.pop())
# >> New
print(L)
# >> ['Bob', 'Cat', 'Spam', 'Programmers']

# 3. 원소 삽입하기: O(n) 소요
L = [20, 37, 58, 72, 91]
L.insert(3, 67)
print(L)
# >> [20, 37, 58, 67, 72, 91]

# 4. 원소 삭제하기: O(n) 소요
del(L[2])
print(L)
# >> [20, 37, 67, 72, 91]
print(L.pop(2))
# >> 67
print(L)
# >> [20, 37, 72, 91]

# 5. 원소 탐색하기
L = ['Bob', 'Cat', 'Spam', 'Programmers']
print(L.index('Spam'))
# >> 2

# 실습문제 #1: 리스트 원소 합
def solution1(x):
    return x[0] + x[-1]

# 실습문제 #2: 정렬된 리스트에 원소 삽입
def solution2(L, x):
    for index in range(len(L)):
        if L[index] >= x:
            L.insert(index, x)
            break
    else:
        L.append(x)
    return L

# 실습문제 #3: 리스트에서 원소 찾아내기
def solution3(L, x):
    answer = []
    idx = -1
    try:
        while True:
            idx += (L[idx + 1:].index(x) + 1)
            answer.append(idx)

    except ValueError:
        if not answer:
            answer.append(-1)

    return answer
