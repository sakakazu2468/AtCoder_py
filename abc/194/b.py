n = int(input())
ab_min = 10**6
a_min = 10**6
b_min = 10**6
ab_list = []
for i in range(n):
    ab_list.append(list(map(int, input().split())))
ans_list = []
for i in range(n):
    for j in range(n):
        if i==j:
            ans_list.append(ab_list[i][0]+ab_list[j][1])
        else:
            ans_list.append(max(ab_list[i][0], ab_list[j][1]))
print(min(ans_list))
