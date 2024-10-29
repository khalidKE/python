x, ch, y, q, s = input("Enter the expression (e.g., 3 + 4 = 7): ").split()
x = int(x)
y = int(y)
s = int(s)

sum_result = x + y
dis_result = x - y
m_result = x * y

if ch == '+':
    if sum_result == s:
        print("Yes")
    else:
        print(sum_result)
elif ch == '-':
    if dis_result == s:
        print("Yes")
    else:
        print(dis_result)
else:  # ch must be '*'
    if m_result == s:
        print("Yes")
    else:
        print(m_result)
