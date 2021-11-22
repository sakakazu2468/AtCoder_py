x = input()
new = {}
for i in range(len(x)):
    new[x[i]] = i

n = int(input())
names = []
for i in range(n):
    name = []
    s = input()
    for c in s:
        name.append(new[c])
    names.append([name, s])
names.sort()
for out in names:
    print(out[-1])
