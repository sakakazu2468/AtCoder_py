n = int(input())
a = list(map(int, input().split()))
rem_a = {}
for i in range(n):
    rem = a[i]%200
    rem_a[rem] = rem_a.get(rem, 0) + 1

ans = 0
for val in rem_a.values():
    ans += val*(val-1)//2
print(ans)

