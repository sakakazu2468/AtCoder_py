from collections import deque


s = input()
t = ""
t_r = ""
r_flag = False
for c in s:
    if c == "R":
        r_flag = not r_flag
        continue

    if r_flag:
        t_r += c
    else:
        t += c

if r_flag:
    t = t[::-1] + t_r
else:
    t = t_r[::-1] + t

# q = []
# queue = deque(q)
queue = []
prev = ""
for i in range(len(t)):
    if len(queue) == 0:
        queue.append(t[i])
        prev = t[i]
    else:
        if prev != t[i]:
            queue.append(t[i])
            prev = t[i]
        else:
            queue.pop()
            if len(queue) == 0:
                prev = ""
            else:
                prev = queue[-1]

for i in range(len(queue)):
    print(queue[i], end="")
    # print(queue.popleft(), end="")
print()

    
     
