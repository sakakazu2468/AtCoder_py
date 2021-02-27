n = int(input())
min_cost = 10**10
for i in range(n):
    a, p, x = map(int, input().split())
    rem_sunuke = x-a
    if rem_sunuke > 0:
        min_cost = min(min_cost, p)
if min_cost != 10**10:
    print(min_cost)
else:
    print(-1)

