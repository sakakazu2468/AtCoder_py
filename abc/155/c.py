import collections


n = int(input())
s = []
for i in range(n):
    s.append(input())

dic = collections.Counter(s)
k = dic.most_common()
m = k[0][1]
mx = m
i = 0
ans = []
while m == mx: 
    ans.append(k[i][0])
    i += 1
    if i > len(k)-1:
        break
    m = k[i][1]

ans = sorted(ans)
for i in ans:
    print(i)
