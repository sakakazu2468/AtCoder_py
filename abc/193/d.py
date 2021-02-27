k = int(input())
s = input()[:4]
t = input()[:4]

k_dict = {}
for i in range(1, 10):
    k_dict[i] = k

for i in s:
    k_dict[(int(i))] -= 1
for i in t:
    k_dict[(int(i))] -= 1

s_pt = [0 for _ in range(9)]
for i in range(1, 10):
    new_s = s + str(i)
    s_dict = {}
    for num in new_s:
        s_dict[num] = s_dict.get(num, 0) + 1
    for j in range(1, 10):
        s_pt[i-1] += j*(10**s_dict.get(str(j), 0))

t_pt = [0 for _ in range(9)]
for i in range(1, 10):
    new_t = t + str(i)
    t_dict = {}
    for num in new_t:
        t_dict[num] = t_dict.get(num, 0) + 1
    for j in range(1, 10):
        t_pt[i-1] += j*(10**t_dict.get(str(j), 0))

possible = 0
for i in range(1, 10):
    for j in range(1, 10):
        if s_pt[i-1] > t_pt[j-1]:
            if (i==j) and (k_dict.get(i)>=2):
                possible += k_dict.get(i)*(k_dict.get(i)-1)
            else:
                if (k_dict.get(i)>=1) and (k_dict.get(j)>=1):
                    possible += k_dict.get(i)*k_dict.get(j)

rem_sum = 0
for i in range(1, 10):
    rem_sum += k_dict.get(i)
all_possible = rem_sum*(rem_sum-1)
print(possible/all_possible)


