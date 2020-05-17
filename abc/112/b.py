n, time = map(int, input().split())
cost = 10000
for i in range(n):
    s, t = map(int, input().split())
    if t <= time:
        cost = min(cost, s)
if cost == 10000:
    print("TLE")
else:
    print(cost)
