import itertools


l = [i for i in range(1, 9)]
li = list(itertools.permutations(l))
print(li.index((2,3,4,5,6,7,1,8)))

