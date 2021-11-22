n = int(input())

ans = set()
for i in range(n):
    ipt = tuple(list(map(int, input().split())))
    ans.add(ipt)

print(len(ans))
