n = int(input())
a = list(map(int, input().split()))
a.sort()

def mod(x):
    m = x%998244353
    return m

mult_list = [0 for i in range(n-1)]
for i in range(n-2, -1, -1):
    if i==n-2:
        mult_list[i] = mod(a[-1])
    else:
        mult_list[i] = mod(mult_list[i+1]*2 + a[i+1])

ans = 0
for i in range(len(mult_list)):
    ans += mod(a[i]*mult_list[i])
    ans = mod(ans)

for i in range(n):
    ans += mod(a[i]**2)
    ans = mod(ans)

print(ans)
