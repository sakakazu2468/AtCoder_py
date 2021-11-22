n = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(n)]
up = True
idx = 1

while idx < n:
    if up:
        if a[idx-1] > a[idx]:
            ans[idx-1] = 1
            up = False
    else:
        if a[idx-1] < a[idx]:
            ans[idx-1] = 1
            up = True
    idx += 1

if up == False:
    ans[-1] = 1

print(" ".join(map(str, ans)))