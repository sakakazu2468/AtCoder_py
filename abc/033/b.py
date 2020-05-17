n = int(input())
m = 0
total = 0
name = ""
for i in range(n):
    s, p = input().split()
    p = int(p)
    total += p
    if p > m:
        name = s
        m = p

if total/2 < m:
    print(name)
else:
    print("atcoder")
