from itertools import permutations

n = int(input())
p = tuple((map(int, input().split())))
q = tuple((map(int, input().split())))
perm = list(permutations([i+1 for i in range(n)]))
print(abs(perm.index(p)-perm.index(q)))

