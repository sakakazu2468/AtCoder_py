s = input()
t = input()
ans = 10000000
for i in range(len(s)-len(t)+1):
    diff = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            diff += 1
    ans = min(ans, diff) 
print(ans)
