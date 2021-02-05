x, y = map(int, input().split())
s = min(x, y)
l = max(x, y)
if l-s < 3:
    print("Yes")
else:
    print("No")
