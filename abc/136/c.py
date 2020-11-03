n = int(input())
h = list(map(int, input().split()))
m = 0
for i in range(n):
    if m < h[i]:
        m = h[i]
    if m - h[i] >= 2:
        print("No")
        break
else:
    print("Yes")