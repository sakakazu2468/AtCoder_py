n = int(input())
s = input()
m = -1
for i in range(n):
    l = set(s[:i])
    r = set(s[i:])
    m = max(len(l.intersection(r)), m)
print(m)
