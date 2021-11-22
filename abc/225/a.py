from itertools import permutations


s = input()
ans = []
for v in permutations(s):
    ans.append("".join(v))
print(len(set(ans)))
