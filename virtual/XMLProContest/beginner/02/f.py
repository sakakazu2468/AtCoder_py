n = int(input())
s = input()
t = input()
t_idx = 0
for i in range(len(s)):
    if t[t_idx] == s[i]:
        t_idx += 1
    else:
        t_idx = 0
        if t[t_idx] == s[i]:
            t_idx = 1
print(len(s+t[t_idx:]))

    
