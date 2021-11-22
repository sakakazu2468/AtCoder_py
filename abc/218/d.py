n = int(input())
dic = dict()
for i in range(n):
    x, y = map(int, input().split())
    g = dic.get(x)
    if g:
        g.append(y)
    else:
        dic[x] = [y]

ans = 0
for key, value in dic.items():
    for k, v in dic.items():
        if key <= k:
            continue
        l = len(set(value)&(set(v)))
        ans += (l*(l-1))//2
print(ans)


        
