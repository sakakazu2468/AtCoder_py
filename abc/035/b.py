s = input()
t = int(input())
v = 0
h = 0
q = 0
for i in s:
    if i == 'L':
        v -= 1
    elif i == 'R':
        v += 1
    elif i == 'U':
        h += 1
    elif i == 'D':
        h -= 1
    elif i == '?':
        q += 1
v = abs(v)
h = abs(h)

if t == 1:
    print(v+h+q)
else:
    if v+h >= q:
        print(v+h-q)
    elif (q-(v+h))%2 == 0:
        print(0)
    else:
        print(1)
