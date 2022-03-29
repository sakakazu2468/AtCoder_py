s = input()
s1 = s[:len(s)//2]
s2 = s[len(s)//2+len(s)%2:]
s2 = s2[::-1]
ans = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        ans += 1
print(ans)
