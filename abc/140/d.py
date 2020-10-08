n, k = map(int, input().split())
s = input()
r_size = []
l_size = []
r_mode = False
l_mode = False
r_keep = 0
l_keep = 0
if s[0] == 'R':
    r_mode = True
else:
    l_mode = True
for i in range(n):
    if r_mode and s[i] == 'R':
        r_keep += 1
    elif l_mode and s[i] == 'L':
        l_keep += 1
    elif r_mode and s[i] == 'L':
        r_size.append(r_keep)
        r_keep = 0
        l_keep += 1
        r_mode = False
        l_mode = True
    elif l_mode and s[i] == 'R':
        l_size.append(l_keep)
        l_keep = 0
        r_keep += 1
        l_mode = False
        r_mode = True
r_point = sum(r_size)-len(r_size)
l_point = sum(l_size)-len(l_size)
r_size[0] -= 1
r_size[-1] -= 1
l_size[0] -= 1
r_size[-1] -= 1
new_r_size = sorted(r_size, reverse=True)
new_l_size = sorted(l_size, reverse=True)
print(new_r_size)
print(new_l_size)
r_ans = sum(r_size[:k-1])+k + r_point
l_ans = sum(l_size[:k-1])+k + l_point
if r_ans > l_ans:
    print(r_ans)
else:
    print(l_ans)