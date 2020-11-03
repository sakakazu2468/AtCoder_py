h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()[:]))
line = []
for i in range(h*2-1):
    if i%2 == 0:
        line.append([1 for j in range(w-1)])
    else:
        line.append([1 for j in range(w)])
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i+1 <= h-1:
                line[i*2+1][j] = 0
            if i-1 >= 0:
                line[i*2-1][j] = 0
            if j <= w-2:
                line[i*2][j] = 0
            if j-1 >= 0:
                line[i*2][j-1] = 0

ans = 0
for i in range(h*2-1):
    ans += sum(line[i])
print(ans)