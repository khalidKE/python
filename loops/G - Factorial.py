num = int(input())
f = 1

for _ in range(num):
    n = int(input())
    for _ in range(n):
        num = int(input())
        for i in range(num, 1, -1):
            f *= i
        print(f)
        f = 1
