s = input()
ans = 1000000
for i in range(len(s)-2):
    n = int(s[i:i+3])
    ans = min(ans, abs(n-753))
print(ans)
