n, m = map(int, input().split())
s_list = [0 for i in range(20)]
for i in range(n):
    s = input()
    one = 0
    for q in s:
        if q == "1":
            one += 1
    s_list[one] += 1
ans = n*(n-1)//2
for i in range(len(s_list)):
    minus = s_list[i]
    if minus != 0:
        ans -= minus*(minus-1)//2
print(ans)
