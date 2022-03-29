s = input()
k = int(input())
ruiseki = [0]
for c in s:
    if c == "X":
        ruiseki.append(ruiseki[-1])
    else:
        ruiseki.append(ruiseki[-1]+1)

pair = [[0, 0] for _ in range(ruiseki[-1]+1)]
use = [False for _ in range(ruiseki[-1]+1)]
for i in range(len(ruiseki)):
    if use[ruiseki[i]] == False:
        pair[ruiseki[i]][0] = i
        use[ruiseki[i]] = True
        if i!=0:
            pair[ruiseki[i-1]][1] = i-1
pair[-1][1] = len(ruiseki)-1

roop = ruiseki[-1] - min(ruiseki[-1], k)+1
m = min(ruiseki[-1], k)
ans = -1
for i in range(roop):
    ans = max(pair[i+m][1]-pair[i][0], ans) 

print(ans)
