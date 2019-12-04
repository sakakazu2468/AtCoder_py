a,b = map(int, input().split())
n = b-a
count = 0
for i in range(n+1):
    s = str(a+i)
    if s[0] == s[4] and s[1] == s[3]:
        count += 1
print(count)
    
