n = int(input())
s = input()
t = input()
if s.count('0') != t.count('0'):
    print(-1)
else:
    s_zero = [0 for i in range(n)]
    t_zero = [0 for i in range(n)]
    s_i = 0
    t_i = 0
    for i in range(n):
        if s[i]=='0':
            s_zero[s_i] = i
            s_i += 1
    for i in range(n):
        if t[i]=='0':
            t_zero[t_i] = i
            t_i += 1
    ans = 0
    for i in range(n):
        if s_zero[i] != t_zero[i]:
            ans += 1
    print(ans)



        
