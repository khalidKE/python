x = input()
if (ord(x) >= 65 and ord(x) <= 90):
    m = 32 + ord(x)
    b = chr(m)
    print(b)
else:
    m = ord(x) - 32
    b = chr(m)
    print(b)