x = float(input("Enter a number: "))
y = int(x)
m = x - y

if m == 0:
    print(f"int {y}")
else:
    print(f"float {y} {m:.3f}")
