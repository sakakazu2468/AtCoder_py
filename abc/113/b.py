n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans = 100000
d = 100000
for i in range(n):
    tem = t-h[i]*0.006
    if d >= abs(tem-a):
        d = min(d, abs(tem-a))
        ans = i+1
print(ans)

