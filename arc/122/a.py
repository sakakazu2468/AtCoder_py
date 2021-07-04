import copy

n = int(input())
fib = [0 for i in range(10**5+10)]
fib[0] = 1
fib[1] = 1

for i in range(10**5+10):
    if i!=0 and i!=1:
        fib[i] = (fib[i-2] + fib[i-1])%(10**9+7)

if n == 1:
    print(int(input()))
else:
    a = list(map(int, input().split()))
    pattern = fib[n]
    plus = 0
    minus = 0
    mx = -1
    for i in range(n-1):
        plus += a[i+1] * fib[i+1]*fib[n-1-i]
        plus %= (10**9+7)
        minus += a[i+1] * (pattern-fib[i+1]*fib[n-1-i])
        minus %= (10**9+7)
    ans = fib[n]*a[0]
    ans %= (10**9+7)
    ans += plus
    ans -= minus

    print(ans%(10**9+7))
