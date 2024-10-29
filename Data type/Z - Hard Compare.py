import math

a, b, c, d = map(int, input("Enter four numbers: ").split())

if b * math.log(a) > d * math.log(c):
    print("YES")
else:
    print("NO")
