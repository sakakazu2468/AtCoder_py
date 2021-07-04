n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n+1-i):
        money = 10000*i + 5000*j + 1000*(n-i-j)
        if money==y:
            print(i, j, (n-i-j))
            break
    else:
        continue
    break
else:
    print(-1, -1, -1)
