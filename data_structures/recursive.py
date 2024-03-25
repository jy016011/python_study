import time
def recursive_fibo(x):
    if x <= 1:
        return x

    return recursive_fibo(x - 1) + recursive_fibo(x - 2)

def iterative_fibo(x):
    if x <= 1:
        return x

    fibo = [0, 1]
    answer = 0
    for n in range(2, x + 1):
        answer = fibo[n - 2] + fibo[n - 1]
        fibo.append(answer)

    return answer

before = time.time()
answer = iterative_fibo(40)
elapsed = (time.time() - before)
print("Iterative: sum {}, time {:.3f}".format(answer, elapsed))
before = time.time()
answer = recursive_fibo(40)
elapsed = (time.time() - before)
print("Recursive: sum {}, time {:.3f}".format(answer, elapsed))
def recursive_binsearch(L, x, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + upper) // 2
    if L[mid] == x:
        return mid
    if L[mid] > x:
        return recursive_binsearch(L, x, lower, mid - 1)
    return recursive_binsearch(L, x, mid + 1, upper)