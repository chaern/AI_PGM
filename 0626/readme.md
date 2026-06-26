# 📦 Python Container

## 📌 Container란?

**Container(컨테이너)** 는 여러 개의 데이터를 하나의 객체에 저장하고 관리하는 자료형입니다.

파이썬에서는 다양한 컨테이너 자료형을 제공하며, 상황에 맞게 선택하여 사용할 수 있습니다.

대표적인 컨테이너는 다음과 같습니다.

| 자료형        | 생성 방법         | 순서              | 중복       | 수정 가능 |
| ---------- | ------------- | --------------- | -------- | ----- |
| List       | `[]`          | O               | O        | O     |
| Tuple      | `()`          | O               | O        | X     |
| Set        | `{}`          | X               | X        | O     |
| Dictionary | `{key:value}` | O (Python 3.7+) | Key 중복 X | O     |

---

# 📋 List (리스트)

여러 개의 데이터를 **순서대로 저장**하는 가장 많이 사용하는 컨테이너입니다.

```python
fruits = ["apple", "banana", "orange"]
```

### 특징

* 순서가 있다.
* 중복을 허용한다.
* 데이터 추가, 수정, 삭제가 가능하다.
* 다양한 자료형을 함께 저장할 수 있다.

### 예제

```python
numbers = [10, 20, 30]

print(numbers[0])

numbers.append(40)

print(numbers)
```

출력

```
10
[10, 20, 30, 40]
```

---

# 📋 Tuple (튜플)

리스트와 비슷하지만 **수정이 불가능(Immutable)** 한 자료형입니다.

```python
point = (10, 20)
```

### 특징

* 순서가 있다.
* 중복을 허용한다.
* 수정할 수 없다.

### 예제

```python
point = (100, 200)

print(point[0])
```

---

# 📋 Set (집합)

중복을 허용하지 않는 자료형입니다.

```python
numbers = {1, 2, 3}
```

### 특징

* 순서가 없다.
* 중복을 허용하지 않는다.
* 합집합, 교집합, 차집합 연산이 가능하다.

### 예제

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

출력

```
{1, 2, 3}
```

---

# 📋 Dictionary (딕셔너리)

**Key : Value** 형태로 데이터를 저장합니다.

```python
student = {
    "name": "Kim",
    "age": 20
}
```

### 특징

* Key를 이용하여 데이터를 조회한다.
* Key는 중복될 수 없다.
* Value는 중복될 수 있다.
* 수정 및 삭제가 가능하다.

### 예제

```python
student = {
    "name": "Kim",
    "age": 20
}

print(student["name"])
```

출력

```
Kim
```

---

# 🔍 Container 비교

| 특징  | List | Tuple | Set | Dictionary      |
| --- | ---- | ----- | --- | --------------- |
| 순서  | O    | O     | X   | O               |
| 인덱스 | O    | O     | X   | Key 사용          |
| 중복  | O    | O     | X   | Key X / Value O |
| 수정  | O    | X     | O   | O               |

---

# 🛠️ 자주 사용하는 함수

### List

```python
append()
insert()
remove()
pop()
sort()
reverse()
len()
sum()
min()
max()
```

### Set

```python
add()
remove()
discard()
union()
intersection()
difference()
```

### Dictionary

```python
keys()
values()
items()
get()
update()
pop()
clear()
```

---

# 💡 언제 사용할까?

* **List** : 순서가 있는 데이터를 저장할 때
* **Tuple** : 변경되지 않는 데이터를 저장할 때
* **Set** : 중복 제거 및 집합 연산이 필요할 때
* **Dictionary** : Key를 이용하여 빠르게 데이터를 찾을 때

---

# 🎯 예제

```python
students = {
    "Kim": 90,
    "Lee": 85,
    "Park": 95
}

for name, score in students.items():
    print(name, score)
```

출력

```
Kim 90
Lee 85
Park 95
```

---

# 📖 정리

✔ **List** → 순서 O, 수정 O, 중복 O

✔ **Tuple** → 순서 O, 수정 X

✔ **Set** → 중복 X, 순서 X

✔ **Dictionary** → Key : Value 구조, Key 중복 X

컨테이너 자료형은 파이썬에서 데이터를 효율적으로 저장하고 관리하기 위한 핵심 자료구조이며, 목적에 맞는 자료형을 선택하는 것이 중요합니다.


# 📦 Python Container

## 📌 Container란?

**Container(컨테이너)** 는 여러 개의 데이터를 하나의 객체에 저장하고 관리하는 자료형입니다.

파이썬에서는 다양한 컨테이너 자료형을 제공하며, 상황에 맞게 선택하여 사용할 수 있습니다.

대표적인 컨테이너는 다음과 같습니다.

| 자료형        | 생성 방법         | 순서              | 중복       | 수정 가능 |
| ---------- | ------------- | --------------- | -------- | ----- |
| List       | `[]`          | O               | O        | O     |
| Tuple      | `()`          | O               | O        | X     |
| Set        | `{}`          | X               | X        | O     |
| Dictionary | `{key:value}` | O (Python 3.7+) | Key 중복 X | O     |

---

# 📋 List (리스트)

여러 개의 데이터를 **순서대로 저장**하는 가장 많이 사용하는 컨테이너입니다.

```python
fruits = ["apple", "banana", "orange"]
```

### 특징

* 순서가 있다.
* 중복을 허용한다.
* 데이터 추가, 수정, 삭제가 가능하다.
* 다양한 자료형을 함께 저장할 수 있다.

### 예제

```python
numbers = [10, 20, 30]

print(numbers[0])

numbers.append(40)

print(numbers)
```

출력

```
10
[10, 20, 30, 40]
```

---

# 📋 Tuple (튜플)

리스트와 비슷하지만 **수정이 불가능(Immutable)** 한 자료형입니다.

```python
point = (10, 20)
```

### 특징

* 순서가 있다.
* 중복을 허용한다.
* 수정할 수 없다.

### 예제

```python
point = (100, 200)

print(point[0])
```

---

# 📋 Set (집합)

중복을 허용하지 않는 자료형입니다.

```python
numbers = {1, 2, 3}
```

### 특징

* 순서가 없다.
* 중복을 허용하지 않는다.
* 합집합, 교집합, 차집합 연산이 가능하다.

### 예제

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

출력

```
{1, 2, 3}
```

---

# 📋 Dictionary (딕셔너리)

**Key : Value** 형태로 데이터를 저장합니다.

```python
student = {
    "name": "Kim",
    "age": 20
}
```

### 특징

* Key를 이용하여 데이터를 조회한다.
* Key는 중복될 수 없다.
* Value는 중복될 수 있다.
* 수정 및 삭제가 가능하다.

### 예제

```python
student = {
    "name": "Kim",
    "age": 20
}

print(student["name"])
```

출력

```
Kim
```

---

# 🔍 Container 비교

| 특징  | List | Tuple | Set | Dictionary      |
| --- | ---- | ----- | --- | --------------- |
| 순서  | O    | O     | X   | O               |
| 인덱스 | O    | O     | X   | Key 사용          |
| 중복  | O    | O     | X   | Key X / Value O |
| 수정  | O    | X     | O   | O               |

---

# 🛠️ 자주 사용하는 함수

### List

```python
append()
insert()
remove()
pop()
sort()
reverse()
len()
sum()
min()
max()
```

### Set

```python
add()
remove()
discard()
union()
intersection()
difference()
```

### Dictionary

```python
keys()
values()
items()
get()
update()
pop()
clear()
```

---

# 💡 언제 사용할까?

* **List** : 순서가 있는 데이터를 저장할 때
* **Tuple** : 변경되지 않는 데이터를 저장할 때
* **Set** : 중복 제거 및 집합 연산이 필요할 때
* **Dictionary** : Key를 이용하여 빠르게 데이터를 찾을 때

---

# 🎯 예제

```python
students = {
    "Kim": 90,
    "Lee": 85,
    "Park": 95
}

for name, score in students.items():
    print(name, score)
```

출력

```
Kim 90
Lee 85
Park 95
```

---

# 📖 정리

✔ **List** → 순서 O, 수정 O, 중복 O

✔ **Tuple** → 순서 O, 수정 X

✔ **Set** → 중복 X, 순서 X

✔ **Dictionary** → Key : Value 구조, Key 중복 X

컨테이너 자료형은 파이썬에서 데이터를 효율적으로 저장하고 관리하기 위한 핵심 자료구조이며, 목적에 맞는 자료형을 선택하는 것이 중요합니다.


# 📦 Python Container

## 📌 Container란?

**Container(컨테이너)** 는 여러 개의 데이터를 하나의 객체에 저장하고 관리하는 자료형입니다.

파이썬에서는 다양한 컨테이너 자료형을 제공하며, 상황에 맞게 선택하여 사용할 수 있습니다.

대표적인 컨테이너는 다음과 같습니다.

| 자료형        | 생성 방법         | 순서              | 중복       | 수정 가능 |
| ---------- | ------------- | --------------- | -------- | ----- |
| List       | `[]`          | O               | O        | O     |
| Tuple      | `()`          | O               | O        | X     |
| Set        | `{}`          | X               | X        | O     |
| Dictionary | `{key:value}` | O (Python 3.7+) | Key 중복 X | O     |

---

# 📋 List (리스트)

여러 개의 데이터를 **순서대로 저장**하는 가장 많이 사용하는 컨테이너입니다.

```python
fruits = ["apple", "banana", "orange"]
```

### 특징

* 순서가 있다.
* 중복을 허용한다.
* 데이터 추가, 수정, 삭제가 가능하다.
* 다양한 자료형을 함께 저장할 수 있다.

### 예제

```python
numbers = [10, 20, 30]

print(numbers[0])

numbers.append(40)

print(numbers)
```

출력

```
10
[10, 20, 30, 40]
```

---

# 📋 Tuple (튜플)

리스트와 비슷하지만 **수정이 불가능(Immutable)** 한 자료형입니다.

```python
point = (10, 20)
```

### 특징

* 순서가 있다.
* 중복을 허용한다.
* 수정할 수 없다.

### 예제

```python
point = (100, 200)

print(point[0])
```

---

# 📋 Set (집합)

중복을 허용하지 않는 자료형입니다.

```python
numbers = {1, 2, 3}
```

### 특징

* 순서가 없다.
* 중복을 허용하지 않는다.
* 합집합, 교집합, 차집합 연산이 가능하다.

### 예제

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

출력

```
{1, 2, 3}
```

---

# 📋 Dictionary (딕셔너리)

**Key : Value** 형태로 데이터를 저장합니다.

```python
student = {
    "name": "Kim",
    "age": 20
}
```

### 특징

* Key를 이용하여 데이터를 조회한다.
* Key는 중복될 수 없다.
* Value는 중복될 수 있다.
* 수정 및 삭제가 가능하다.

### 예제

```python
student = {
    "name": "Kim",
    "age": 20
}

print(student["name"])
```

출력

```
Kim
```

---

# 🔍 Container 비교

| 특징  | List | Tuple | Set | Dictionary      |
| --- | ---- | ----- | --- | --------------- |
| 순서  | O    | O     | X   | O               |
| 인덱스 | O    | O     | X   | Key 사용          |
| 중복  | O    | O     | X   | Key X / Value O |
| 수정  | O    | X     | O   | O               |

---

# 🛠️ 자주 사용하는 함수

### List

```python
append()
insert()
remove()
pop()
sort()
reverse()
len()
sum()
min()
max()
```

### Set

```python
add()
remove()
discard()
union()
intersection()
difference()
```

### Dictionary

```python
keys()
values()
items()
get()
update()
pop()
clear()
```

---

# 💡 언제 사용할까?

* **List** : 순서가 있는 데이터를 저장할 때
* **Tuple** : 변경되지 않는 데이터를 저장할 때
* **Set** : 중복 제거 및 집합 연산이 필요할 때
* **Dictionary** : Key를 이용하여 빠르게 데이터를 찾을 때

---

# 🎯 예제

```python
students = {
    "Kim": 90,
    "Lee": 85,
    "Park": 95
}

for name, score in students.items():
    print(name, score)
```

출력

```
Kim 90
Lee 85
Park 95
```

---

# 📖 정리

✔ **List** → 순서 O, 수정 O, 중복 O

✔ **Tuple** → 순서 O, 수정 X

✔ **Set** → 중복 X, 순서 X

✔ **Dictionary** → Key : Value 구조, Key 중복 X

컨테이너 자료형은 파이썬에서 데이터를 효율적으로 저장하고 관리하기 위한 핵심 자료구조이며, 목적에 맞는 자료형을 선택하는 것이 중요합니다.

