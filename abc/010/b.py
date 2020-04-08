n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i == 9:
        pass
    elif i >= 7:
        ans += i - 7
    elif i >= 3:
        ans += i - 3
    else:
        ans += i - 1
print(ans)
