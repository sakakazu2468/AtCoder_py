count = []
for i in range(18):
    num = 9*(10**i)
    count.append(num*(num+1)//2)
ans = 0
n = int(input())
for i in range(len(str(n))-1):
    ans += count[i]

if len(str(n)) == 1:
    print(n*(n+1)//2)
else:
    tmp = n-(10**(len(str(n))-1))+1
    ans += tmp*(tmp+1)//2
    print(ans%998244353)
