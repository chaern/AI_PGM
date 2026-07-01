# 반복문으로 피보나치 수열을 생성하는 프로그램

def fibonacci(n):
    """n개의 피보나치 수를 리스트로 반환합니다."""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    try:
        n = int(input("몇 개의 피보나치 수를 출력할까요? "))
    except ValueError:
        n = 10
    if n < 1:
        n = 1
    sequence = fibonacci(n)
    print(" ".join(str(x) for x in sequence))



