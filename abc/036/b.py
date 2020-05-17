n = int(input())
s = []
for i in range(n):
    s.append(list(input()))

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(s[n-j-1][i])
        else:
            print(s[n-j-1][i], end="")
