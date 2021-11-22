s = []
for i in range(3):
    s.append(input())

ans = ""
t = input()
for i in t:
    ans += s[int(i)-1]
print(ans)
