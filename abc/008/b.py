n = int(input())
names = []
vote = []
for i in range(n):
    name = input()
    if name in names:
        vote[names.index(name)] += 1
    else:
        names.append(name)
        vote.append(1)
print(names[vote.index(max(vote))])
