L = [3, 8, 2, 7, 6, 10, 9]
L2 = sorted(L)
print(L2)
# >> [2, 3, 6, 7, 8, 9, 10]
print(L)
# >> [3, 8, 2, 7, 6, 10, 9]
L.sort()
print(L)
# >> [2, 3, 6, 7, 8, 9, 10]

L = ['abcd', 'xyz', 'spam']
print(sorted(L, key=lambda x: len(x))) # 길이 순 정렬
# >> ['xyz', 'abcd', 'spam']

# 선형 탐색
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    return -1

# 이진탐색
def binary_search(L, x):
    # L은 크기 순으로 이미 정렬되어있음
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if L[mid] < x:
            lower = mid + 1
        elif L[mid] > x:
            upper = mid - 1
        else:
            return mid
    return -1

from max_heap import MaxHeap
def heapSort(unsorted):
    H = MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted_arr = []
    data = H.remove()
    while data:
        sorted_arr.append(data)
        data = H.remove()
    return sorted_arr