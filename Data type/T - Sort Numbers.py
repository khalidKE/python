x, y, z = map(int, input("Enter three numbers: ").split())

if x >= y and y >= z:
    print(z)
    print(y)
    print(x)
elif x >= z and z >= y:
    print(y)
    print(z)
    print(x)
elif y >= z and z >= x:
    print(x)
    print(z)
    print(y)
elif y >= x and x >= z:
    print(z)
    print(x)
    print(y)
elif z >= x and x >= y:
    print(y)
    print(x)
    print(z)
else:
    print(x)
    print(y)
    print(z)

print()
print(x)
print(y)
print(z)
