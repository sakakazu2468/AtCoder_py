n = int(input())
memo = {}
for i in range(n):
    a = int(input())
    if memo.get(a, 0) == 0:
        memo[a] = memo.get(a, 0) + 1
    else:
        memo[a] = memo.get(a, 0) - 1

ans = 0
for val in memo.values():
    ans += val
print(ans)
