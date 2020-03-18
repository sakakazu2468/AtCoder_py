import math


a, b, c = map(int, input().split())
upper = (c-a-b)**2
lower = a*b*4
if upper > lower:
    print("Yes")
else:
    print("No")
