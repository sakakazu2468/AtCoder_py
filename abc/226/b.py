n = int(input())
ans = set()
for i in range(n):
    ipt = tuple(map(int, input().split()))[1:]
    ans.add(ipt)
print(len(ans))
