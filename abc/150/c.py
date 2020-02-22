import itertools 


n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
kind = [i for i in range(1, n+1)]
li = list(itertools.permutations(kind))
a = li.index(p)
b = li.index(q)

print(abs(a-b))
