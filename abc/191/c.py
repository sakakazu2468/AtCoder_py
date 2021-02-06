h, w = map(int, input().split())
s = []
lattice = [[-1 for i in range(w-1)] for j in range(h-1)]
for i in range(h):
    s.append(list(input())[:])

for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] == "#":
            lattice[i-1][j-1] *= -1
            lattice[i][j-1] *= -1
            lattice[i-1][j] *= -1
            lattice[i][j] *= -1

count = 0
for i in lattice:
    for j in i:
        if j == 1:
            count += 1
print(count)

