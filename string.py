# 변수,상수,정수,실수,문자열

print("Hello Python!")
print("Hello \n Py\n thon!")
print("""He\nllo
      Python!""")

print("I have %s apples" % 3)

a=3
b=5
print("I eat %d apples." % a)
print("I eat %d apples and %f oranges." % ((1+2),3.141592))
print("I eat %d apples and %.2f oranges." % ((1+2),3.141592)) 

# 문자열
str1="simple python string"
print(str1)
print("exampled string : %s" % str1)


# 변수, 포맷, f
print("I eat {}" . format(3))
print("I eat %d apples and %d oranges " %(3,5))
print("I eat {0} apples and {1} oranges ". format(3,5))
print(f"I eat {3} apples and {5} oranges.")
print(f"I eat 3 apples and 5 oranges.")

#키보드로 부터 입력 받는 함수 input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"You entered: {a} and {b}")
print(f"a + b: {(a) + (b)}")
print(f"a - b: {(a) - (b)}")
print(f"a * b: {(a) * (b)}")
print(f"a / b: {(a) / (b)}")

# 1. 두 개의 정수를 입력 받아 사칙연산의 결과를 출력하세요.
a = int(input("enter fist number:"))
b = int(input("enter fist number:"))
print(f"a + b: {(a) + (b)}")
print(f"a - b: {(a) - (b)}")
print(f"a * b: {(a) * (b)}")
print(f"a / b: {(a) / (b)}")

# 2. 5개의 정수 값을 입력 받아 리스트에 저장하고 그 리스트의 합, 평균, 최소값, 최대값을 출력하세요.

num1 = int(input("enter fist number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
num4 = int(input("enter fourth number:"))
num5 = int(input("enter fifth number:"))

number = [num1, num2, num3, num4, num5]

print("합:", sum(number))
print("평균:", sum(number) / len(number))
print("최소값:", min(number))
print("최대값:", max(number))

# 3. 과일명이 있는 리스트를 정의하고 그 리스트의 첫번째와 마지막 문자열을 출력하세요.
fruits = ["사과", "과일", "배"]
print("첫번째 과일 : ", fruits[0])
print("마지막 과일 : ", fruits[-1])

fruit = ["사과", "과일", "배"]
fruits = input("Enter a fruit")
fruits. append(fruit)
fruits = input("Enter a fruit")
fruits. append(fruit)
fruits = input("Enter a fruit")
fruits. append(fruit)
fruits = input("Enter a fruit")
fruits. append(fruit)
fruits = input("Enter a fruit")
fruits. append(fruit)
print(fruits)
print(fruits[0])
print(fruits[-1])
