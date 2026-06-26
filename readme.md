
## 파이썬 리스트(List)

**학습 목표**

* 리스트의 개념 이해
* 리스트 생성 및 사용법 익히기
* 리스트의 주요 함수 활용하기

---

# **슬라이드 2. 리스트(List)란?**

### 리스트의 특징

* 여러 개의 데이터를 하나의 변수에 저장하는 자료형
* 순서(인덱스)를 가진다.
* 데이터의 추가, 수정, 삭제가 가능하다.
* 서로 다른 자료형을 함께 저장할 수 있다.

```python
fruits = ["apple", "banana", "orange"]
```

---

# **슬라이드 3. 리스트 생성하기**

```python
numbers = [10, 20, 30, 40]

names = ["Tom", "Jane", "Mike"]

mixed = [10, "Python", 3.14, True]
```

빈 리스트 생성

```python
list1 = []

list2 = list()
```

---

# **슬라이드 4. 인덱스(Index)**

리스트는 **0부터 시작하는 번호(인덱스)**를 사용합니다.

```python
fruits = ["apple", "banana", "orange"]
```

| 인덱스 | 값      |
| :-: | :----- |
|  0  | apple  |
|  1  | banana |
|  2  | orange |

```python
print(fruits[0])   # apple
print(fruits[2])   # orange
```

---

# **슬라이드 5. 음수 인덱스와 슬라이싱**

### 음수 인덱스

```python
print(fruits[-1])    # orange
print(fruits[-2])    # banana
```

### 슬라이싱

```python
print(fruits[0:2])
```

출력

```
['apple', 'banana']
```

---

# **슬라이드 6. 리스트 수정 및 추가**

### 값 수정

```python
fruits[1] = "melon"
```

### 데이터 추가

```python
fruits.append("grape")
```

### 원하는 위치에 추가

```python
fruits.insert(1, "kiwi")
```

---

# **슬라이드 7. 리스트 삭제**

### 마지막 요소 삭제

```python
fruits.pop()
```

### 특정 위치 삭제

```python
fruits.pop(1)
```

### 값으로 삭제

```python
fruits.remove("banana")
```

### 모두 삭제

```python
fruits.clear()
```

---

# **슬라이드 8. 자주 사용하는 함수**

| 함수          | 설명         |
| ----------- | ---------- |
| `append()`  | 요소 추가      |
| `insert()`  | 원하는 위치에 추가 |
| `remove()`  | 값 삭제       |
| `pop()`     | 인덱스로 삭제    |
| `sort()`    | 오름차순 정렬    |
| `reverse()` | 순서 뒤집기     |
| `len()`     | 요소 개수      |
| `sum()`     | 합계(숫자 리스트) |
| `min()`     | 최솟값        |
| `max()`     | 최댓값        |

---

# **슬라이드 9. 반복문과 리스트**

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

출력

```
apple
banana
orange
```

또는 인덱스를 사용할 수도 있습니다.

```python
for i in range(len(fruits)):
    print(fruits[i])
```

---

# **슬라이드 10. 실습 문제**

### 실습 1

과일 리스트를 만들고

* 첫 번째 과일 출력
* 마지막 과일 출력

```python
fruits = ["apple", "banana", "orange", "melon"]

print(fruits[0])
print(fruits[-1])
```

### 실습 2

5개의 정수를 입력받아 리스트에 저장한 후

* 합계
* 평균
* 최솟값
* 최댓값을 출력해 보세요.


이 구성은 약 **30~40분 분량의 입문 강의**에 적합하며, 각 슬라이드에 그림(인덱스 구조), 실행 결과 화면, 간단한 실습을 추가하면 학습 효과를 높일 수 있습니다.

