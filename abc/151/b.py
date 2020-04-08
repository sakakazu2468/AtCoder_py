n, k, m = map(int, input().split())
a = list(map(int, input().split()))
total = m*n
if total-sum(a) > k:
    print(-1)
elif total-sum(a) < 0:
    print(0)
else:
    print(total-sum(a))
