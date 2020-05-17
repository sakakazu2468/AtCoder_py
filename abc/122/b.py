s = input()
table = [0 for i in range(len(s))]
acgt = ['A', 'C', 'G', 'T']
for i in range(len(s)):
    if s[i] in acgt:
        table[i] += 1

count = 0
ans = 0
for i in table:
    if i:
        count += 1
        ans = max(ans, count)
    else:
        count = 0
print(ans)
