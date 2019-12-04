n, m, b = map(int, input().split())
gy, gx = map(int, input().split())
for i in range(m):
    ry, rx, c = input().split()

b_list = []
for i in range(b):
    by, bx = map(int, input().split())
    b_list.append([by, bx])

neigh_list = []
for i in b_list:
    if i[0] < gy and i[1] < gx:
        if not i[0] == 0 and not [i[0]-1, i[1]] in b_list:
            neigh_list.append([i[0]-1, i[1], 'R'])
    if i[0] > gy and i[1] < gx:
        if not i[1] == 0 and not [i[0], i[1]-1] in b_list:
            neigh_list.append([i[0], i[1]-1, 'U'])
    if i[0] < gy and i[1] > gx:
        if not i[1] == 39 and not [i[0], i[1]+1] in b_list:
            neigh_list.append([i[0], i[1]+1, 'D'])
    if i[0] > gy and i[1] > gx:
        if not i[0] == 39 and not [i[0]+1, i[1]] in b_list:
            neigh_list.append([i[0]+1, i[1], 'L'])
count = 0
for i in range(40):
    if [gy, i] in b_list:
        count += 1
    if [i, gx] in b_list:
        count += 1

print((n-1)+(n-1)-count+len(neigh_list))
for i in range(40):
    if [gy, i] in b_list:
        pass
    elif i == gx:
        pass
    elif i < gx:
        print(gy, i, 'R') 
    else:
        print(gy, i, 'L')
for i in range(40):
    if [i, gx] in b_list:
        pass
    elif i == gy:
        pass
    elif i < gy:
        print(i, gx, 'D')
    else:
        print(i, gx, 'U')

for i in neigh_list:
    print(i[0], i[1], i[2])
