# Python_study

### 파이썬 개인 학습 레포입니다.

---

## 1. [프로그래머스: 파이썬을 파이썬답게](https://school.programmers.co.kr/learn/courses/4008/4008-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%8B%B5%EA%B2%8C)

### 1) 몫과 나머지 - divmod

`divmod(x, y)`: 복소수가 아닌 두 숫자를 인자로 전달받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 `tuple` 형식으로 반환
```python3
a = 7
b = 5
print(divmod(a, b))
>> (1, 2)
print(*divmod(a, b)) # unpacking
>> 1 2
```

가독성에 따라 `a // b a % b`가 더 나을 수 있음

`divmod`는 작은 숫자를 다룰 때는 `a // b a % b`보다 느림

반대로 큰 숫자를 다룰 떄는 속도가 더 빠름.(숫자가 더 커질 수록 차이는 더 커짐)

속도 관련 자세한 내용은 [1] 을 참조

### 2) n진법으로 표기된 string을 10진법 수로 변환

```python
num = '444'
base = 5
answer = int(num, base)
>> 124
```

### 3) 문자열 정렬하기

```python
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

```

### 4) 알파벳 출력하기 - string 모듈

```python
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```

### 5) 2차원 리스트 뒤집기 - zip 이용

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
>> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```
`zip(*iterables)`는 iterables의 요소들을 모으는 이터레이터를 만듦

`tuple`형식의 이터레이터를 돌려주는데, i번째 튜플은 각 인자로 전달된 sequence/iterable의 i번째 요소를 포함
```python
mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
```

key 리스트와 value 리스트로 딕셔너리 생성하기
```python
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

인덱싱 없이 동시에 다른 인덱스 원소 접근하기
```python
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
>> [35, 35, 9, 67, 60]
```

### 6) Cartesian product 구하기

```python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
print(list(itertools.product(iterable1, iterable2)))
>> [('A', 'x'), ('A', 'y'), ('B', 'x'), ... , ('D', 'y')]
```

### 7) 2차원 리스트를 1차원 리스트로 만들기

```python
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))
```

다음은 제한적으로 각 원소의 길이가 동일한 경우에 사용 가능한 방법

```python
# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
```

### 8) 순열과 조합 - combinations, permutations

```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 순열 만들기
print(list(map(''.join, itertools.combinations(pool)))) # 3개의 원소로 조합 만들기
print(list(map(''.join, itertools.combinations(pool, 2)))) # 2개의 원소로 조합 만들기
```

### 9) flag 대신 for-else

```python
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    # break를 만나지 않고, for문이 완전히 다 수행된 후 종료되었을 때 출력            
    else:
        print('not found')
```

### 10) 이진 탐색 모듈 bisect

```python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 7))
>> 4
```

### 11) 가장 큰 수, inf

```python
max_val = float('inf')
max_val > 10000000000 # 어떠한 수가 오더라도 참 

min_val = float('-inf')
min_val < -10000000000 # 어떠한 수가 오더라도 참
```

### 12) 파일 입출력 간단하게 하기

```python
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
```

`with - as`구문을 이용하면 코드를 간결하고, 파일을 `close()` 하지 않아도 됨(`with - as`종료시 파일이 자동으로 close)

`readlines()`가 EOF까지만 읽으므로, EOF를 일일히 체크해줄 필요 없음 



[1]: (https://stackoverflow.com/questions/30079879/is-divmod-faster-than-using-the-and-operators)


---

## 2. numpy 모듈

### 1) numpy 왜 쓸까?

 - 리스트보다 훨씬 연산이 빠르다
   - 파이썬의 순서형 데이터 객체들은 컴퓨터 메모리에 연속되지 않은 곳에 저장되는 반면, `numpy`의 array 데이터 객체는 메모리에 연속되어 저장
     - 메모리 접근하는 속도가 더 빠르다(데이터 지역성)
     - SIMD(Single Instruction Multi Data: 하나의 명령어로 여러개의 데이터 처리) 지원
   - numpy함수는 C/C++로 제작이 되어 Python 내장함수에 비해 수행되는 명령어가 적음
 - 대용령의 배열과 행렬연산을 빠르게 수행한다.
 - 고차원적인 수학 연산자와 함수를 포함하고 있다.
 - 데이터 분석을 위한 패키지인 pandas나 기계학습을 위한 scikit-learn, tensorflow 등이 numpy를 기본 자료형으로 사용하여 동작 