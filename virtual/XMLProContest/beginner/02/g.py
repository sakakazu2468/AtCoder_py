n, x = map(int, input().split())
a = list(map(int, input().split()))
b = bin(x)[2:]
ans = 0
for i in range(len(b)):
    ans += a[i]*int(b[-1*(i+1)])
print(ans)


