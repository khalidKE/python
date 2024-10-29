x = int(input("Enter the number of days: "))
y = 0
c = 0

while x >= 365:
    y += 1
    x -= 365

while x >= 30:
    c += 1
    x -= 30

print(f"{y} years")
print(f"{c} months")
print(f"{x} days")
