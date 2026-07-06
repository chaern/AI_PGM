def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b


def main():
    print("=== CLI 계산기 ===")

    while True:
        print("\n연산 선택")
        print("1. 덧셈 (+)")
        print("2. 뺄셈 (-)")
        print("3. 곱셈 (*)")
        print("4. 나눗셈 (/)")
        print("q. 종료")

        choice = input("선택: ")

        if choice.lower() == "q":
            print("프로그램을 종료합니다.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("잘못된 선택입니다.")
            continue

        try:
            num1 = float(input("첫 번째 숫자: "))
            num2 = float(input("두 번째 숫자: "))
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operator = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"
        else:
            result = divide(num1, num2)
            operator = "/"

        print(f"\n결과: {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()