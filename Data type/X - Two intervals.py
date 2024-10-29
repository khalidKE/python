l1, r1, l2, r2 = map(int, input("Enter the intervals (l1 r1 l2 r2): ").split())

if ((l2 > l1 and l2 > r1) or (l1 > l2 and l1 > r2)):
    print(-1)
elif (l1 < l2 and r2 > r1):
    print(l2, r1)
elif (l2 < l1 and r1 > r2):
    print(l1, r2)
elif (l2 > l1 and r2 == r1):
    print(l2, r2)
elif (l1 > l2 and r2 == r1):
    print(l1, r2)
elif (l1 == l2 and r2 > r1):
    print(l1, r1)
elif (l1 == l2 and r1 > r2):
    print(l1, r2)
elif (l2 > l1 and r1 > r2):
    print(l2, r2)
elif (l1 > l2 and r2 > r1):
    print(l1, r1)
else:
    print(l1, r1)
