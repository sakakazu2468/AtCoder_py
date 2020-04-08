n = int(input())
p = list(map(int, input().split()))
ans = 0
num = 1000000
for i in p:
    if num > i:
        ans += 1
        num = i
print(ans)
