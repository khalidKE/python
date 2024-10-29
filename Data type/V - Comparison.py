x, ch, y = input("Enter an expression (e.g., 3 = 4): ").split()
x = int(x)
y = int(y)

if ch == '=':
    if x == y:
        print("Right")
    else:
        print("Wrong")
elif ch == '>':
    if x > y:
        print("Right")
    else:
        print("Wrong")
else:  # ch must be '<'
    if x < y:
        print("Right")
    else:
        print("Wrong")
