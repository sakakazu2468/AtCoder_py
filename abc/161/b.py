n, m = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
for i in range(m):
    if sum_a/4/m > max(a):
        print("No")
        break
    else:
        a.remove(max(a))
else:
    print("Yes")
