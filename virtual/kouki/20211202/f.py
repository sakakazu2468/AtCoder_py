h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
ans = 0
for i in range(1, h-1):
    for j in range(1, w-1):
        if s[i][j] == "#":
            if s[i-1][j-1] == "#":
                if s[i-1][j] == "#":
                    if s[i][j-1] == "#":
                        ans -= 2
                    else:
                        ans += 2
                else:
                    if s[i][j-1] == "#":
                        ans += 2
            else:
                if s[i-1][j] == "#":
                    if s[i][j-1] == "#":
                        ans -= 2
                else:
                    if s[i][j-1] == "#":
                        pass
                    else:
                        ans += 4
        print(ans)
print(ans)
