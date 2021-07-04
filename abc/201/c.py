s = input()
oxq = [0, 0, 0]
for i in s:
    if i == 'o':
        oxq[0] += 1
    elif i == 'x':
        oxq[1] += 1
    else:
        oxq[2] += 1

sort_oxq = 'o'*oxq[0] + 'x'*oxq[1] + '?'*oxq[2]
ans = 0
for i in range(10000):
    sort_oxq_table = [0 for i in range(10)]
    num = str(i).zfill(4)
    for n in num:
        sort_oxq_table[int(n)] += 1
    for j in range(10):
        if sort_oxq[j] == 'x' and sort_oxq_table[j] >= 1:
            break
        elif sort_oxq[j] == 'o' and sort_oxq_table[j] < 1:
            break
    else:
        ans += 1
print(ans)



