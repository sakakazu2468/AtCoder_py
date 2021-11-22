n = int(input())
s = []
t = []
s_x = 0
s_y = 0
t_x = 0
t_y = 0
for i in range(n):
    x, y = map(int, input().split())
    s_x += x
    s_y += y
    s.append([x, y])
for i in range(n):
    t_x += x
    t_y += y
    t.append([x, y])

s_dis.sort()
t_dis.sort()

s_around = [(s[0][0]-s[-1][0])**2+(s[0][1]-s[-1][1])**2]
for i in range(n-1):
    s_around.append((s[i][0]-s[i+1][0])**2+(s[i][1]-s[i+1][1])**2)
t_around = [(t[0][0]-t[-1][0])**2+(t[0][1]-t[-1][1])**2]
for i in range(n-1):
    t_around.append((t[i][0]-t[i+1][0])**2+(t[i][1]-t[i+1][1])**2)

for i in range(n):
    s_rotate = s_around[i:] + s_around[:i]
    print(s_rotate, t_around)
    if s_rotate==t_around:
        if s_dis==t_dis:
            print("Yes")
            break
else:
    print("No")
