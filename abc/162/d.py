n = int(input())
s = input()
r, g, b = 0, 0, 0
for i in s:
    if i == 'R':
        r += 1
    elif i == 'G':
        g += 1
    else:
        b += 1
bad = 0
for i in range(n):
    gap = 0
    while i+(gap+1)*2 <= n-1:
        if s[i] != s[i+gap+1] and s[i+gap+1] != s[i+(gap+1)*2]\
                and s[i] != s[i+(gap+1)*2]:
            bad += 1
        gap += 1
print(r*g*b-bad) 
