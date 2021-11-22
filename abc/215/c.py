from itertools import permutations


s, k = input().split()
k = int(k)
pattern = list(set(permutations(s)))
pattern.sort()
print("".join(pattern[k-1]))
