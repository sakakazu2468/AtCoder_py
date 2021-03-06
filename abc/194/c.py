n = int(input())
a = list(map(int, input().split()))
a.sort()
cum_a = []
cum = 0
ans = 0
for i in range(n):
    ans += (n-1)*(a[i]**2) 
    cum += a[i]
    cum_a.append(cum)
cum_a = cum_a[:-1]
for i in range(n-1):
    ans -= 2*cum_a[n-2-i]*a[n-1-i]
print(ans)

