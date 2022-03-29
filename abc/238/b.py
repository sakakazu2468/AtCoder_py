n = int(input())
a = list(map(int, input().split()))
cuts = [0]
now = 0
for i in range(n):
    now = (now+a[i]) % 360
    cuts.append(now)
cuts.sort()
ans = -1
cuts.append(360)
for i in range(len(cuts)-1):
    ans = max(cuts[i+1]-cuts[i], ans)
print(ans)
