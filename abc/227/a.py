n, k, a = map(int, input().split())
if a + k <= n:
    print(a+k)
else:
    rem = k - (n-a+1)
    print(rem%n+1)
