import sys

x, y, z = map(int, input().split())

mini = min(x, y)
ma = max(x, y)

print(min(mini, z), max(ma, z))

