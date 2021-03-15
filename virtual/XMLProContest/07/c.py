n = int(input())
s = input()
if len(s)%2 != 0:
    print(-1)
else:
    dif_count = 0
    s_head = s[:n//2]
    s_tail = s[n//2:]
    for i in range(len(s_head)):
        if s_head[i] != s_tail[i]:
            dif_count += 1
    print(dif_count)
