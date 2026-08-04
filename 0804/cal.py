def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "오류: 0으로 나눌 수 없습니다."
        return a / b
    else:
        return "잘못된 연산자입니다."


while True:
    print("\n===== 계산기 =====")

    num1 = float(input("첫 번째 숫자: "))
    op = input("연산자(+,-,*,/): ")
    num2 = float(input("두 번째 숫자: "))

    result = calculate(num1, num2, op)
    print("결과:", result)

    again = input("계속 계산하시겠습니까? (y/n): ")

    if again.lower() != "y":
        print("프로그램을 종료합니다.")
        break