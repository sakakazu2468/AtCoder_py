a, b, c = map(int, input().split())
l = [0 for i in range(10)]
l[a] += 1
l[b] += 1
l[c] += 1
if l[5] == 2 and l[7] == 1:
    print("YES")
else:
    print("NO")
