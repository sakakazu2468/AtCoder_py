n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
if (0 in t) and not (0 in s):
    print(-1)
elif (1 in t) and not (1 in s):
    print(-1)
else:
    if s[0] == 0:
        p_dis = 0
        for i in range(n):
            if s[i] == 1:
                p_dis = i
                break
        m_dis = 0
        for i in range(n):
            if s[(i+1)*-1] == 1:
                m_dis = i+1
                break
        dis = min(p_dis, m_dis)
    else:
        p_dis = 0
        for i in range(n):
            if s[i] == 0:
                p_dis = i
                break
        m_dis = 0
        for i in range(n):
            if s[(i+1)*-1] == 0:
                m_dis = i+1
                break
        dis = min(p_dis, m_dis)
        
    cost = True
    ans = 0
    prev = s[0]
    for i in range(m):
        if cost:
            if prev != t[i]:
                cost = False
                ans += dis+1
            else:
                ans += 1
        else:
            if prev != t[i]:
                ans += 2
            else:
                ans += 1
        prev = t[i]
    print(ans)
