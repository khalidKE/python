x = int(input())
odd = 0
even = 0
pos = 0
neg = 0

for _ in range(x):
    num = int(input())
    if num % 2 == 0:
        even += 1
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    else:
        odd += 1
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", pos)
print("Negative:", neg)
