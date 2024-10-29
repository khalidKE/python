x = int(input())

if x == 1:
    print(-1)
else:
    for c in range(1, x + 1):
        if c % 2 == 0:
            print(c)
