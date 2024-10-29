x, y, z, r = map(int, input("Enter four numbers: ").split())

x = x % 100
y = y % 100
z = z % 100
r = r % 100

mult = (x * y * z * r) % 100

if mult <= 9:
    print(f"0{mult}")
else:
    print(mult)
