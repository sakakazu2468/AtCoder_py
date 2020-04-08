n, x = map(int, input().split())
a = list(map(int, input().split()))
b = str(bin(x))
ans = 0
for i in range(len(b)-2):
    if b[-i-1] == '1':
        ans += a[i]
print(ans)
