c = int(input())
k = 0

for x in range(1, c + 1):
    num = int(input())
    if num > k:
        k = num

print(k)
