x, y = map(int, input().split())
for i in range(x+1):
    a, b = i, x-i
    if 2*a + 4*b == y:
        print("Yes")
        break
else:
    print("No")
