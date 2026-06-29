
for i in range(1, 5):
    for j in range(1, i+1):
            print("*", end = "")
    print()

for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 6):
    # 공백 출력
    for j in range(5 - i):
        print(" ", end="")

    # 별 출력
    for j in range(2 * i - 1):
        print("*", end="")

    # 줄바꿈
    print()   

n = 5

# 위쪽
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 아래쪽
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()