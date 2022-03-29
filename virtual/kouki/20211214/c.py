n = int(input())
s = input()
ans = -1
for i in range(n-1):
    l = set(list(s[:i+1]))
    r = set(list(s[i+1:]))
    ans = max(len(l.intersection(r)), ans)
print(ans)
