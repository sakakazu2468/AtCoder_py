n = int(input())
b = list(map(int, input().split()))
if n == 2:
    print(b[0]*2)
else:
    ans = b[0]
    for i in range(n-2):
        ans += min(b[i], b[i+1])
    print(ans+b[-1])