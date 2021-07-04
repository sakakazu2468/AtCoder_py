n = int(input())
t = list(map(int, input().split()))
t = sorted(t, reverse=True)
oven1 = 0
o1 = []
oven2 = 0
o2 = []
for i in range(n):
    if oven1 <= oven2:
        oven1 += t[i]
        o1.append(t[i])
    else:
        oven2 += t[i]
        o2.append(t[i])
if oven1==oven2:
    print(oven1)
elif len(o1) == 1 or len(o2) == 1:
    print(max(oven1, oven2))
else:
    diff = (oven1-oven2)//2
    near_diff = 10**6
    for i in range(len(o1)):
        for j in range(len(o2)):
            near_diff = min(abs(diff-(o1[i]-o2[j])), near_diff)
    print(max((oven1-near_diff, oven2+near_diff)))
