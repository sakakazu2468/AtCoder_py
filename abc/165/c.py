n, m, q = map(int, input().split())
abcd = []
a = [1 for i in range(n)]
ans = []
for i in range(q):
    abcd.append(list(map(int, input().split())))
for i in range(1, m+1):
    a[-1] = i
    for j in range(n-1):
        p = i
        for k in range(a[-j-1]):
            a[-j-2] = p
            print(a)
            for l in range(q):
                ans.append(0)
                if a[abcd[l][1]-1]-a[abcd[l][0]-1] == abcd[l][2]:
                    ans[-1] += abcd[l][3]
            p += 1
print(ans)
        
